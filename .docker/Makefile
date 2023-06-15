# makefile

build:
	docker-compose --file dc-produccion.yml --project-name django-boilerplate up -d --build --force-recreate --remove-orphans
	docker ps

_build:
	docker-compose --project-name django_boilerplate up -d --build --force-recreate --remove-orphans
	make _migrate
	docker exec django_boilerplate make precommit
	docker ps

_admin:
	docker exec django_boilerplate bash -c "echo \"from django.contrib.auth.models import User; User.objects.create_superuser('admin', '', 'admin')\" | python manage.py shell"

restart:
	docker restart django_boilerplate
	docker ps

update:
	git submodule update
	git stash
	git pull
	git stash pop

_static:
	docker exec django_boilerplate python manage.py collectstatic --no-input

media:
	sudo cp -r ../media/* /home/instalar/media/django_boilerplate

_migrate:
	docker exec django_boilerplate python manage.py migrate

loaddata:
	docker exec django_boilerplate make loaddata

logs:
	docker logs -f django_boilerplate

ssh:
	docker exec -it django_boilerplate bash

deploy:
	make update
	make build
	make migrate
	# make loaddata
	make static
	make media
	make restart

_secret:
	./app/secret.sh
