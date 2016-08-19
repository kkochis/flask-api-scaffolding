# flask-api-scaffolding
API scaffolding project for Flask to use as a starting point to build your next
application.

The goal is to have a good starting point for building APIs/microservices and
avoid getting bogged down by boilerplate when beginning a project. The scaffold
is meant to have good defaults that are easy to change to suit different needs
rather than have every feature under the sun that will bloat your API and slow
down performance.

## Features
* PEP8 style checker ([flake8](https://pypi.python.org/pypi/flake8))
* Linting/code quality checking (with [PyLint](https://www.pylint.org/))
* Unit and Integration testing (with [pytest](http://doc.pytest.org/) and built-in flask goodness)
  * Test coverage reporting ([coverage](https://pypi.python.org/pypi/coverage))
* Gunicorn ready (or easily use a different app server)
* [JSON API](http://jsonapi.org/) compliant responses (TODO)

## Running Linting and Tests
```
make pep8 # PEP8 checking
make lint # Linting and code quality check
make test # Tests and coverage reports
make ci # Do all of the above
```

## Running the Application
Development:
```
make run_dev
```

Production with Gunicorn:
```
make run
```

## Application Structure / Code Organization
You should notice that this scaffolding does _not_ use the popular MVC
paradigm but you can easily modify the structure to suit whatever paradigm or
method of code organization you prefer.

* **Controllers**: handles and sanatizes inputs, calls the appropriate services
and returns outputs in the correct form for the route.
* **Services**: handles the business or domain logic of the application; may call
out to the data access to get/set data from various data sources.
* **Data Access**: Retrieves data to be returned to the Service layer for
manipulation.

If you want to use a different paradigm, simply rename the directories and use
them according the the paradigm you prefer. 

### Controllers
Remember that if you rename controllers you will need to change the reference
to them in `application.py`. Also note that whatever you call them and however
you use them, that is where the routes are defined.

#### Registering Controllers
Creating a new controller will not automatically cause the application start
serving those routes. You need the register them by editing the
`controllers/__init__.py` file and import the new controller. You can also
change the `__init__.py` to automatically import all files in the controllers
directory if you wish.

## Todo
* swagger docs and validation
*  flesh out example for controller, service and data-access layer
* Extend Flask Response class to accept dictionaries from routes/controllers
  * Make response class return with `Content-Type: application/vnd.api+json`
  * Inteligent defaults for json-api compatibility (prefilled links.self)
  * Potentially split into separate Flask extension?
