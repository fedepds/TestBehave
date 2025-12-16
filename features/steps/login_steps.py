from behave import given, when, then
from pages.login_page import LoginPage
from pages.inventory_page import InventoryPage


@given("the user is on the SauceDemo login page")
def step_impl(context):
    # El navegador y la página ya están creados por environment.py
    context.login_page = LoginPage(context.page)
    context.login_page.go_to("https://www.saucedemo.com/")
    context.login_page.take_screenshot("login_page")

@when("they enter valid credentials")
def step_impl(context):
    context.login_page.login("standard_user", "secret_sauce")
    context.login_page.take_screenshot("after_login")

@then("they should be redirected to the inventory page")
def step_impl(context):
    context.inventory_page = InventoryPage(context.page)
    assert "inventory" in context.page.url
    context.inventory_page.take_screenshot("inventory_page")
