run:
	python3 manage.py runserver

migrations:
	python manage.py makemigrations

migrate:
	python manage.py migrate

lint:
	poetry run flake8 .

install:
	poetry install