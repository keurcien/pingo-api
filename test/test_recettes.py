import pytest

from pingo_api.scraper import create_recipe


@pytest.mark.parametrize(
    "url, recipe_ref",
    [
        (
            "https://www.cuisineaz.com/recettes/pot-au-feu-traditionnel-5620.aspx",
            {
                "name": "Pot-au-feu traditionnel",
                "servings": "6",
                "ingredients": 15,
                "directions": 4,
            },
        ),
        (
            "https://cuisine.journaldesfemmes.fr/recette/307392-steak-hache-a-la-japonaise",
            {
                "name": "Steak haché à la japonaise",
                "servings": "2",
                "ingredients": 9,
                "directions": 6,
            },
        ),
        (
            "https://cuisine.journaldesfemmes.fr/recette/176020-pot-au-feu",
            {
                "name": "Pot-au-feu : la meilleure recette",
                "servings": "8",
                "ingredients": 17,
                "directions": 6,
            },
        ),
        (
            "https://www.marmiton.org/recettes/recette_pot-au-feu_32792.aspx",
            {
                "name": "Pot-au-feu",
                "servings": "4",
                "ingredients": 13,
                "directions": 10,
            },
        ),
        (
            "https://www.750g.com/pot-au-feu-r1452.htm",
            {
                "name": "Pot au feu",
                "servings": "6",
                "ingredients": 17,
                "directions": 4,
            },
        ),
    ],
)
def test_recettes(url, recipe_ref):
    recipe = create_recipe(url)

    assert url == recipe.url
    assert recipe_ref["name"] == recipe.name
    assert recipe_ref["servings"] == recipe.servings
    assert recipe_ref["ingredients"] == len(recipe.ingredients)
    assert recipe_ref["directions"] == len(recipe.directions)
