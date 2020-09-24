<<<<<<< HEAD
import re

from ._base import RecetteBase
from .recette import register

__all__ = [
    "Recette750g",
]


class Recette750g(RecetteBase):
    def __init__(self, url):
        super().__init__(url)

    def _get_name(self, soup):
        self._name = soup.find("span", {"class": "recipe-title"}).text.strip()

    def _get_ingredients(self, soup):
        self._ingredients = []

        ingredients = soup.findAll("span", {"class": "recipe-ingredients-item-label"})

        for ingredient in ingredients:
            if ingredient.span:
                self._ingredients.append(ingredient.span.previous_sibling.strip())
            else:
                self._ingredients.append(ingredient.text)

    def _get_directions(self, soup):
        directions = soup.findAll("div", {"class": "recipe-steps-text"})
        self._directions = [direction.text for direction in directions]

    def _get_servings(self, soup):
        if soup.find("span", {"class": "ingredient-variator-label"}):
            servings = soup.find("span", {"class": "ingredient-variator-label"}).text
        else:
            servings = soup.find("h2", {"class": "u-title-section"}).text

        self._servings = re.sub("[^0-9]", "", servings)


register("www.750g.com", Recette750g)
=======
import re

from ._base import RecetteBase
from .recette import register

__all__ = [
    "Recette750g",
]


class Recette750g(RecetteBase):
    def __init__(self, url):
        super().__init__(url)

    def _get_name(self, soup):
        self._name = soup.find("span", {"class": "recipe-title"}).text.strip()

    def _get_ingredients(self, soup):
        self._ingredients = []

        ingredients = soup.findAll("span", {"class": "recipe-ingredients-item-label"})

        for ingredient in ingredients:
            if ingredient.span:
                self._ingredients.append(ingredient.span.previous_sibling.strip())
            else:
                self._ingredients.append(ingredient.text)

    def _get_directions(self, soup):
        directions = soup.findAll("div", {"class": "recipe-steps-text"})
        self._directions = [direction.text for direction in directions]

    def _get_servings(self, soup):
        if soup.find("span", {"class": "ingredient-variator-label"}):
            servings = soup.find("span", {"class": "ingredient-variator-label"}).text
        else:
            servings = soup.find("h2", {"class": "u-title-section"}).text

        self._servings = re.sub("[^0-9]", "", servings)


register("www.750g.com", Recette750g)
>>>>>>> bea9df1ba0d4b8f7ce7c5112dd96b70cb303902c
