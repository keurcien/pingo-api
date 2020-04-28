# pingo-api

## To get started

```
cd pingo-api
virtualenv venv-api
pip install -r requirements.txt
```

## Run the local server

```
waitress-serve --port=8000 app:app
```

You can also use `gunicorn` if you like.

## Make a request to the local server

I like to use Postman but if you prefer CLI tools, you can always use `httpie`

```
pip install httpie

http localhost:8000/recette url=https://www.marmiton.org/recettes/recette_soupe-a-l-oignon_10891.aspx
```

## TODO

- Madame Le Figaro
- Add falcon-cors
