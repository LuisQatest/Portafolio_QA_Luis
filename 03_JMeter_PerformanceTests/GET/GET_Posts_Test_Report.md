# Prueba de Rendimiento - Método GET con JMeter

## Descripción
Se realizó una prueba de rendimiento usando Apache JMeter para el endpoint `GET /posts` de la API pública JSONPlaceholder.

##  Configuración de la prueba

- Herramienta: Apache JMeter 5.6
- Endpoint: `https://jsonplaceholder.typicode.com/posts`
- Método: GET
- Threads (Usuarios): 5
- Loop Count: 3

## Resultado

Todas las peticiones respondieron con código 200 OK.

## Evidencia

![Evidencia](./evidencia_GET_Posts_JMeter.png)
