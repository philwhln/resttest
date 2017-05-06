setup:
	pip install -r requirements.txt
	pip install -r requirements-test.txt

test:
	PYTHONPATH=. py.test --flake8 --cov=resttest

run:
	PYTHONPATH=. python app.py

docker-build:
	docker build -t resttest .

docker-run:
	docker run --rm -ti resttest

docker-test: docker-build
	docker build -t resttest-test -f Dockerfile.tests .
	docker run --rm -ti resttest-test
