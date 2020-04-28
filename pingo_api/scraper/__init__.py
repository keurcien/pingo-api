from .recette import create_recipe

from ._cuisineaz import RecetteCuisineAZ
from ._jdf import RecetteJournalDesFemmes
from ._marmiton import RecetteMarmiton
from ._sccg import Recette750g

__all__ = [
    "create_recipe",
]
