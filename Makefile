.PHONY: init test pep8 lint ci run_dev run

init:
	pip install -r requirements.txt

test:
	coverage run -m py.test tests/
	coverage report

pep8:
	flake8 --count --statistics

lint:
	PYTHONPATH=${PWD}/api pylint ${PWD}/api

ci: pep8 lint test

run_dev:
	python api/runserver.py --env development

run:
	gunicorn --pythonpath api runserver:app -b 0.0.0.0:5000
