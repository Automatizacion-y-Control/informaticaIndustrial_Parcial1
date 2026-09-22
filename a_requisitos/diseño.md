# Diseño Editorial — Informe TP Nº 1

**Editorial académica superior para la generación del informe en PDF** (`c_prototipado/informatica_TP01.md` + `assets/` → PDF final).

Este documento es la fuente única de verdad del estilo visual del informe. El script `c_prototipado/scripts/build_pdf.py` debe leer estos criterios (tipografías, colores, jerarquía, viñetas, bloques especiales y maquetación de página) para renderizar el PDF; ningún valor de diseño debería quedar hardcodeado en el script sin estar definido acá primero.

Formato de generación previsto: HTML + CSS → **WeasyPrint**. Las unidades de página van en `mm`, evitar emoji en el HTML final (WeasyPrint no las renderiza de forma consistente) y usar `break-inside: avoid` en bloques que no deban partirse entre páginas (figuras, tablas, callouts).

---

## 1. Identidad editorial

Editorial técnico-académica de nivel superior: sobria, con jerarquía clara y aire (whitespace) generoso, pensada para un informe de ingeniería con procedimiento paso a paso, capturas de pantalla y hallazgos técnicos. Referencia de tono: publicaciones técnicas universitarias (MIT Press / O'Reilly en su vertiente más formal), no una presentación corporativa ni un slide.

Principios:

- **Contraste tipográfico con propósito**: serif con carácter en portada y títulos de nivel 1, sans-serif técnica en el resto de la jerarquía y el cuerpo, monoespaciada solo para comandos, rutas y código.
- **Color como sistema, no como decoración**: una paleta institucional acotada + colores semánticos reservados exclusivamente para notas, advertencias e incidencias — nunca decorativos.
- **Numeración explícita**: las secciones del informe siguen numeración decimal (`1.`, `2.`, `3.` …), heredada de la resolución paso a paso ya redactada en `informatica_TP01.md`. El diseño no debe introducir una segunda numeración en conflicto.
- **Evidencia visual protagonista**: las capturas de pantalla (`assets/`) llevan numeración de figura y epígrafe; nunca flotan sin contexto.

## 2. Tipografía

| Uso | Familia | Fallback | Peso | Notas |
|---|---|---|---|---|
| Portada / título del informe | **Libre Baskerville** | Georgia, serif | 700 | Serif editorial clásica, con autoridad académica |
| Título H1 (secciones principales) | **Libre Baskerville** | Georgia, serif | 700 | Mismo trazo que portada, coherencia de tapa a cuerpo |
| Títulos H2–H4 | **Source Sans 3** | "Segoe UI", Arial, sans-serif | 600 | Sans técnica, alto contraste con el cuerpo serif |
| Cuerpo de texto | **Source Serif 4** | Georgia, serif | 400 | Serif de lectura larga, buena legibilidad en impresión/PDF |
| Comandos, rutas, código | **JetBrains Mono** | "Courier New", monospace | 400 / 500 (negrita para valores clave) | Uso en `ipconfig`, rutas como `D:\Sources\SxS`, IPs |
| Epígrafes de figura / notas al pie | **Source Sans 3** | "Segoe UI", Arial, sans-serif | 400 itálica | Tamaño reducido respecto al cuerpo |

Fuentes obtenidas de Google Fonts (embebibles para WeasyPrint vía `@font-face` con los `.ttf`/`.woff2` locales, no depender de red en tiempo de build).

### Escala tipográfica (base 11.5 px de cuerpo, adecuada a contenido denso)

| Elemento | Tamaño | Interlineado |
|---|---|---|
| Título de portada | 34 pt | 1.15 |
| H1 (`## N. Sección`) | 20 pt | 1.2 |
| H2 (`### N.N Subsección`) | 15 pt | 1.25 |
| H3 | 12.5 pt | 1.3 |
| Cuerpo | 11.5 pt | 1.5 |
| Código / comandos | 10 pt | 1.4 |
| Epígrafe de figura | 9.5 pt | 1.3 |
| Nota al pie / metadatos de portada | 9 pt | 1.3 |

## 3. Jerarquía de títulos

- **H1** — numerado (`1.`, `2.`, `3.`…), color primario, precedido por una regla horizontal fina en color acento y separación generosa antes del bloque (mínimo 14 mm en página).
- **H2** — numeración decimal heredada del cuerpo (`5.1`, `5.2`…) cuando corresponda, color grafito, sin regla.
- **H3** — versalitas o negrita simple, mismo color que el cuerpo, se usa para agrupar dentro de un paso (p. ej. "Fecha y hora", "Nombre del equipo" dentro de la sección de configuración post-instalación).
- **H4** — reservado para aclaraciones puntuales dentro de un H3 (uso excepcional).

No se introducen íconos ni emoji en los títulos del PDF (a diferencia de los README, que sí los usan). El informe académico mantiene un registro más formal.

## 4. Paleta de colores

Paleta institucional acotada + semántica reservada. Sin colores decorativos fuera de esta lista.

### 4.1 Institucional

| Token | Hex | Uso |
|---|---|---|
| `azul-institucional` | `#1B3A6B` | Título de portada, H1, líneas de regla, encabezado/pie de página |
| `grafito` | `#2E3440` | Cuerpo de texto, H2/H3 |
| `oro-academico` | `#B8912F` | Acentos de numeración, filete bajo H1, borde de portada |
| `gris-linea` | `#D7DBE0` | Reglas horizontales secundarias, bordes de tabla |
| `fondo-pagina` | `#FFFFFF` | Fondo general |
| `fondo-bloque` | `#F5F6F8` | Fondo de bloques de código y callouts neutros |

### 4.2 Semántica (solo para bloques especiales, sección 6)

| Token | Hex | Uso |
|---|---|---|
| `info` | `#2B6CB0` | Notas aclaratorias |
| `exito` | `#2F855A` | Verificaciones exitosas (ej. conectividad confirmada) |
| `advertencia` | `#B7791F` | Consideraciones a tener en cuenta |
| `problema` | `#C53030` | Incidencias / problemas encontrados durante la instalación (requisito explícito del TP) |

## 5. Viñetas y listas

- **Nivel 1**: marcador cuadrado sólido en `oro-academico` (`▪`), no el bullet redondo por defecto.
- **Nivel 2**: guion medio (`–`) en `grafito`.
- **Nivel 3**: círculo hueco (`○`), uso excepcional.
- **Listas numeradas** (pasos de procedimiento): numeración arábiga con punto (`1.`, `2.`…) en `azul-institucional`, negrita solo el número.
- Ítems de lista con más de dos líneas: sangría colgante alineada al texto, no al marcador.

## 6. Bloques especiales

Callouts con barra lateral de 3 mm en el color semántico correspondiente (sección 4.2), fondo `fondo-bloque`, título corto en versalitas sans-serif:

- **NOTA** (`info`): aclaración teórica breve, remite implícitamente a la investigación de base.
- **VERIFICACIÓN** (`exito`): resultado positivo de una prueba (ping, IIS respondiendo, etc.).
- **A TENER EN CUENTA** (`advertencia`): decisiones de configuración relevantes (p. ej. no desactivar el firewall).
- **PROBLEMA ENCONTRADO** (`problema`): incidencia real durante la instalación y su resolución (obligatorio por consigna, sección 6 de `a_requisitos`).

Bloques de código/comandos (`ipconfig`, `ping`, `Install-WindowsFeature…`): fondo `fondo-bloque`, tipografía monoespaciada, sin numeración de línea, borde izquierdo 1 pt `gris-linea`.

## 7. Imágenes y figuras

- Cada captura de `assets/` se numera correlativamente: **Figura N.** seguida de epígrafe descriptivo en `Source Sans 3` itálica, `grafito` al 80 % de opacidad.
- Ancho máximo de imagen: 100 % de la caja de texto, centrada, con borde fino 0.5 pt `gris-linea` y sombra sutil no permitida (mantener plano, editorial).
- `break-inside: avoid` entre imagen y epígrafe, para que nunca queden separados por un salto de página.
- Las imágenes no llevan marco decorativo ni fondo de color.

## 8. Tablas

- Encabezado con fondo `azul-institucional`, texto blanco, `Source Sans 3` 600.
- Filas alternadas con `fondo-bloque` al 50 % para lectura horizontal.
- Bordes horizontales únicamente en `gris-linea` (sin bordes verticales), estilo *quiet table* propio de editoriales académicas.

## 9. Maquetación de página (PDF / WeasyPrint)

```
@page {
  size: A4;
  margin-top: 30mm;
  margin-bottom: 25mm;
  margin-left: 25mm;
  margin-right: 25mm;
}
```

- **Portada**: página independiente, sin encabezado ni pie, fondo blanco con filete superior e inferior en `oro-academico` (1.5 mm), escudo/nombre de la institución centrado, título en Libre Baskerville 34 pt, metadatos (docente, alumno, legajo, fecha) en `Source Sans 3` 10 pt.
- **Encabezado** (desde la primera página de contenido): nombre de la materia en versalitas pequeñas, alineado a la izquierda; número de sección actual alineado a la derecha. Línea `gris-linea` de 0.5 pt debajo.
- **Pie de página**: `UTN Facultad Regional Córdoba — Informática Industrial` a la izquierda, número de página a la derecha, `Source Sans 3` 8.5 pt en `grafito` al 70 %.
- **Interlineado de página**: caja de texto con `orphans: 3; widows: 3;` para evitar líneas sueltas al saltar de página.

## 10. Tokens de diseño (referencia rápida para `build_pdf.py`)

```yaml
color:
  azul_institucional: "#1B3A6B"
  grafito: "#2E3440"
  oro_academico: "#B8912F"
  gris_linea: "#D7DBE0"
  fondo_pagina: "#FFFFFF"
  fondo_bloque: "#F5F6F8"
  info: "#2B6CB0"
  exito: "#2F855A"
  advertencia: "#B7791F"
  problema: "#C53030"

tipografia:
  portada_h1: "Libre Baskerville, Georgia, serif"
  h2_h4: "Source Sans 3, Segoe UI, Arial, sans-serif"
  cuerpo: "Source Serif 4, Georgia, serif"
  codigo: "JetBrains Mono, Courier New, monospace"
  epigrafe: "Source Sans 3, Segoe UI, Arial, sans-serif"

escala_pt:
  portada: 34
  h1: 20
  h2: 15
  h3: 12.5
  cuerpo: 11.5
  codigo: 10
  epigrafe: 9.5
  pie_pagina: 9

pagina:
  tamano: A4
  margen_superior_mm: 30
  margen_inferior_mm: 25
  margen_lateral_mm: 25

vinetas:
  nivel_1: "▪"
  nivel_2: "–"
  nivel_3: "○"
```

---

## Referencia de inspiración

Se tomó como referencia de formato la filosofía de sistemas de diseño en Markdown de [designmd.ai](https://designmd.ai/) — un archivo único, legible tanto por personas como por herramientas de generación automática (el script de este proyecto), que define tokens de diseño de forma explícita y parseable en vez de dejarlos implícitos en el código. La paleta y tipografía en sí son de elaboración propia para este informe, orientadas a una línea editorial académica (el sitio de referencia está enfocado en sistemas de diseño de producto/SaaS, no en publicaciones académicas).
