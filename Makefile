.PHONY: test startapp stopapp buildapp format

test:
	docker-compose run --rm app sh -c "python manage.py test"

startapp:
	docker-compose up

stopapp:
	docker-compose down

buildapp:
	docker-compose build

format:
	docker-compose run --rm app sh -c "python manage.py flake8"
