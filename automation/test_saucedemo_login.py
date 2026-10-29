"""
====================================================================
QA AUTOMATION TEST - SAUCEDEMO LOGIN & CATALOG VERIFICATION
====================================================================
Framework: Selenium WebDriver + Python
Target: https://www.saucedemo.com
Description: Automates end-to-end login flow and validates UI elements.
====================================================================
"""

import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager


def run_automation_test():
    # 1. Configuración del navegador (Chrome)
    print("[INFO] Iniciando el navegador Chrome...")
    options = webdriver.ChromeOptions()
    options.add_argument("--headless")  # Ejecución en modo headless (sin interfaz gráfica)
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")

    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
    driver.implicitly_wait(10)  # Espera implícita de hasta 10 segundos

    try:
        # 2. Navegar a la página de prueba
        url = "https://www.saucedemo.com"
        print(f"[INFO] Navegando a {url}...")
        driver.get(url)

        # 3. Localizar elementos del formulario e ingresar credenciales
        print("[INFO] Introduciendo credenciales de acceso...")
        username_input = driver.find_element(By.ID, "user-name")
        password_input = driver.find_element(By.ID, "password")
        login_button = driver.find_element(By.ID, "login-button")

        username_input.send_keys("standard_user")
        password_input.send_keys("secret_sauce")

        # 4. Hacer clic en el botón de Login
        login_button.click()
        time.sleep(2)

        # 5. Aserciones y validaciones (Asserts)
        current_url = driver.current_url
        print(f"[INFO] URL actual tras login: {current_url}")

        # Validación 1: Verificar que fuimos redirigidos a la página del catálogo
        assert "inventory.html" in current_url, "[FAIL] Redirección fallida tras login"

        # Validación 2: Verificar que el título del catálogo está visible
        title_element = driver.find_element(By.CLASS_NAME, "title")
        assert title_element.text == "Products", "[FAIL] El título del catálogo no coincide"

        # Validación 3: Verificar que hay productos cargados en el DOM
        inventory_items = driver.find_elements(By.CLASS_NAME, "inventory_item")
        assert len(inventory_items) > 0, "[FAIL] No se encontraron productos en el catálogo"

        print(f"[SUCCESS] Test de Automatización Exitoso! Productos encontrados: {len(inventory_items)}")

    except AssertionError as error:
        print(f"[ERROR] Fallo en la aserción: {error}")
    except Exception as ex:
        print(f"[ERROR] Ocurrió una excepción durante la ejecución: {ex}")
    finally:
        # 6. Cerrar sesión del navegador
        print("[INFO] Cerrando sesión del navegador...")
        driver.quit()


if __name__ == "__main__":
    run_automation_test()
