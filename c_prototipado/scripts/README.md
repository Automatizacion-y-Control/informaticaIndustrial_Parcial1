# 🐍 scripts

Script que genera el PDF final del informe (`informeParcial1_infoInd.pdf`) a partir de `../informeParcial1_infoInd.md`, `../assets/` y la editorial definida en `a_requisitos/diseño.md`. El PDF resultante se aloja en `d_presentacion/`.

## Uso

```bash
pip install -r requirements.txt
playwright install chromium      # una sola vez, descarga el navegador headless

python build_pdf.py              # genera d_presentacion/informeParcial1_infoInd.pdf
python build_pdf.py --proof 4    # además exporta PNG de control de las primeras 4 páginas
                                  # (+ la última) a scripts/qa/ — requiere poppler instalado
```

Al finalizar imprime un **reporte de consistencia** en la terminal: cantidad de figuras insertadas, imágenes referenciadas en el `.md` que no existen en `assets/`, archivos de `assets/` sin usar, callouts detectados y qué fuentes reales se embebieron.

## Fuentes reales (opcional)

Por defecto el script usa equivalentes ya instalados en el sistema (GFS Baskerville, DejaVu Serif/Sans/Mono, Liberation) para no depender de internet. Si querés usar las fuentes exactas definidas en `diseño.md` (Libre Baskerville, Source Serif 4, Source Sans 3, JetBrains Mono), descargá los `.ttf` de Google Fonts / JetBrains y colocalos acá con estos nombres exactos:

```
fonts/LibreBaskerville-Regular.ttf
fonts/LibreBaskerville-Bold.ttf
fonts/LibreBaskerville-Italic.ttf
fonts/SourceSerif4-Regular.ttf
fonts/SourceSerif4-Italic.ttf
fonts/SourceSerif4-Bold.ttf
fonts/SourceSans3-Regular.ttf
fonts/SourceSans3-SemiBold.ttf
fonts/SourceSans3-Italic.ttf
fonts/JetBrainsMono-Regular.ttf
fonts/JetBrainsMono-Bold.ttf
```

El script las detecta automáticamente en la próxima corrida (no hay que tocar el código).

## Convención de bloques especiales

Para que un párrafo se renderice como callout (nota/verificación/advertencia/problema encontrado, sección 6 de `diseño.md`), escribirlo como cita Markdown con la etiqueta en negrita al inicio:

```markdown
> **PROBLEMA ENCONTRADO:** el host no recibía respuesta ICMP desde la VM...
```

Etiquetas reconocidas: `NOTA`, `VERIFICACIÓN`, `A TENER EN CUENTA`, `PROBLEMA ENCONTRADO`.
