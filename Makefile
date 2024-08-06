.PHONY: install
install:
	docker compose up --build --detach
	@echo "\nThe development server is running at http://127.0.0.1:8000/\n"

.PHONY: up
up:
	docker compose up --detach
	docker compose run --rm app python manage.py runserver 0.0.0.0:8000

.PHONY: down
down:
	docker compose down

.PHONY: make-migrations
make-migrations:
	docker compose run --rm app python manage.py makemigrations

.PHONY: migrate
migrate:
	docker compose run --rm app python manage.py migrate

.PHONY: create-superuser
create-superuser:
	docker compose run --rm app python manage.py createsuperuser

.PHONY: update
update: install make-migrations migrate ;


.PHONY: test
test:
	docker compose run --rm app python manage.py test

.PHONY: fetch_cryptocurrencies
fetch_cryptocurrencies:
	docker compose run --rm app python manage.py fetch_cryptocurrencies
