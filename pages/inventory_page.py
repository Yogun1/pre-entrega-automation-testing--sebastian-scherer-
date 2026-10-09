from selenium.webdriver.common.by import By
from pages.base_page import BasePage

class InventoryPage(BasePage):
    # Locators
    TITLE = (By.CLASS_NAME, "title")
    ADD_TO_CART_BACKPACK = (By.ID, "add-to-cart-sauce-labs-backpack")
    CART_BADGE = (By.CLASS_NAME, "shopping_cart_badge")
    INVENTORY_ITEMS = (By.CLASS_NAME, "inventory_item")
    INVENTORY_ITEM_NAME = (By.CLASS_NAME, "inventory_item_name")

    # UI Elements Locators
    MENU_BUTTON = (By.ID, "react-burger-menu-btn")
    APP_LOGO = (By.CLASS_NAME, "app_logo")
    SHOPPING_CART_LINK = (By.CLASS_NAME, "shopping_cart_link")
    PRODUCT_SORT_CONTAINER = (By.CLASS_NAME, "product_sort_container")

    # Add to cart & Badge Locators
    ADD_TO_CART_BACKPACK = (By.ID, "add-to-cart-sauce-labs-backpack")
    REMOVE_BACKPACK = (By.ID, "remove-sauce-labs-backpack")
    CART_BADGE = (By.CLASS_NAME, "shopping_cart_badge")

    def get_title(self):
        """ título del inventario."""
        return self.get_text(self.TITLE)

    def get_page_title(self):
        """obtiene el título principal."""
        return self.get_title()

    def add_backpack_to_cart(self):
        """click en 'Add to cart' de la mochila."""
        self.click(self.ADD_TO_CART_BACKPACK)

    def get_cart_badge_count(self):
        """Retorna el número en el carrito."""
        return self.get_text(self.CART_BADGE)

    def is_remove_button_displayed(self):
        """Verifica que el botón cambie a 'Remove'."""
        return self.find_element(self.REMOVE_BACKPACK).is_displayed()

    def get_cart_badge_text(self):
        return self.get_text(self.CART_BADGE)

    def get_header_title(self):
        """ verifica encabezado 'Products' en la página."""
        return self.get_page_title()

    def get_browser_title(self):
        """ Da el título de la pestaña."""
        title = self.driver.title
        return title.strip() if title else ""

    def get_inventory_items_count(self):
        """para contar cuántas tarjetas de producto con la clase .inventory_item hay."""
        self.find_element(self.INVENTORY_ITEMS)
        items = self.driver.find_elements(*self.INVENTORY_ITEMS)
        return len(items)

    def get_all_product_names(self):
        """retorna la lista de productos."""
        self.find_element(self.INVENTORY_ITEM_NAME)
        elements = self.driver.find_elements(*self.INVENTORY_ITEM_NAME)
        return [element.text for element in elements]

    def is_menu_button_displayed(self):
        """Comprueba si el botón del menú hamburguesa está visible."""
        return self.find_element(self.MENU_BUTTON).is_displayed()

    def is_app_logo_displayed(self):
        """Comprueba si el logo de la aplicación ('Swag Labs') está visible."""
        return self.find_element(self.APP_LOGO).is_displayed()

    def is_shopping_cart_displayed(self):
        """Comprueba si el ícono del carrito de compras está visible."""
        return self.find_element(self.SHOPPING_CART_LINK).is_displayed()

    def is_sort_container_displayed(self):
        """Comprueba si el filtro/desplegable de ordenamiento está visible."""
        return self.find_element(self.PRODUCT_SORT_CONTAINER).is_displayed()