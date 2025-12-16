from playwright.sync_api import sync_playwright
import os

def before_all(context):
    """Set up Playwright before all tests."""
    context.playwright = sync_playwright().start()
    context.browser = context.playwright.chromium.launch(headless=False)  # Change to True for headless execution

def before_scenario(context, scenario):
    """Set up a new browser page before each scenario."""
    context.page = context.browser.new_page()


def after_all(context):
    """Close the browser and stop Playwright after all tests."""
    if hasattr(context, 'browser'):
        context.browser.close()
    if hasattr(context, 'playwright'):
        context.playwright.stop()
