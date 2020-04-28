import re

from ._base import RecetteBase

__all__ = [
    "RecetteCuisineAZ",
]


class RecetteCuisineAZ(RecetteBase):

    def __init__(self, url):
        super().__init__(url)
        
    def _get_name(self, soup):
        self._name = soup.find("article", { "class": "recipe_main" }).find("header").text.strip()

    def _get_ingredients(self, soup):
        ingredients = soup.find("section", { "class": "recipe_ingredients" }).findAll("li")
        self._ingredients = [ingredient.text.strip() for ingredient in ingredients]

    def _get_directions(self, soup):
        directions = soup.find("div", { "id": "preparation" }).findAll("p", { "class": "p10"})
        self._directions = [direction.span.next_sibling for direction in directions]
    
    def _get_servings(self, soup):
        servings = soup.find("span", { "id": "ContentPlaceHolder_LblRecetteNombre" }).text
        self._servings = re.sub("[^0-9]", "", servings)
