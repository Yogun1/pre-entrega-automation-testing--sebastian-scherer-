import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service #importa el servicio de chrome
from webdriver_manager.chrome import ChromeDriverManager

@pytest.fixture
def driver():
    # Inicialización del driver
    options = webdriver.ChromeOptions() # opciones de config del navegador
    options.add_argument("--start-maximized")
    # options.add_argument("--headless")  # Descomentar para ejecutar sin interfaz gráfica
    
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
    yield driver # es como el return, pero permite ejecutar codigo despues
    
    # Teardown
    driver.quit()