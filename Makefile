SERVICE_NAME := app

setup:
	@poetry install --no-root

lint:
	-poetry run mypy $(SERVICE_NAME)/
	poetry run flake8 $(SERVICE_NAME)/ tests/

format:
	@poetry run black $(SERVICE_NAME)/ tests/
	@poetry run isort $(SERVICE_NAME)/ tests/

test:
	@poetry run pytest tests --cov $(SERVICE_NAME) -vv

start:
	@poetry run python -m $(SERVICE_NAME).app


start_docker:
	docker-compose  down && docker-compose up --build -d && docker-compose logs -f
