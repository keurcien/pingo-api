from scraper.marmiton import RecetteMarmiton
from scraper.jdf import RecetteJournalDesFemmes
from scraper.cuisineaz import RecetteCuisineAZ
from scraper.sccg import Recette750g

def create_recipe(url):
    
    tokens = url.split("/")
    
    if "www.marmiton.org" in tokens:
        return RecetteMarmiton(url)
    elif "cuisine.journaldesfemmes.fr" in tokens:
        return RecetteJournalDesFemmes(url)
    elif "www.cuisineaz.com" in tokens:
        return RecetteCuisineAZ(url)
    elif "www.750g.com" in tokens:
        return Recette750g(url)