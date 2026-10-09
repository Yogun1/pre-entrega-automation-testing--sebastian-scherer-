import pytest
from conftest import driver
from pages.login_page import LoginPage
from pages.inventory_page import InventoryPage



@pytest.fixture(autouse=True)
def setup_login(driver):
        """Fixture inicio de sesión."""
        login_page = LoginPage(driver)
        login_page.navigate()
        login_page.login("standard_user", "secret_sauce")

def test_add_single_product_to_cart(driver):
        """Verifica que al hacer click el contador aumente a 1 y cambie a 'Remove'."""
        inventory_page = InventoryPage(driver)

        # click en 'Add to cart'
        inventory_page.add_backpack_to_cart()

        # contador carrito + '1'
        cart_count = inventory_page.get_cart_badge_count()
        assert cart_count == "1", f"Se esperaba '1' en el carrito, pero se obtuvo '{cart_count}'"

        # botón cambia a 'Remove'
        assert inventory_page.is_remove_button_displayed(), "El botón 'Remove' no se encuentra visible tras agregar el producto"