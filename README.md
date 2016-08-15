# flask-api-scaffolding
API Scaffolding for Flask with linting, tests, and json-api responses

The project aims to be simple scaffolding setup for APIs built with flask.

## Running Linting and Tests
### PEP8
```flake8 --count --statistics```

### PyLint
```PYTHONPATH=$PWD pylint $PWD```

### Tests and Coverage Reports
```coverage run -m py.test tests/ && coverage report```

## Running the Application
### Development
```python runserver.py --env development```

### Production with Gunicorn
```gunicorn runserver:app -b 0.0.0.0:5000```
