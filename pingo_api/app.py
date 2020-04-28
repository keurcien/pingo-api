import falcon
import json
from scraper import recette

class Recette:

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

app = falcon.API()

app.add_route('/recette', Recette())