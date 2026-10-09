import pytest
from selenium.webdriver.chrome.webdriver import WebDriver
from pages.base_page import BasePage
from pages.login_page import LoginPage
from pages.inventory_page import InventoryPage

@pytest.fixture(autouse=True)
def setup_login(driver: WebDriver):
        """Fixture de inicio de sesión."""
        login_page = LoginPage(driver)
        login_page.navigate()
        login_page.login("standard_user", "secret_sauce")

def test_verify_inventory_header_title(driver: WebDriver):
        """ encabezado 'Products'."""
        inventory_page = InventoryPage(driver)
        
        actual_title = inventory_page.get_header_title()
        
        assert actual_title == "Products", f"Se esperaba 'Products' pero se obtuvo '{actual_title}'"

def test_verify_inventory_browser_tab_title(driver: WebDriver):
        """Verifica título de la pestaña 'Swag Labs'."""
        inventory_page = InventoryPage(driver)
        
        actual_browser_title = inventory_page.get_browser_title()
        
        assert actual_browser_title == "Swag Labs", f"Se esperaba 'Swag Labs' pero se obtuvo '{actual_browser_title}'"

def test_verify_product(driver: WebDriver):
        """Comprueba que exista al menos un producto."""
        inventory_page = InventoryPage(driver)
        
        count = inventory_page.get_inventory_items_count()
        
        # Verifica que exista un producto
        assert count > 0, f"Se esperaban productos visibles, pero se encontraron {count}"

def test_verify_specific_product(driver: WebDriver):
        """Comprueba la presencia de producto por nombre."""
        inventory_page = InventoryPage(driver)
        
        product_names = inventory_page.get_all_product_names()
        expected_product = "Sauce Labs Backpack"
        
        # Validar que el producto esperado esté dentro de la lista de nombres
        assert expected_product in product_names, f"El producto '{expected_product}' no se encuentra visible en la lista"

def test_verify_ui_elements_presence(driver: WebDriver):
        """Verifica que los elementos principales de la UI (menú, logo, carrito y filtro) estén presentes."""
        inventory_page = InventoryPage(driver)

        # Validaciones de visibilidad de componentes clave de la interfaz
        assert inventory_page.is_menu_button_displayed(), "El botón del menú principal no está visible"
        assert inventory_page.is_app_logo_displayed(), "El logo de la aplicación no está visible"
        assert inventory_page.is_shopping_cart_displayed(), "El icono del carrito de compras no está visible"
        assert inventory_page.is_sort_container_displayed(), "El filtro de ordenamiento de productos no está visible"
        