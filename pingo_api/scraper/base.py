import requests
from abc import ABC, abstractmethod
from bs4 import BeautifulSoup

class RecetteBase(ABC):

    def __init__(self, url):
        self.name = ""
        self.servings = 0
        self.ingredients = []
        self.directions = []
        self.url = url
        self.soup = self._get_html()
        self._get_recipe()
        del self.soup

    def _get_html(self):
        response = requests.get(self.url)
        return BeautifulSoup(response.text, "html.parser")

    @abstractmethod
    def _get_name(self):
        pass

    @abstractmethod
    def _get_servings(self):
        pass

    @abstractmethod
    def _get_ingredients(self):
        pass

    @abstractmethod
    def _get_directions(self):
        pass 

    def _get_recipe(self):
        self._get_name()
        self._get_servings()
        self._get_ingredients()
        self._get_directions()
