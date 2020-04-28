import re
from scraper.base import RecetteBase

class RecetteJournalDesFemmes(RecetteBase):

    def __init__(self, url):
        super().__init__(url)
        
    def _get_name(self):
        self.name = self.soup.find("h1", { "class": "app_recipe_title_page" }).text

    def _get_ingredients(self):

        if self.soup.find("ul", { "class": "bu_cuisine_ingredients" }):
       
            ingredients = self.soup.find("ul", { "class": "bu_cuisine_ingredients" }).findAll("li")
        
            for ingredient in ingredients:  
            
                ingredient_ = ingredient.find("a", { "class": "bu_cuisine_pointille_vert name" })
            
                if ingredient_:
                    name = ingredient_.text.strip()
                    quantity = ingredient_.previous_sibling
                    if quantity:
                        quantity = quantity.strip()
                        self.ingredients.append(f"{quantity} {name}")
                    else:
                        self.ingredients.append(name)              

        else:

            ingredients = self.soup.find("ul", { "class": "app_recipe_list" }).findAll("h3", { "class": "app_recipe_ing_title" })

            for ingredient in ingredients:
                if ingredient.a:
                    name = ingredient.a.text.strip()
                    if ingredient.span:
                        quantity = ingredient.span.text.replace('\n', '')
                        quantity = ' '.join(quantity.split())
                        if quantity:
                            self.ingredients.append(f"{quantity} {name}")
                    else:
                        self.ingredients.append(name)       
        
    def _get_directions(self):
        directions = self.soup.findAll("li", { "class": "bu_cuisine_recette_prepa" })

        for direction in directions:
            direction_ = direction.text.replace('\n', '')
            tokens = direction_.split()
            if tokens[0] == "Pour":
                direction_ = ' '.join(tokens[2:])
            else:
                direction_ = ' '.join(tokens[1:])
            self.directions.append(direction_)
    
    
    def _get_servings(self):
        if self.soup.find("span", { "id": "numberPerson" }):
            servings = self.soup.find("span", { "id": "numberPerson" }).text
        else:
            servings = self.soup.find("span", { "class": "bu_cuisine_title_3--subtitle" }).text
        
        self.servings = re.sub("[^0-9]", "", servings)