import json
import falcon
from falcon_cors import CORS
from pingo_api.scraper import recette

cors = CORS(
    allow_all_origins=True, 
    allow_all_methods=True, 
    allow_all_headers=True
)

import logging 
logger = logging.getLogger(__name__)
logger.addHandler(logging.FileHandler('pingo_api.log'))
logger.setLevel(logging.DEBUG) 

class Recette:

    def on_post(self, req, resp):
        
        url = req.media.get('url')

        try:
            
            r = recette.create_recipe(url)
            resp.status = falcon.HTTP_200
            resp.body = json.dumps({
                "url": r.url,
                "name": r.name,
                "ingredients": r.ingredients,
                "directions": r.directions,
                "servings": r.servings   
            })

        except:

            logger.error(f"Scraping failed: {url}")
            resp.status = falcon.HTTP_400




app = falcon.API(middleware=[cors.middleware])

app.add_route('/recette', Recette())
