from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
import time

# Configuración del driver
driver_path = rdriver_path = r"C:\Users\Luis\Desktop\HERRAMIENTAS QA TESTING\chromedriver.exe"
service = Service(executable_path=driver_path)
driver = webdriver.Chrome(service=service)

# Paso 1: Abrir la página
driver.get("https://demoqa.com/text-box")
driver.maximize_window()

# Paso 2: Completar el formulario
driver.find_element(By.ID, "userName").send_keys("Luis Martinez")
driver.find_element(By.ID, "userEmail").send_keys("luis.martinez@email.com")
driver.find_element(By.ID, "currentAddress").send_keys("Av. Abundancia 742, CABA")
driver.find_element(By.ID, "permanentAddress").send_keys("Av. Abundancia 742, Buenos Aires")

# Paso 3: Hacer clic en el botón de enviar
driver.find_element(By.ID, "submit").click()

# Paso 4: Guardar evidencia
driver.save_screenshot("evidencia_formulario_demoqa.png")

# Pausa para ver el resultado
time.sleep(3)

# Cerrar navegador
driver.quit()

# Mantener la ventana de consola abierta (opcional para debug)
input("Presioná Enter para cerrar...")
