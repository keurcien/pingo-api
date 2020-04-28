import re
from scraper.base import RecetteBase

class RecetteMarmiton(RecetteBase):
    
    def __init__(self, url):
        super().__init__(url)
        
    def _get_name(self):
        self.name = self.soup.find("h1", { "class": "main-title" }).text

    def _get_servings(self):
        self.servings = self.soup.find("span", { "class": "recipe-infos__quantity__value" }).text

    def _get_ingredients(self):

        ingredients = self.soup.findAll("li", { "class": "recipe-ingredients__list__item" })
        
        for ingredient in ingredients:

            name = ingredient.find("span", { "class": "ingredient" }).text.strip()
            quantity = ingredient.find("span", { "class": "recipe-ingredient-qt" }).text.strip()
            complement = ingredient.find("span", { "class": "recipe-ingredient__complement" }).text.strip()
            
            if quantity and complement:
                self.ingredients.append(f"{quantity} {name} {complement}")
            elif quantity:
                self.ingredients.append(f"{quantity} {name}")
            else:
                self.ingredients.append(name)

    def _get_directions(self):
        directions = self.soup.findAll("li", { "class": "recipe-preparation__list__item" })
        for direction in directions:
            self.directions.append(direction.text.strip())
