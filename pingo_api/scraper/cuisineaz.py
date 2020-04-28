import re
from scraper.base import RecetteBase

class RecetteCuisineAZ(RecetteBase):

    def __init__(self, url):
        super().__init__(url)
        
    def _get_name(self):
        self.name = self.soup.find("article", { "class": "recipe_main" }).find("header").text.strip()

    def _get_ingredients(self):
        ingredients = self.soup.find("section", { "class": "recipe_ingredients" }).findAll("li")

        for ingredient in ingredients:
            self.ingredients.append(ingredient.text.strip())

    def _get_directions(self):
        directions = self.soup.find("div", { "id": "preparation" }).findAll("p", { "class": "p10"})

        for direction in directions:
            self.directions.append(direction.span.next_sibling)
    
    def _get_servings(self):
        servings = self.soup.find("span", { "id": "ContentPlaceHolder_LblRecetteNombre" }).text
        self.servings = re.sub("[^0-9]", "", servings)