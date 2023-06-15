# makefile

_build:
	docker-compose --project-name django_utils up -d --build --force-recreate --remove-orphans
	docker ps

_admin:
	docker exec django_utils bash -c "echo \"from django.contrib.auth.models import User; User.objects.create_superuser('admin', '', 'admin')\" | python manage.py shell"

logs:
	docker logs -f django_utils

ssh:
	docker exec -it django_utils bash
