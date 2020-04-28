import re
from scraper.base import RecetteBase

class Recette750g(RecetteBase):

    def __init__(self, url):
        super().__init__(url)

    def _get_name(self):
        self.name = self.soup.find("span", { "class": "u-title-page" }).text

    def _get_ingredients(self):
        ingredients = self.soup.find("ul", { "class": "c-recipe-ingredients__list" }).findAll("li")

        for ingredient in ingredients:
            if ingredient.span:
                self.ingredients.append(ingredient.span.previous_sibling.strip())
            else:
                self.ingredients.append(ingredient.text)

    def _get_directions(self):
        directions = self.soup.findAll("div", { "class": "c-recipe-steps__item-content" })

        for direction in directions:
            self.directions.append(direction.text)

    
    def _get_servings(self):
        if self.soup.find("span", { "class": "c-ingredient-variator-label" }):
            servings = self.soup.find("span", { "class": "c-ingredient-variator-label" }).text
        else:
            servings = self.soup.find("h2", { "class": "u-title-section" }).text
        
        self.servings = re.sub("[^0-9]", "", servings)