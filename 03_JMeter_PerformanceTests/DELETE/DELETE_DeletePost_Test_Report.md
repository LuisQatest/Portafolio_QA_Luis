# Prueba de Rendimiento - Método DELETE con JMeter

## Descripción
Prueba para eliminar un recurso existente utilizando el endpoint `DELETE /posts/1` de JSONPlaceholder.

## Configuración de la prueba

- Herramienta: Apache JMeter 5.6
- Endpoint: `https://jsonplaceholder.typicode.com/posts/1`
- Método: DELETE
- Headers: Ninguno requerido
- Body: No aplica
- Usuarios: 3
- Iteraciones por usuario: 2

## Resultado

La API respondió con código **200 OK**, simulando la eliminación correcta del recurso.

## Evidencia

![Evidencia](./evidencia_DELETE_DeletePost_JMeter.png)
