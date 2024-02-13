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

update:
	poetry update

test:
	poetry run python ./manage.py test --verbosity 2
