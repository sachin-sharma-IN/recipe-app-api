.PHONY: test startapp stopapp

test:
	docker-compose run --rm app sh -c "python manage.py test"

startapp:
	docker-compose up

stopapp:
	docker-compose down
