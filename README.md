## Fabric lookup app

Very simple app for lookup of the fabrics based on the information that was scraped from Wikipedia ([scraping script repo](https://github.com/simicic/scrapingWikipediaTopic))

Data source: [List of fabrics](https://en.wikipedia.org/wiki/List_of_fabrics) and linked pages 

#### Features

- Import data about fabrics from a csv
- Get list of all fabrics info (json)
- Get info about one fabrics given an id (json)


#### Running the app

Set app secret:

`export APP_SECRET='something-really-secret'`

Set environment variables: 

```
export FLASK_APP=/path/to/auto_app.py
export FLASK_DEBUG=1
```

Install dependencies, for pipenv: 

`pipenv install`

Setup database:

```
flask db init
flask db migrate
flask db upgrade
```

Run app: 

` flask run`

#### TODO: 

- return fabric sustainability rating
- API authentication
- API versioning
- dockerize

#### Notes

App structure is inspired by [flask-realworld-example-app](https://github.com/gothinkster/flask-realworld-example-app) 
