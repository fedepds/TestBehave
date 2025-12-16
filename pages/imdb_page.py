from pages.base_page import BasePage
from playwright.sync_api import Page, Locator
from typing import Callable

class ImdbPage(BasePage):
    def __init__(self, page):
        super().__init__(page)
        self.search_input = page.locator("input[id='suggestion-search']")
        self.search_button = page.locator("button[id='suggestion-search-button']")

        # Mapeo de nombres de campos a funciones que retornan localizadores
        self.field_names_mapping = {
            "search_input": lambda page: page.locator("input[id='suggestion-search']"),
            "search_button": lambda page: page.locator("button[id='suggestion-search-button']"),
            "first_movie_list": lambda page: page.locator('//*[@id="__next"]/main/div[2]/div[2]/section/div/div[1]/section[2]/div[2]/ul/li[1]/div/div/div/div/div[2]/div[1]/a/h3'),
            "director": lambda page: page.locator('//*[@id="__next"]/main/div/section[1]/section/div[3]/section/section/div[3]/div[2]/div[2]/div[2]/ul/li[1]/div/ul/li/a'),
            "rating": lambda page: page.locator('//*[@id="__next"]/main/div/section[1]/section/div[3]/section/section/div[3]/div[2]/div[2]/div[1]/div/div[1]/a/span/div/div[2]/div[1]/span[1]'),
        }

    def get_field_by_enum(self, valor: str) -> Callable[[Page], Locator]:
        locator = self.field_names_mapping.get(valor)
        if not locator:
            raise ValueError(f"Nombre de campo no válido: {valor}")
        return locator

    def search_movie(self, movie_name):
        self.search_input.fill(movie_name)
        self.search_button.click()
