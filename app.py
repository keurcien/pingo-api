import falcon
import json
import sys
import os
from falcon_cors import CORS

sys.path.insert(0, os.path.dirname(__file__))

from scraper import recette

cors = CORS(allow_all_origins=True, allow_all_headers=True)

class Recette:

    def on_get(self, req, resp):
        resp.body = json.dumps("Hello World!")
        resp.status = falcon.HTTP_200

    def on_post(self, req, resp):
        
        url = req.media.get('url')

        try:
            
            r = recette.create_recipe(url)
            
            if r:
                resp.status = falcon.HTTP_200
                resp.body = json.dumps(vars(r))
            else:
                resp.status = falcon.HTTP_400
        except:

            resp.status = falcon.HTTP_500

app = falcon.API(middleware=[cors.middleware])

app.add_route('/recette', Recette())
