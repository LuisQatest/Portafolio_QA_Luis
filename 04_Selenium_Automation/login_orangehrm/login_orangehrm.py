from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
import time
import os

# Ruta al chromedriver
chrome_driver_path = r"C:\Users\Luis\Desktop\HERRAMIENTAS QA TESTING\chromedriver.exe"

# Configurar el servicio de Chrome
service = Service(executable_path=chrome_driver_path)
driver = webdriver.Chrome(service=service)

# Acceder a OrangeHRM demo
driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
driver.maximize_window()
time.sleep(2)

# Completar login
driver.find_element(By.NAME, "username").send_keys("Admin")
driver.find_element(By.NAME, "password").send_keys("admin123")
driver.find_element(By.CLASS_NAME, "orangehrm-login-button").click()
time.sleep(5)

# Capturar evidencia
evidencia_path = r"C:\Users\Luis\Desktop\PROYECTO_GITHUB\04_Selenium_Automation\login_orangehrm\evidencia_login_orangehrm.png"
driver.save_screenshot(evidencia_path)

print(f"Evidencia guardada en: {evidencia_path}")

# Cerrar navegador
driver.quit()
