.PHONY: run

test:
	py.test --flake8 --cov=resttest

setup:
	pip install -r requirements.txt
	pip install -r requirements-test.txt

run:
	PYTHONPATH=. python app.py
