from ._cuisineaz import RecetteCuisineAZ
from ._jdf import RecetteJournalDesFemmes
from ._marmiton import RecetteMarmiton
from ._sccg import Recette750g

__all__ = [
    "create_recipe",
]


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
