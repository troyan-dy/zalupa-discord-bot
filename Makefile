SERVICE_NAME := app

setup:
	@poetry install --no-root

lint:
	poetry run ruff check $(SERVICE_NAME)/
	poetry run ruff format --check $(SERVICE_NAME)/
	poetry run mypy $(SERVICE_NAME)/
	poetry run flake8 $(SERVICE_NAME)/ --select=WPS

format:
	@poetry run ruff check --fix $(SERVICE_NAME)/
	@poetry run ruff format $(SERVICE_NAME)/

requirements:
	@poetry export -f requirements.txt --without-hashes -o requirements.txt

test:
	@poetry run pytest tests --cov $(SERVICE_NAME) -vv

start:
	@poetry run python -m $(SERVICE_NAME).app


start_docker:
	docker-compose  down && docker-compose up --build -d && docker-compose logs -f
