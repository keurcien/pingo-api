import json
import logging 
import falcon
from falcon_cors import CORS
from pingo_api.scraper import recette

logger = logging.getLogger(__name__)
logger.addHandler(logging.FileHandler('pingo_api.log'))
logger.setLevel(logging.DEBUG) 

cors = CORS(
    allow_all_origins=True, 
    allow_all_methods=True, 
    allow_all_headers=True
)

class Recette:

    def on_post(self, req, resp):
        
        url = req.media.get('url')
        print(url)
        try:
            
            r = recette.create_recipe(url)

            if not r.ingredients:
                logger.error(f"Couldn't retrieve ingredients: {url}")

            if not r.directions:
                logger.error(f"Couldn't retrieve directions: {url}")

            if len(r.ingredients) == 1:
                logger.warning(f"Found only one ingredient: {url}")

            if len(r.directions) == 1:
                logger.warning(f"Found only one direction: {url}")

            resp.status = falcon.HTTP_200
            resp.body = json.dumps({
                "url": r.url,
                "name": r.name,
                "ingredients": r.ingredients,
                "directions": r.directions,
                "servings": r.servings   
            })

        except Exception as e:

            logger.error(f"Scraping failed: {url}")
            resp.status = falcon.HTTP_400
            raise e
        
app = falcon.API(middleware=[cors.middleware])

app.add_route('/recette', Recette())
