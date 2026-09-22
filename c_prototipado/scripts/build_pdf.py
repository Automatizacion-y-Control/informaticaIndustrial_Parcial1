#!/usr/bin/env python3
"""
build_pdf.py — Genera informeParcial1_infoInd.pdf del Parcial Nº 1 de Informática Industrial.

Fuentes que combina:
  - c_prototipado/informeParcial1_infoInd.md → contenido del informe (portada + cuerpo)
  - c_prototipado/assets/                    → capturas de pantalla referenciadas desde el .md
  - a_requisitos/diseño.md                   → editorial: tipografía, jerarquía, paleta, viñetas,
                                                bloques especiales, imágenes, tablas y maquetación
                                                de página (bloque YAML en la sección 10 de ese archivo)

Salida:
  - d_presentacion/informeParcial1_infoInd.pdf

Motor de render: Playwright (Chromium headless) → PDF, en dos pasadas que luego se combinan:
  1) portada (sin encabezado/pie, a página completa)
  2) cuerpo del informe (con encabezado, pie de página y numeración)
Se combinan con pypdf para que la numeración de página empiece en 1 recién en el cuerpo.

Uso:
    python build_pdf.py                # genera el PDF final
    python build_pdf.py --proof 4      # además exporta PNG de las primeras 4 páginas a
                                        # scripts/qa/ para control visual (requiere poppler)

Primer uso en una máquina nueva:
    pip install -r requirements.txt
    playwright install chromium        # descarga el navegador headless (una sola vez)

Tipografía: el script busca fuentes reales (Libre Baskerville, Source Serif 4, Source Sans 3,
JetBrains Mono) en scripts/fonts/*.ttf — ver requirements.txt / README para los nombres de
archivo esperados. Si no están presentes, usa equivalentes ya instalados en el sistema
(GFS Baskerville, DejaVu Serif/Sans/Mono, Liberation) sin romper la compilación.
"""

from __future__ import annotations

import argparse
import re
import sys
from dataclasses import dataclass, field
from pathlib import Path
from urllib.parse import quote

if sys.stdout.encoding and sys.stdout.encoding.lower() != "utf-8":
    sys.stdout.reconfigure(encoding="utf-8", errors="replace")
    sys.stderr.reconfigure(encoding="utf-8", errors="replace")

import markdown as md
import numpy as np
import yaml
from bs4 import BeautifulSoup
from playwright.sync_api import sync_playwright
from pypdf import PdfReader, PdfWriter

# ---------------------------------------------------------------------------
# Rutas del proyecto
# ---------------------------------------------------------------------------

SCRIPT_DIR = Path(__file__).resolve().parent
C_PROTOTIPADO_DIR = SCRIPT_DIR.parent
PROJECT_ROOT = C_PROTOTIPADO_DIR.parent

MD_PATH = C_PROTOTIPADO_DIR / "informeParcial1_infoInd.md"
ASSETS_DIR = C_PROTOTIPADO_DIR / "assets"
DESIGN_PATH = PROJECT_ROOT / "a_requisitos" / "diseño.md"
FONTS_DIR = SCRIPT_DIR / "fonts"
QA_DIR = SCRIPT_DIR / "qa"

OUTPUT_DIR = PROJECT_ROOT / "d_presentacion"
OUTPUT_PDF = OUTPUT_DIR / "informeParcial1_infoInd.pdf"

BUILD_DIR = SCRIPT_DIR / "_build"  # HTML/PDF intermedios, no es parte del entregable

# Archivos de fuentes reales esperados (opcionales). Si el usuario los coloca en
# scripts/fonts/ con estos nombres, se embeben vía @font-face con prioridad sobre
# los equivalentes del sistema.
FONT_FILES = {
    "Libre Baskerville": [
        ("normal", "normal", "LibreBaskerville-Regular.ttf"),
        ("bold", "normal", "LibreBaskerville-Bold.ttf"),
        ("normal", "italic", "LibreBaskerville-Italic.ttf"),
    ],
    "Source Serif 4": [
        ("normal", "normal", "SourceSerif4-Regular.ttf"),
        ("normal", "italic", "SourceSerif4-Italic.ttf"),
        ("bold", "normal", "SourceSerif4-Bold.ttf"),
    ],
    "Source Sans 3": [
        ("normal", "normal", "SourceSans3-Regular.ttf"),
        ("600", "normal", "SourceSans3-SemiBold.ttf"),
        ("normal", "italic", "SourceSans3-Italic.ttf"),
    ],
    "JetBrains Mono": [
        ("normal", "normal", "JetBrainsMono-Regular.ttf"),
        ("bold", "normal", "JetBrainsMono-Bold.ttf"),
    ],
}

# Equivalentes ya presentes en el sistema (fallback si no están las fuentes reales).
FALLBACKS = {
    "portada_h1": ['"GFS Baskerville"', '"DejaVu Serif"', '"Liberation Serif"', "Georgia", "serif"],
    "h2_h4": ['"DejaVu Sans"', '"Liberation Sans"', "Arial", "sans-serif"],
    "cuerpo": ['"DejaVu Serif"', '"Liberation Serif"', "Georgia", "serif"],
    "codigo": ['"DejaVu Sans Mono"', '"Liberation Mono"', '"Courier New"', "monospace"],
    "epigrafe": ['"DejaVu Sans"', '"Liberation Sans"', "Arial", "sans-serif"],
}

CALLOUT_LABELS = {
    "NOTA": ("info", "NOTA"),
    "VERIFICACIÓN": ("exito", "VERIFICACIÓN"),
    "VERIFICACION": ("exito", "VERIFICACIÓN"),
    "A TENER EN CUENTA": ("advertencia", "A TENER EN CUENTA"),
    "PROBLEMA ENCONTRADO": ("problema", "PROBLEMA ENCONTRADO"),
}


@dataclass
class BuildReport:
    """Hallazgos de consistencia recolectados durante la generación, para reportar al final."""
    figuras_insertadas: int = 0
    imagenes_faltantes: list[str] = field(default_factory=list)
    imagenes_sin_usar: list[str] = field(default_factory=list)
    callouts_detectados: int = 0
    fuentes_reales_encontradas: list[str] = field(default_factory=list)
    fuentes_reales_faltantes: list[str] = field(default_factory=list)


# ---------------------------------------------------------------------------
# 1. Carga de tokens de diseño (a_requisitos/diseño.md)
# ---------------------------------------------------------------------------

def load_design_tokens(path: Path) -> dict:
    if not path.exists():
        raise FileNotFoundError(
            f"No se encontró el archivo de editorial: {path}\n"
            "Se esperaba a_requisitos/diseño.md con un bloque ```yaml de tokens (sección 10)."
        )
    text = path.read_text(encoding="utf-8")
    match = re.search(r"```yaml\s*\n(.*?)\n```", text, re.DOTALL)
    if not match:
        raise ValueError(
            f"No se encontró el bloque ```yaml de tokens de diseño dentro de {path}. "
            "Revisá la sección 10 ('Tokens de diseño') de diseño.md."
        )
    tokens = yaml.safe_load(match.group(1))
    required = {"color", "tipografia", "escala_pt", "pagina", "vinetas"}
    missing = required - tokens.keys()
    if missing:
        raise ValueError(f"Faltan claves en los tokens de diseño.md: {sorted(missing)}")
    return tokens


def font_stack(tokens: dict, key: str) -> str:
    """Arma el stack CSS: nombre real deseado (diseño.md) + fallbacks del sistema."""
    deseado = tokens["tipografia"][key].split(",")[0].strip()
    partes = [f'"{deseado}"'] + FALLBACKS[key]
    # evitar duplicar si el nombre deseado coincide con el primer fallback
    vistos, resultado = set(), []
    for p in partes:
        if p not in vistos:
            resultado.append(p)
            vistos.add(p)
    return ", ".join(resultado)


def build_font_face_css(report: BuildReport) -> str:
    """Genera @font-face para las fuentes reales si el usuario las colocó en scripts/fonts/."""
    rules = []
    for family, faces in FONT_FILES.items():
        alguna_encontrada = False
        for weight, style, filename in faces:
            fpath = FONTS_DIR / filename
            if fpath.exists():
                alguna_encontrada = True
                uri = fpath.resolve().as_uri()
                rules.append(
                    f'@font-face {{ font-family: "{family}"; src: url("{uri}"); '
                    f"font-weight: {weight}; font-style: {style}; }}"
                )
        if alguna_encontrada:
            report.fuentes_reales_encontradas.append(family)
        else:
            report.fuentes_reales_faltantes.append(family)
    return "\n".join(rules)


# ---------------------------------------------------------------------------
# 2. Parseo del informe (portada + cuerpo)
# ---------------------------------------------------------------------------

COVER_BODY_SPLIT = "## Índice del documento"


def _parse_integrantes_tabla(tabla_md: str) -> list[dict[str, str]]:
    """Convierte una tabla Markdown '| Integrante | Legajo |' en una lista de dicts,
    descartando la fila de encabezado y la fila separadora (---)."""
    filas = []
    for linea in tabla_md.splitlines():
        linea = linea.strip()
        if not linea.startswith("|"):
            continue
        celdas = [c.strip().strip("*").strip() for c in linea.strip("|").split("|")]
        if len(celdas) < 2 or not celdas[0] or set(celdas[0]) <= {"-", ":"}:
            continue
        if celdas[0].lower() == "integrante":
            continue
        filas.append({"nombre": celdas[0], "legajo": celdas[1]})
    return filas


def parse_informe(path: Path) -> tuple[dict, str]:
    """La portada de este informe es Markdown plano de grupo (sin <div>, sin Docente/Alumno
    únicos): universidad, facultad, carrera, epígrafe ('Parcial N° X'), título, bajada,
    tabla de integrantes (nombre + legajo) y fecha, en ese orden, separados por línea en
    blanco. El cuerpo del informe arranca en COVER_BODY_SPLIT ('## Índice del documento')."""
    if not path.exists():
        raise FileNotFoundError(f"No se encontró el informe: {path}")
    text = path.read_text(encoding="utf-8")

    split_idx = text.find(COVER_BODY_SPLIT)
    if split_idx == -1:
        raise ValueError(f"No se encontró '{COVER_BODY_SPLIT}' que separa portada y cuerpo del informe.")
    cover_raw = text[:split_idx]
    body_raw = text[split_idx:]

    cover_raw = re.sub(r"<!--.*?-->", "", cover_raw, flags=re.DOTALL).strip()
    bloques = [b.strip() for b in re.split(r"\n\s*\n", cover_raw) if b.strip()]

    def sin_encabezado(bloque: str) -> str:
        return re.sub(r"^#+\s*", "", bloque).strip()

    def es_tabla(bloque: str) -> bool:
        return bloque.lstrip().startswith("|")

    def es_docente(bloque: str) -> bool:
        return bloque.lower().startswith("docente:")

    docente_bloque = next((b for b in bloques if es_docente(b)), "")
    docente = re.sub(r"(?i)^docente:\s*", "", docente_bloque).strip()

    textos = [b for b in bloques if not es_tabla(b) and not es_docente(b)]
    tablas = [b for b in bloques if es_tabla(b)]

    cover = dict(
        universidad=sin_encabezado(textos[0]) if len(textos) > 0 else "",
        facultad=textos[1] if len(textos) > 1 else "",
        carrera=textos[2] if len(textos) > 2 else "",
        tp=sin_encabezado(textos[3]) if len(textos) > 3 else "",
        titulo=sin_encabezado(textos[4]) if len(textos) > 4 else "",
        tema=re.sub(r"\s+", " ", textos[5]).strip() if len(textos) > 5 else "",
        docente=docente,
        fecha=textos[-1] if textos else "",
        integrantes=_parse_integrantes_tabla(tablas[0]) if tablas else [],
    )
    faltantes = [k for k, v in cover.items() if not v]
    if faltantes:
        print(f"[build_pdf] AVISO: no se pudieron extraer de la portada estos campos: {faltantes}", file=sys.stderr)

    return cover, body_raw


# ---------------------------------------------------------------------------
# 3. Conversión del cuerpo Markdown -> HTML, con figuras numeradas y callouts
# ---------------------------------------------------------------------------

def _unwrap_from_solo_p(tag) -> None:
    """Markdown envuelve una línea de imagen suelta en <p><img></p>. Como acá el img ya
    se reemplazó por un <figure> (o el aviso de imagen faltante) -que es un elemento de
    bloque-, si ese <p> quedó como único contenedor del tag lo desenvolvemos para que el
    bloque sea un hermano directo dentro de .cuerpo. Evita <p> vacíos (HTML inválido que
    el parser reacomoda distinto según el motor) y deja una lista plana de bloques, que es
    lo que necesita la simulación de paginación (simulate_pagination) para medir cada
    bloque una sola vez y calcular saltos de página de forma predecible."""
    parent = tag.parent
    if parent is not None and parent.name == "p" and len(parent.contents) == 1:
        parent.replace_with(tag)


def render_body_html(body_markdown: str, assets_dir: Path, report: BuildReport):
    html = md.markdown(
        body_markdown,
        extensions=["extra", "sane_lists", "codehilite"],
        extension_configs={"codehilite": {"guess_lang": False}},
    )
    soup = BeautifulSoup(html, "html.parser")

    # Los bloques ```sql (script T-SQL completo) van resaltados con colores de sintaxis
    # y en su propia hoja; el resto de los bloques de código (powershell, etc.) mantienen
    # el estilo plano habitual. codehilite no conserva el lenguaje del fence en el HTML,
    # así que se cruza por orden: el bloque de código Nº k del Markdown original con el
    # div.codehilite Nº k generado.
    fence_langs = re.findall(r"^```(\w+)", body_markdown, re.MULTILINE)
    codehilite_divs = soup.find_all("div", class_="codehilite")
    for lang, div in zip(fence_langs, codehilite_divs):
        if lang.lower() != "sql":
            continue
        div["class"] = div.get("class", []) + ["sql-script"]
        etiqueta = soup.new_tag("div")
        etiqueta["class"] = "code-lang-label"
        etiqueta.string = "SQL"
        div.insert(0, etiqueta)
        # El salto de hoja va en el encabezado que antecede al script (si lo hay), no en el
        # propio bloque de código: si el salto se aplicara al código, el encabezado ("### Parte
        # N — ...") queda huérfano al pie de la hoja anterior, seguido de una hoja casi vacía.
        heading = div.find_previous_sibling(["h1", "h2", "h3", "h4"])
        (heading if heading is not None else div)["class"] = \
            (heading if heading is not None else div).get("class", []) + ["antes-de-sql-script"]

    # Los tres bloques temáticos ("2. Bloque 1 — ...", "3. Bloque 2 — ...", "4. Bloque 3 — ...")
    # son el cuerpo propiamente dicho del informe (Introducción y Conclusiones son apertura y
    # cierre); se resaltan con un tratamiento propio para que se distingan de un H1 común.
    for h1 in soup.find_all("h1"):
        if re.match(r"^\s*\d+\.\s*Bloque\b", h1.get_text()):
            h1["class"] = h1.get("class", []) + ["h1-bloque"]

    existentes = {p.name for p in assets_dir.glob("*")} if assets_dir.exists() else set()
    usadas = set()

    figura_n = 0
    for img in soup.find_all("img"):
        src = img.get("src", "")
        nombre = Path(src).name
        alt = img.get("alt", "").strip()

        if src.startswith("assets/") and nombre in existentes:
            usadas.add(nombre)
            abs_uri = (assets_dir / nombre).resolve().as_uri()
            img["src"] = abs_uri

            # Normalización de tamaño: las capturas vienen de fuentes muy dispares (recortes
            # angostos y verticales de una consola, franjas horizontales de un solo campo de
            # AWS, capturas 16:9 completas...). El tope por defecto (max-height: 90mm) deja a
            # las muy verticales reducidas a una columna angosta e ilegible, y a las muy
            # horizontales como una franja finita. Se reclasifican por relación de aspecto real
            # para que cada una ocupe un tamaño legible y con peso visual consistente.
            try:
                from PIL import Image

                with Image.open(assets_dir / nombre) as im_probe:
                    ancho_px, alto_px = im_probe.size
                ratio = ancho_px / alto_px if alto_px else 1.0
            except Exception:
                ratio = 1.0
            if ratio < 0.6:
                img["class"] = "img-vertical"
            elif ratio > 2.4:
                img["class"] = "img-panoramica"

            figura_n += 1
            figure = soup.new_tag("figure")
            figure["id"] = f"fig-{figura_n}"
            img.replace_with(figure)
            figure.append(img)
            figcaption = soup.new_tag("figcaption")
            figcaption.string = f"Figura {figura_n}. {alt}" if alt else f"Figura {figura_n}."
            figure.append(figcaption)
            _unwrap_from_solo_p(figure)
        else:
            report.imagenes_faltantes.append(nombre or src)
            aviso = soup.new_tag("div")
            aviso["class"] = "imagen-faltante"
            aviso.string = f"⚠ Imagen no encontrada en assets/: {nombre or src}" + (f" ({alt})" if alt else "")
            img.replace_with(aviso)
            _unwrap_from_solo_p(aviso)

    report.figuras_insertadas = figura_n
    report.imagenes_sin_usar = sorted(existentes - usadas)

    # Callouts: blockquotes cuyo primer texto en negrita coincide con una etiqueta conocida
    for bq in soup.find_all("blockquote"):
        strong = bq.find("strong")
        if not strong:
            continue
        etiqueta = strong.get_text(strip=True).rstrip(":").upper()
        if etiqueta in CALLOUT_LABELS:
            clase, titulo = CALLOUT_LABELS[etiqueta]
            bq["class"] = f"callout callout-{clase}"
            titulo_tag = soup.new_tag("p")
            titulo_tag["class"] = "callout-titulo"
            titulo_tag.string = titulo
            strong.decompose()
            first_p = bq.find("p")
            if first_p is not None:
                first_p.insert_before(titulo_tag)
            report.callouts_detectados += 1

    return soup


# ---------------------------------------------------------------------------
# 4. CSS a partir de los tokens de diseño
# ---------------------------------------------------------------------------

def build_css(tokens: dict, report: BuildReport) -> str:
    c = tokens["color"]
    e = tokens["escala_pt"]
    v = tokens["vinetas"]
    p = tokens["pagina"]

    f_portada = font_stack(tokens, "portada_h1")
    f_h2h4 = font_stack(tokens, "h2_h4")
    f_cuerpo = font_stack(tokens, "cuerpo")
    f_codigo = font_stack(tokens, "codigo")
    f_epigrafe = font_stack(tokens, "epigrafe")

    font_face_css = build_font_face_css(report)

    return f"""
{font_face_css}

* {{ box-sizing: border-box; }}

html, body {{
  margin: 0; padding: 0;
  background: {c['fondo_pagina']};
  color: {c['grafito']};
  font-family: {f_cuerpo};
  font-size: {e['cuerpo']}pt;
  line-height: 1.5;
  orphans: 3; widows: 3;
}}

/* ---- Cuerpo del informe ---- */
.cuerpo {{ padding: 0; }}

h1 {{
  font-family: {f_portada};
  color: {c['azul_institucional']};
  font-size: {round(e['h1'] * 1.35, 1)}pt;
  font-weight: 700;
  margin: 16mm 0 6mm 0;
  padding-top: 3mm;
  border-top: 0.6mm solid {c['oro_academico']};
  break-before: page;
  break-after: avoid;
  page-break-before: always;
  page-break-after: avoid;
}}
/* El primer H1 del cuerpo ("1. Introducción...") sí debe saltar de hoja: el
   Índice del documento (H2) que lo precede necesita su propia hoja, no compartirla. */

/* Bloque 1 / Bloque 2 / Bloque 3: cuerpo central del informe, se resaltan con una
   banda de color propia (a todo el ancho de la hoja) para distinguirlos de un H1
   común (Introducción, Conclusiones). */
h1.h1-bloque {{
  color: {c['fondo_pagina']};
  background: {c['azul_institucional']};
  border-top: none;
  padding: 8mm {p['margen_lateral_mm']}mm;
  margin: 0 -{p['margen_lateral_mm']}mm 8mm -{p['margen_lateral_mm']}mm;
}}

h2 {{
  font-family: {f_portada};
  color: {c['azul_institucional']};
  font-size: {e['h1']}pt;
  font-weight: 700;
  margin: 12mm 0 4mm 0;
  padding-top: 2mm;
  border-top: 0.35mm solid {c['oro_academico']};
  break-after: avoid;
  page-break-after: avoid;
}}

h3 {{
  font-family: {f_h2h4};
  color: {c['grafito']};
  font-size: {e['h2']}pt;
  font-weight: 600;
  margin: 7mm 0 3mm 0;
  break-after: avoid;
  page-break-after: avoid;
}}

h4 {{
  font-family: {f_h2h4};
  color: {c['grafito']};
  font-size: {e['h3']}pt;
  font-weight: 600;
  font-variant: small-caps;
  letter-spacing: 0.02em;
  margin: 5mm 0 2mm 0;
}}

p {{ margin: 0 0 3.2mm 0; text-align: justify; hyphens: auto; }}

strong {{ font-weight: 700; }}
em {{ font-style: italic; }}

a {{ color: {c['azul_institucional']}; text-decoration: none; border-bottom: 0.3pt solid {c['azul_institucional']}; }}

/* ---- Listas ---- */
ul {{ margin: 0 0 3.2mm 0; padding-left: 6mm; list-style: none; }}
ul > li {{ position: relative; margin-bottom: 1.3mm; padding-left: 4.5mm; }}
ul > li::before {{
  content: "{v['nivel_1']}"; position: absolute; left: 0; color: {c['oro_academico']};
}}
ul ul {{ margin-top: 1.3mm; }}
ul ul > li::before {{ content: "{v['nivel_2']}"; color: {c['grafito']}; }}
ul ul ul > li::before {{ content: "{v['nivel_3']}"; color: {c['grafito']}; }}

ol {{ margin: 0 0 3.2mm 0; padding-left: 7mm; }}
ol > li {{ margin-bottom: 1.3mm; padding-left: 1mm; }}
ol > li::marker {{ color: {c['azul_institucional']}; font-weight: 700; }}

/* ---- Código / comandos ---- */
code {{
  font-family: {f_codigo}; font-size: {e['codigo']}pt;
  background: {c['fondo_bloque']}; padding: 0.3mm 1.2mm; border-radius: 0.6mm;
}}
pre {{
  font-family: {f_codigo}; font-size: {e['codigo']}pt;
  background: {c['fondo_bloque']}; border-left: 1pt solid {c['gris_linea']};
  padding: 3mm 4mm; margin: 0 0 4mm 0; overflow-wrap: break-word; white-space: pre-wrap;
  break-inside: avoid; page-break-inside: avoid;
}}
pre code {{ background: none; padding: 0; }}

/* ---- Script SQL completo: hoja propia + resaltado de sintaxis clásico ---- */
.codehilite {{ margin: 0 0 4mm 0; }}
/* El salto de hoja se aplica al encabezado que antecede al script (o al propio bloque
   si no hay encabezado), para que ambos viajen juntos a la hoja nueva. */
.antes-de-sql-script {{
  break-before: page !important; page-break-before: always !important;
}}
.code-lang-label {{
  font-family: {f_h2h4}; font-size: 8.5pt; font-weight: 700; letter-spacing: 0.08em;
  text-transform: uppercase; color: {c['azul_institucional']}; margin-bottom: 2mm;
}}
.sql-script pre {{ background: #F7F8FA; }}
.sql-script .k  {{ color: #0033AA; font-weight: 700; }}   /* palabras clave: SELECT, CREATE, FROM... */
.sql-script .nb {{ color: #7A2CA0; font-weight: 600; }}   /* tipos de dato: INT, VARCHAR, DECIMAL... */
.sql-script .s1, .sql-script .s2 {{ color: #A31515; }}    /* literales de texto */
.sql-script .mi, .sql-script .mf {{ color: #0B7285; }}    /* literales numéricos */
.sql-script .c1, .sql-script .cm {{ color: #2F855A; font-style: italic; }}  /* comentarios -- */
.sql-script .n  {{ color: {c['grafito']}; }}              /* identificadores (tablas, columnas) */
.sql-script .o, .sql-script .p {{ color: {c['grafito']}; }}  /* operadores y puntuación */

/* ---- Figuras ---- */
/* Tope de altura pensado para que entren hasta 2 figuras por hoja en el area
   de contenido (A4, 242mm de alto util con los margenes de pagina.md):
   2 x (90mm imagen + ~6mm epigrafe + 9mm margenes de figura) ~= 210mm,
   dejando margen para algun titulo/parrafo intercalado. */
figure {{
  margin: 4mm 0 5mm 0; text-align: center;
  break-inside: avoid; page-break-inside: avoid;
}}
figure img {{
  max-width: 100%; max-height: 90mm; width: auto; height: auto;
  display: block; margin: 0 auto;
  border: 0.5pt solid {c['gris_linea']};
}}
/* Capturas muy verticales (relación ancho/alto < 0.6, ej. explorador de archivos, consola
   completa): el tope por altura las dejaba en una columna angosta e ilegible; se prioriza
   un ancho legible y se les permite ocupar más alto de página. */
figure img.img-vertical {{
  max-height: 170mm; max-width: 95mm;
}}
/* Capturas muy panorámicas (relación > 2.4, ej. recorte de un solo campo de una consola web):
   se limita el ancho para que no se estiren de borde a borde como una franja accidental. */
figure img.img-panoramica {{
  max-width: 130mm; max-height: none;
}}
figcaption {{
  font-family: {f_epigrafe}; font-style: italic; font-size: {e['epigrafe']}pt;
  color: {c['grafito']}; opacity: 0.8; margin-top: 2mm;
}}
.imagen-faltante {{
  font-family: {f_epigrafe}; font-size: {e['cuerpo']}pt; color: {c['problema']};
  background: {c['fondo_bloque']}; border-left: 3mm solid {c['problema']};
  padding: 3mm 4mm; margin: 4mm 0; break-inside: avoid; page-break-inside: avoid;
}}

/* ---- Tablas ---- */
table {{
  width: 100%; border-collapse: collapse; margin: 4mm 0 6mm 0;
  font-size: {e['cuerpo'] - 0.5}pt; break-inside: avoid; page-break-inside: avoid;
}}
thead th {{
  background: {c['azul_institucional']}; color: #FFFFFF;
  font-family: {f_h2h4}; font-weight: 600; text-align: left;
  padding: 2mm 3mm; border: none;
}}
tbody td {{ padding: 2mm 3mm; border-bottom: 0.4pt solid {c['gris_linea']}; }}
tbody tr:nth-child(even) td {{ background: {c['fondo_bloque']}; }}

/* ---- Bloques especiales (callouts) ---- */
.callout {{
  margin: 4mm 0; padding: 3mm 4mm; background: {c['fondo_bloque']};
  border-left: 3mm solid {c['grafito']};
  break-inside: avoid; page-break-inside: avoid;
}}
.callout p {{ margin: 0 0 1.5mm 0; text-align: left; }}
.callout-titulo {{
  font-family: {f_h2h4}; font-weight: 600; font-variant: small-caps;
  letter-spacing: 0.04em; margin-bottom: 1.5mm !important;
}}
.callout-info {{ border-left-color: {c['info']}; }}
.callout-info .callout-titulo {{ color: {c['info']}; }}
.callout-exito {{ border-left-color: {c['exito']}; }}
.callout-exito .callout-titulo {{ color: {c['exito']}; }}
.callout-advertencia {{ border-left-color: {c['advertencia']}; }}
.callout-advertencia .callout-titulo {{ color: {c['advertencia']}; }}
.callout-problema {{ border-left-color: {c['problema']}; }}
.callout-problema .callout-titulo {{ color: {c['problema']}; }}

/* ---- Portada ---- */
.portada {{
  width: 100%; height: 100vh; box-sizing: border-box;
  display: flex; flex-direction: column; align-items: center; justify-content: center;
  text-align: center; padding: 20mm 25mm;
  border-top: 3mm solid {c['oro_academico']};
  border-bottom: 3mm solid {c['oro_academico']};
}}
.portada .universidad {{
  font-family: {f_h2h4}; font-size: 11pt; font-weight: 600; letter-spacing: 0.03em;
  color: {c['grafito']}; text-transform: uppercase;
}}
.portada .facultad {{
  font-family: {f_h2h4}; font-size: 10pt; color: {c['grafito']};
}}
.portada .carrera {{
  font-family: {f_h2h4}; font-size: 9.5pt; color: {c['grafito']}; opacity: 0.85; margin-bottom: 10mm;
}}
.portada .materia {{
  font-family: {f_h2h4}; font-size: 12pt; font-weight: 600; letter-spacing: 0.06em;
  text-transform: uppercase; color: {c['oro_academico']}; margin-bottom: 6mm;
}}
.portada .titulo {{
  font-family: {f_portada}; font-size: {e['portada']}pt; font-weight: 700;
  color: {c['azul_institucional']}; line-height: 1.15; margin-bottom: 4mm;
}}
.portada .tema {{
  font-family: {f_cuerpo}; font-style: italic; font-size: 13pt;
  color: {c['grafito']}; max-width: 130mm; margin-bottom: 14mm;
}}
.portada .metadatos {{
  font-family: {f_h2h4}; font-size: 10pt; color: {c['grafito']};
}}
.portada .integrantes-titulo {{
  font-size: 8.5pt; font-weight: 600; letter-spacing: 0.08em; text-transform: uppercase;
  color: {c['oro_academico']}; margin-bottom: 2mm;
}}
.portada .integrantes-tabla {{
  border-collapse: collapse; margin: 0 auto 8mm auto;
}}
.portada .integrantes-tabla td {{
  padding: 0.6mm 3mm; line-height: 1.6;
}}
.portada .integrantes-tabla td:last-child {{
  color: {c['azul_institucional']}; font-weight: 600; text-align: left;
}}
.portada .docente {{
  font-size: 10pt; margin-bottom: 2mm;
}}
.portada .fecha {{
  font-size: 10pt;
}}
""".strip()


# ---------------------------------------------------------------------------
# 4bis. Paginación: evita hojas con una figura sola y medio página en blanco
# ---------------------------------------------------------------------------
#
# El navegador decide sólo con CSS (max-height fijo + break-inside: avoid) si una figura
# entra entera en lo que queda de hoja; si no entra, la manda completa a la hoja siguiente
# y deja un hueco en blanco donde no entró. Con capturas de pantalla grandes ese hueco
# puede ser media hoja, lo cual no es aceptable en una edición prolija.
#
# En vez de tratar de predecir de antemano cómo va a paginar Chromium (frágil: depende de
# reglas de orphans/widows, de break-after:avoid en encabezados, de redondeos, etc. —
# se probó y el resultado no siempre coincidía con la paginación real), se usa el PDF real
# como fuente de verdad: se renderiza, se mide con Chromium/pdf2image cuánto blanco quedó
# al final de cada hoja del cuerpo y, con el texto embebido "Figura N." de cada epígrafe
# (pypdf), se sabe qué figura abre cada hoja siguiente. Si una hoja tiene un hueco grande
# y la hoja siguiente arranca con una figura, se achica esa figura (nunca por debajo de un
# mínimo legible) y se vuelve a renderizar. Se repite unas pocas veces hasta que no queden
# huecos grandes explicables por una figura, o hasta un tope de iteraciones.

MM_TO_PX = 96 / 25.4
PX_TO_MM = 25.4 / 96

MIN_FIGURA_MM = 62.0       # piso absoluto: nunca achicar una figura por debajo de esto
MIN_ANCHO_FRACCION = 0.60  # y nunca dejarla más angosta que este % del ancho de contenido
PASO_MAX_MM = 18.0         # achique máximo por iteración (evita saltar directo al piso)
GAP_UMBRAL_MM = 42.0       # sólo vale la pena corregir huecos realmente grandes al pie
MAX_ITERACIONES = 5


def _extraer_pagina_por_figura(pdf_path: Path) -> dict[int, int]:
    """{numero_de_figura: numero_de_pagina (1-indexed, dentro de este PDF de sólo cuerpo)},
    leyendo el texto "Figura N." que dejó cada <figcaption> ya embebido en el PDF."""
    reader = PdfReader(str(pdf_path))
    patron = re.compile(r"Figura\s+(\d+)\.")
    resultado: dict[int, int] = {}
    for i, pg in enumerate(reader.pages, start=1):
        texto = pg.extract_text() or ""
        for m in patron.finditer(texto):
            n = int(m.group(1))
            resultado.setdefault(n, i)  # sólo la primera vez que aparece (por si se repite)
    return resultado


def _huecos_al_pie_mm(pdf_path: Path, tokens: dict) -> dict[int, float]:
    """{numero_de_pagina: mm en blanco entre el último contenido y el margen inferior}."""
    from pdf2image import convert_from_path

    p = tokens["pagina"]
    top_mm = p["margen_superior_mm"]
    bottom_mm = 297 - p["margen_inferior_mm"]
    dpi = 100

    huecos: dict[int, float] = {}
    for idx, im in enumerate(convert_from_path(str(pdf_path), dpi=dpi), start=1):
        arr = np.array(im.convert("L"))
        top_px = int(top_mm / 25.4 * dpi)
        bottom_px = int(bottom_mm / 25.4 * dpi)
        region = arr[top_px:bottom_px, :]
        # fila "con contenido" = suficientes píxeles claramente no blancos (letras, bordes,
        # capturas); un par de píxeles sueltos se ignoran (antialiasing/ruido de compresión).
        con_contenido = np.where((region < 245).sum(axis=1) > 3)[0]
        ultimo_px = con_contenido.max() if len(con_contenido) else 0
        ultimo_mm = top_mm + ultimo_px / dpi * 25.4
        huecos[idx] = bottom_mm - ultimo_mm
    return huecos


def _aspect_ratio_img(img) -> float:
    """Ancho/alto de la imagen fuente (vía PIL), para no achicarla por debajo de un ancho
    razonable. Si no se puede leer, asume 16:9 (lo más común en las capturas del TP)."""
    src = img.get("src", "")
    try:
        from PIL import Image

        ruta = src.replace("file://", "", 1) if src.startswith("file://") else src
        with Image.open(ruta) as im:
            w, h = im.size
            if h > 0:
                return w / h
    except Exception:
        pass
    return 16 / 9


def refinar_paginacion(soup, css: str, tokens: dict, render_cuerpo_pdf) -> dict[str, float]:
    """Itera render -> medir hueco real -> achicar la figura que abre la hoja siguiente,
    hasta que no queden huecos grandes o se llegue al tope de iteraciones. render_cuerpo_pdf
    es una función que, dado el HTML del cuerpo, devuelve la ruta al PDF (sólo cuerpo,
    sin portada) ya renderizado. Devuelve {fig_id: alto_mm_aplicado} para loguear.

    El achique es deliberadamente conservador: sólo ataca huecos grandes (no los ~20-40mm
    que son normales al cierre de una sección en cualquier informe), avanza de a pasos
    chicos (no salta directo al mínimo) y nunca deja una figura ni por debajo de un alto
    mínimo legible ni más angosta que una fracción del ancho de contenido -evita que una
    captura de aspecto casi cuadrado termine como un sello diminuto rodeado de blanco."""
    ancho_contenido_mm = 210 - 2 * tokens["pagina"]["margen_lateral_mm"]
    alturas_actuales: dict[str, float] = {}
    pisos_por_figura: dict[str, float] = {}

    for iteracion in range(1, MAX_ITERACIONES + 1):
        body_html = render_body_document(str(soup), css)
        pdf_path = render_cuerpo_pdf(body_html)

        pagina_de_figura = _extraer_pagina_por_figura(pdf_path)
        huecos = _huecos_al_pie_mm(pdf_path, tokens)

        cambios = False
        for pagina, hueco_mm in huecos.items():
            if hueco_mm < GAP_UMBRAL_MM:
                continue
            siguiente = pagina + 1
            figs_en_siguiente = sorted(n for n, pg in pagina_de_figura.items() if pg == siguiente)
            if not figs_en_siguiente:
                continue  # la hoja siguiente no arranca con una figura; no hay qué achicar

            fig_num = figs_en_siguiente[0]
            fig_id = f"fig-{fig_num}"
            fig = soup.find(id=fig_id)
            img = fig.find("img") if fig else None
            if img is None:
                continue

            if fig_id not in pisos_por_figura:
                aspecto = _aspect_ratio_img(img)
                piso_por_ancho = (MIN_ANCHO_FRACCION * ancho_contenido_mm) / aspecto
                pisos_por_figura[fig_id] = max(MIN_FIGURA_MM, piso_por_ancho)
            piso = pisos_por_figura[fig_id]

            alto_actual = alturas_actuales.get(fig_id, 90.0)
            achique = min(hueco_mm - 2.0, PASO_MAX_MM)  # paso acotado, deja ~2mm de margen
            alto_nuevo = max(alto_actual - achique, piso)

            if alto_nuevo < alto_actual - 0.5:
                img["style"] = f"max-height:{alto_nuevo:.1f}mm;"
                alturas_actuales[fig_id] = alto_nuevo
                cambios = True

        if not cambios:
            break

    return alturas_actuales


# ---------------------------------------------------------------------------
# 5. Plantillas HTML (portada / cuerpo)
# ---------------------------------------------------------------------------

def render_cover_html(cover: dict, css: str) -> str:
    filas_integrantes = "\n".join(
        f'      <tr><td>{i["nombre"]}</td><td>{i["legajo"]}</td></tr>'
        for i in cover["integrantes"]
    )
    return f"""<!doctype html>
<html lang="es"><head><meta charset="utf-8"><style>{css}</style></head>
<body>
  <div class="portada">
    <div class="universidad">{cover['universidad']}</div>
    <div class="facultad">{cover['facultad']}</div>
    <div class="carrera">{cover['carrera']}</div>
    <div class="materia">{cover['tp']}</div>
    <div class="titulo">{cover['titulo']}</div>
    <div class="tema">{cover['tema']}</div>
    <div class="metadatos">
      <div class="integrantes-titulo">Integrantes</div>
      <table class="integrantes-tabla">
{filas_integrantes}
      </table>
      <div class="docente">Docente: {cover['docente']}</div>
      <div class="fecha">{cover['fecha']}</div>
    </div>
  </div>
</body></html>"""


def render_body_document(body_html: str, css: str) -> str:
    return f"""<!doctype html>
<html lang="es"><head><meta charset="utf-8"><style>{css}</style></head>
<body><div class="cuerpo">{body_html}</div></body></html>"""


# ---------------------------------------------------------------------------
# 6. Render a PDF con Playwright + combinación de portada y cuerpo
# ---------------------------------------------------------------------------

def _header_footer_templates(tokens: dict, titulo_encabezado: str) -> tuple[str, str]:
    p = tokens["pagina"]
    margin_side = f"{p['margen_lateral_mm']}mm"
    c = tokens["color"]
    f_h2h4_names = tokens["tipografia"]["h2_h4"]

    header_template = f"""
    <div style="width:100%; margin:0 {margin_side}; font-family:{f_h2h4_names},'DejaVu Sans',sans-serif;
                font-size:8pt; color:{c['grafito']}; opacity:0.85; letter-spacing:0.04em;
                text-transform:uppercase; border-bottom:0.5pt solid {c['gris_linea']}; padding-bottom:1.5mm;">
      {titulo_encabezado}
    </div>"""

    footer_template = f"""
    <div style="width:100%; margin:0 {margin_side}; font-family:{f_h2h4_names},'DejaVu Sans',sans-serif;
                font-size:8.5pt; color:{c['grafito']}; opacity:0.85; display:flex; justify-content:space-between;
                border-top:0.5pt solid {c['gris_linea']}; padding-top:1.5mm;">
      <span>UTN Facultad Regional Córdoba — Informática Industrial</span>
      <span>Página <span class="pageNumber"></span> de <span class="totalPages"></span></span>
    </div>"""
    return header_template, footer_template


def render_cover_pdf(cover_html: str) -> Path:
    BUILD_DIR.mkdir(parents=True, exist_ok=True)
    cover_html_path = BUILD_DIR / "portada.html"
    cover_pdf_path = BUILD_DIR / "portada.pdf"
    cover_html_path.write_text(cover_html, encoding="utf-8")

    with sync_playwright() as pw:
        browser = pw.chromium.launch()
        page = browser.new_page()
        page.goto(cover_html_path.resolve().as_uri())
        page.pdf(
            path=str(cover_pdf_path), format="A4",
            print_background=True, prefer_css_page_size=False,
            margin={"top": "0mm", "bottom": "0mm", "left": "0mm", "right": "0mm"},
            display_header_footer=False,
        )
        browser.close()
    return cover_pdf_path


def render_body_pdf(body_html: str, tokens: dict, titulo_encabezado: str) -> Path:
    """Renderiza sólo el cuerpo (encabezado/pie/numeración). Se usa varias veces durante
    refinar_paginacion (cada iteración necesita el PDF real para medir) y una vez más para
    el resultado final."""
    BUILD_DIR.mkdir(parents=True, exist_ok=True)
    body_html_path = BUILD_DIR / "cuerpo.html"
    body_pdf_path = BUILD_DIR / "cuerpo.pdf"
    body_html_path.write_text(body_html, encoding="utf-8")

    p = tokens["pagina"]
    margin_top = f"{p['margen_superior_mm']}mm"
    margin_bottom = f"{p['margen_inferior_mm']}mm"
    margin_side = f"{p['margen_lateral_mm']}mm"
    header_template, footer_template = _header_footer_templates(tokens, titulo_encabezado)

    with sync_playwright() as pw:
        browser = pw.chromium.launch()
        page = browser.new_page()
        page.goto(body_html_path.resolve().as_uri())
        page.pdf(
            path=str(body_pdf_path), format="A4",
            print_background=True,
            margin={"top": margin_top, "bottom": margin_bottom, "left": margin_side, "right": margin_side},
            display_header_footer=True,
            header_template=header_template,
            footer_template=footer_template,
        )
        browser.close()
    return body_pdf_path


def merge_pdfs(cover_pdf: Path, body_pdf: Path, output_path: Path) -> None:
    writer = PdfWriter()
    for p in (cover_pdf, body_pdf):
        reader = PdfReader(str(p))
        for pg in reader.pages:
            writer.add_page(pg)
    output_path.parent.mkdir(parents=True, exist_ok=True)
    with open(output_path, "wb") as f:
        writer.write(f)


# ---------------------------------------------------------------------------
# 7. Control visual opcional (--proof N)
# ---------------------------------------------------------------------------

def export_proof_pages(pdf_path: Path, n_pages: int) -> list[Path]:
    from pdf2image import convert_from_path

    QA_DIR.mkdir(parents=True, exist_ok=True)
    images = convert_from_path(str(pdf_path), dpi=150, first_page=1, last_page=n_pages)
    out_paths = []
    for i, img in enumerate(images, start=1):
        out = QA_DIR / f"pagina_{i:02d}.png"
        img.save(out)
        out_paths.append(out)
    total = len(PdfReader(str(pdf_path)).pages)
    if total > n_pages:
        last = convert_from_path(str(pdf_path), dpi=150, first_page=total, last_page=total)[0]
        out = QA_DIR / f"pagina_{total:02d}_ultima.png"
        last.save(out)
        out_paths.append(out)
    return out_paths


# ---------------------------------------------------------------------------
# main
# ---------------------------------------------------------------------------

def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument("--proof", type=int, default=0, metavar="N",
                         help="exporta PNG de control de las primeras N páginas (+ la última) a scripts/qa/")
    args = parser.parse_args()

    report = BuildReport()

    print(f"[build_pdf] Leyendo editorial: {DESIGN_PATH}")
    tokens = load_design_tokens(DESIGN_PATH)

    print(f"[build_pdf] Leyendo informe: {MD_PATH}")
    cover, body_md = parse_informe(MD_PATH)
    titulo_encabezado = f"{cover['carrera'].split('·')[-1].strip()} — {cover['tp']}"

    print("[build_pdf] Convirtiendo Markdown -> HTML y resolviendo imágenes...")
    body_soup = render_body_html(body_md, ASSETS_DIR, report)

    css = build_css(tokens, report)

    print("[build_pdf] Ajustando paginación (render real, sin huecos grandes)...")
    alturas = refinar_paginacion(
        body_soup, css, tokens,
        render_cuerpo_pdf=lambda body_html: render_body_pdf(body_html, tokens, titulo_encabezado),
    )
    if alturas:
        print(f"    - {len(alturas)} figura(s) achicada(s) para cerrar la hoja: "
              + ", ".join(f"{k} ({v:.0f}mm)" for k, v in alturas.items()))
    else:
        print("    - no hicieron falta ajustes.")

    cover_html = render_cover_html(cover, css)
    body_html = render_body_document(str(body_soup), css)

    print("[build_pdf] Renderizando PDF final con Chromium (Playwright)...")
    cover_pdf = render_cover_pdf(cover_html)
    body_pdf = render_body_pdf(body_html, tokens, titulo_encabezado)

    print(f"[build_pdf] Combinando portada + cuerpo -> {OUTPUT_PDF}")
    merge_pdfs(cover_pdf, body_pdf, OUTPUT_PDF)

    total_paginas = len(PdfReader(str(OUTPUT_PDF)).pages)

    print("\n" + "=" * 70)
    print("REPORTE DE CONSISTENCIA")
    print("=" * 70)
    print(f"PDF generado: {OUTPUT_PDF}  ({total_paginas} páginas)")
    print(f"Figuras insertadas: {report.figuras_insertadas}")
    if report.imagenes_faltantes:
        print(f"⚠ Imágenes referenciadas en el .md que NO existen en assets/ ({len(report.imagenes_faltantes)}):")
        for nombre in report.imagenes_faltantes:
            print(f"    - {nombre}")
    else:
        print("Imágenes referenciadas: todas encontradas en assets/.")
    if report.imagenes_sin_usar:
        print(f"ℹ Archivos en assets/ que no están referenciados en el informe ({len(report.imagenes_sin_usar)}):")
        for nombre in report.imagenes_sin_usar:
            print(f"    - {nombre}")
    print(f"Callouts detectados (bloques NOTA/VERIFICACIÓN/ADVERTENCIA/PROBLEMA ENCONTRADO): {report.callouts_detectados}")
    if report.fuentes_reales_encontradas:
        print(f"Fuentes reales embebidas desde scripts/fonts/: {report.fuentes_reales_encontradas}")
    if report.fuentes_reales_faltantes:
        print(f"ℹ Fuentes de diseño.md no encontradas en scripts/fonts/ (se usó equivalente del sistema): {report.fuentes_reales_faltantes}")
    print("=" * 70)

    if args.proof:
        print(f"\n[build_pdf] Exportando control visual de {args.proof} página(s) + última a {QA_DIR}/")
        paths = export_proof_pages(OUTPUT_PDF, args.proof)
        for p in paths:
            print(f"    - {p}")


if __name__ == "__main__":
    main()
