# 🧩 c_prototipado

Informe de soporte del Parcial N° 1 de Informática Industrial (Lic. en Automatización y Control, UTN FRC): infraestructura industrial completa, de servidores virtuales en VMware a una base de datos administrada en AWS, documentada paso a paso con evidencias, más el script que compila esa documentación a PDF.

## Contenido

| Elemento | Descripción |
|---|---|
| [`informeParcial1_infoInd.md`](informeParcial1_infoInd.md) | Informe completo del parcial: carátula (universidad, carrera, integrantes con legajo, docente), índice, introducción, los tres bloques de resolución (virtualización local con TP1 Windows Server y TP2 Ubuntu Server, migración a AWS y ciberseguridad, implementación en Amazon RDS) y conclusiones. Es la fuente única de verdad del informe. |
| [`assets/`](assets/) | 55 capturas de pantalla normalizadas y numeradas, referenciadas desde el informe (VMware Workstation, instalación de Windows Server y Ubuntu Server, configuración de red e IIS, snapshots, consola de AWS, Security Group, instancia RDS y conexión desde SSMS). |
| [`scripts/`](scripts/) | `build_pdf.py`: genera el PDF final del informe a partir de `informeParcial1_infoInd.md` + `assets/`, aplicando un archivo de estilo editorial (`diseño.md`: tipografías, colores, jerarquía de títulos, viñetas y maquetación de página). Incluye `requirements.txt` y su propio `README.md` con instrucciones de uso. |

## Flujo de generación del informe

```
informeParcial1_infoInd.md   ─┐
assets/*.png                  ├──▶  scripts/build_pdf.py  ──▶  informeParcial1_infoInd.pdf
diseño.md (estilo)            ─┘
```

El script reporta en consola, en cada corrida, un control de consistencia: figuras insertadas, imágenes referenciadas que no existen en `assets/`, archivos de `assets/` sin usar y qué fuentes de diseño pudo aplicar.
