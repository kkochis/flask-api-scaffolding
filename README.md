# flask-api-scaffolding
API scaffolding project for Flask to use as a starting point to build your next
application.

The goal is to have a good starting point for building APIs/microservices and
avoid getting bogged down by boilerplate when beginning a project. The scaffold
is meant to have good defaults that are easy to change to suit different needs
rather than have every feature under the sun that will bloat your API and slow
down performance.

## Features
* PEP8 style checker (flake8)
* Linting/code quality checking (with PyLint)
* Unit and Integration testing (with pytest and built-in flask goodness)
    * Test coverage reporting (coverage)
* Gunicorn ready (or easily use a different app server)
* JSON API compliant responses (TODO)

## Running Linting and Tests
PEP8 checking:
```make pep8```

Linting and code quality check:
```make lint```

Tests and coverage reports :
```make test```

Do all of the above:
```make ci```

## Running the Application
Development:
```make run_dev```

Production with Gunicorn:
```make run```

## Todo
* swagger docs and validation
*  flesh out example for controller, service and data-access layer
* Extend Flask Response class to accept dictionaries from routes/controllers
  * Make response class return with `Content-Type: application/vnd.api+json`
  * Inteligent defaults for json-api compatibility (prefilled links.self)
  * Potentially split into separate Flask extension?
