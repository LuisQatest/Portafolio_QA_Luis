# Prueba de Rendimiento - Método POST con JMeter

## Descripción
Se ejecutó una prueba de carga para el endpoint `POST /posts` de JSONPlaceholder, simulando la creación de nuevos recursos.

## Configuración de la prueba

- Herramienta: Apache JMeter 5.6
- Endpoint: `https://jsonplaceholder.typicode.com/posts`
- Método: POST
- Headers: Content-Type: application/json
- Body:
  ```json
  {
    "title": "Luis QA Test",
    "body": "Este es un post de prueba para el portafolio QA",
    "userId": 101
  }
