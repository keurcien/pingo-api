import re

from ._base import RecetteBase

__all__ = [
    "RecetteMarmiton"
]


class RecetteMarmiton(RecetteBase):
    
    def __init__(self, url):
        super().__init__(url)

    def _get_name(self, soup):
        self._name = soup.find("h1", { "class": "main-title" }).text

    def _get_servings(self, soup):
        self._servings = soup.find("span", { "class": "recipe-infos__quantity__value" }).text

    def _get_ingredients(self, soup):
        self._ingredients = []

        ingredients = soup.findAll("li", { "class": "recipe-ingredients__list__item" })
        for ingredient in ingredients:
            name = ingredient.find("span", { "class": "ingredient" }).text.strip()
            quantity = ingredient.find("span", { "class": "recipe-ingredient-qt" }).text.strip()
            complement = ingredient.find("span", { "class": "recipe-ingredient__complement" }).text.strip()
            
            if quantity and complement:
                self._ingredients.append(f"{quantity} {name} {complement}")
            elif quantity:
                self._ingredients.append(f"{quantity} {name}")
            else:
                self._ingredients.append(name)

    def _get_directions(self, soup):
        directions = soup.findAll("li", { "class": "recipe-preparation__list__item" })
        self._directions = [direction.text.strip() for direction in directions]
