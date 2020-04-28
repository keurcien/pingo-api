from abc import ABC, abstractmethod

import requests
from bs4 import BeautifulSoup

__all__ = [
    "RecetteBase",
]


class RecetteBase(ABC):
    def __init__(self, url):
        response = requests.get(url)
        soup = BeautifulSoup(response.text, "html.parser")

        self._url = url
        self._get_name(soup)
        self._get_servings(soup)
        self._get_ingredients(soup)
        self._get_directions(soup)

    @abstractmethod
    def _get_name(self, soup):
        raise NotImplementedError()

    @abstractmethod
    def _get_servings(self, soup):
        raise NotImplementedError()

    @abstractmethod
    def _get_ingredients(self, soup):
        raise NotImplementedError()

    @abstractmethod
    def _get_directions(self, soup):
        raise NotImplementedError()

    @property
    def url(self):
        return self._url

    @url.setter
    def url(self, value):
        self._url = value

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        self._name = value

    @property
    def servings(self):
        return self._servings

    @servings.setter
    def servings(self, value):
        self._servings = value

    @property
    def ingredients(self):
        return self._ingredients

    @ingredients.setter
    def ingredients(self, value):
        self._ingredients = value

    @property
    def directions(self):
        return self._directions

    @directions.setter
    def directions(self, value):
        self._directions = value
