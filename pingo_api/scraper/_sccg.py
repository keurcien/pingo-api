import re

from ._base import RecetteBase

__all__ = [
    "Recette750g",
]


class Recette750g(RecetteBase):

    def __init__(self, url):
        super().__init__(url)

    def _get_name(self, soup):
        self._name = soup.find("span", { "class": "u-title-page" }).text

    def _get_ingredients(self, soup):
        self._ingredients = []

        ingredients = soup.find("ul", { "class": "c-recipe-ingredients__list" }).findAll("li")
        for ingredient in ingredients:
            if ingredient.span:
                self._ingredients.append(ingredient.span.previous_sibling.strip())
            else:
                self._ingredients.append(ingredient.text)

    def _get_directions(self, soup):
        directions = soup.findAll("div", { "class": "c-recipe-steps__item-content" })
        self._directions = [direction.text for direction in directions]
    
    def _get_servings(self, soup):
        if soup.find("span", { "class": "c-ingredient-variator-label" }):
            servings = soup.find("span", { "class": "c-ingredient-variator-label" }).text
        else:
            servings = soup.find("h2", { "class": "u-title-section" }).text
        
        self._servings = re.sub("[^0-9]", "", servings)
