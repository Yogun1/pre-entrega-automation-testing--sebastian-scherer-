import pytest
from selenium.webdriver.common.by import By
from pages.login_page import LoginPage
from pages.inventory_page import InventoryPage


def test_successful_login(driver):
        login_page = LoginPage(driver)
        inventory_page = InventoryPage(driver)

        login_page.navigate()
        login_page.login("standard_user", "secret_sauce")

        assert inventory_page.get_title() == "Products"

        print("Login correcto, estas en el inventario.")

@pytest.mark.parametrize(
        "username, password, expected_error",
        [
            ("locked_out_user", "secret_sauce", "Epic sadface: Sorry, this user has been locked out."),
            ("invalid_user", "invalid_pass", "Epic sadface: Username and password do not match any user in this service"),
            ("", "", "Epic sadface: Username is required"),
            ("standard_user", "", "Epic sadface: Password is required"),
        ]
    )
def test_invalid_login(driver, username, password, expected_error):
        login_page = LoginPage(driver)
        
        login_page.navigate()
        login_page.login(username, password)

        assert login_page.get_error_message() == expected_error

'''
Aca estaba intentando hacer un test para el problem_user, pero no supe como identificar la ventana de alerta de js desde selenium. Se que se puede hacer con un alert pero nose como identificarlo y pasarlo por un assert despues.
def test_problem_user(driver, username, password):
        login_page = LoginPage(driver)
        
        login_page.navigate()
        login_page.login(username, password)
        driver.switch_to.alert.accept
'''        



        