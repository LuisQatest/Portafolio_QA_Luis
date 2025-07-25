# Automatización con Selenium - Formulario DemoQA

Este script automatiza la interacción con un formulario web en el sitio [DemoQA](https://demoqa.com/text-box), utilizando **Selenium con Python**.

## ¿Qué hace el script?

1. Abre el navegador y navega a `https://demoqa.com/text-box`
2. Completa automáticamente los campos del formulario:
   - Nombre completo
   - Email
   - Dirección actual
   - Dirección permanente
3. Hace clic en el botón "Submit"
4. Toma una captura de pantalla como evidencia (`evidencia_formulario_demoqa.png`)
5. Cierra el navegador

## Tecnologías utilizadas

- Python 3
- Selenium WebDriver
- ChromeDriver

## Archivos incluidos

- `formulario_demoqa.py` → Script principal
- `evidencia_formulario_demoqa.png` → Imagen generada automáticamente con los resultados

## Requisitos para ejecutarlo

- Tener instalado Python y Selenium (`pip install selenium`)
- Tener el archivo `chromedriver.exe` en una ruta válida
- Reemplazar la línea del script con la ruta local correspondiente:
  ```python
  driver_path = r"C:\RUTA\A\chromedriver.exe"
