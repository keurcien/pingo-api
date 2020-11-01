import json
import logging 
import falcon
import cv2
import numpy as np
import pytesseract
from falcon_cors import CORS
from falcon_multipart.middleware import MultipartMiddleware
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

class RecetteOCR:

    def on_post(self, req, resp):
        
        custom_config = r'--oem 3 --psm 6'

        try:

            img_ingr = req.get_param('img_ingr')
            img_ingr = img_ingr.file.read()
            img_ingr = np.fromstring(img_ingr, np.uint8)
            img_ingr = cv2.imdecode(img_ingr, cv2.IMREAD_COLOR)
            
            ingredients = pytesseract.image_to_string(img_ingr, config=custom_config)
            ingredients = ingredients.split("\n")
            ingredients = list(filter(lambda ingr: len(ingr) > 2, ingredients))

            img_dir = req.get_param('img_dir')
            img_dir = img_dir.file.read()
            img_dir = np.fromstring(img_dir, np.uint8)
            img_dir = cv2.imdecode(img_dir, cv2.IMREAD_COLOR)
            
            directions = pytesseract.image_to_string(img_dir, config=custom_config)
            directions = directions.split("\n")
            directions = list(filter(lambda ingr: len(ingr) > 2, directions))
        
            resp.media = {
                "ingredients": ingredients,
                "directions": directions
            }
        
        except:

            resp.media = {
                "ingredients": [],
                "directions": []
            }



        
app = falcon.API(middleware=[cors.middleware, MultipartMiddleware()])

app.add_route('/recette', Recette())
app.add_route('/ocr', RecetteOCR())
