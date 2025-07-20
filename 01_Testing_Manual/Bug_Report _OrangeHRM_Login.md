# Bug Report - OrangeHRM Login

##  ID del Bug
TC02-BUG-LOGIN

##  Fecha
2025-07-20

##  Caso de prueba relacionado
**TC02 - Login con credenciales inválidas**

##  Descripción
Al ingresar un usuario inválido con una contraseña correcta, el sistema deberia mostrar un  mensaje de error “Invalid credentials”
##  Pasos para reproducir

1. Navegar a: https://opensource-demo.orangehrmlive.com/web/index.php/auth/login/
2. Ingresar usuario: `admin311`
3. Ingresar la contraseña: `admin123`
4. Hacer clic en el botón **Login**

##  Resultado esperado
El sistema debería mostrar el mensaje de error y limpiar el campo de usuario por seguridad.

##  Resultado obtenido
El sistema no muestra el mensaje: `Invalid credentials`
##  Evidencia
se deja ScreenShot

## Entorno de prueba

- Navegador: Google Chrome v114
- Sistema Operativo: Windows 10
- URL: https://opensource-demo.orangehrmlive.com/

##  Severidad
**Media** – Puede generar desconfianza o fallos en usuarios reales.

##  Estado
Reportado (simulado en Jira)

---

 Reportado por: Luis Martínez  
 Proyecto: Portafolio QA Manual
