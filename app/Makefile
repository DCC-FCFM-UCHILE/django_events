# makefile

precommit:
	black --line-length=140 .
	flake8 --ignore E501 --exclude 'core/settings/*' .

migrations:
	python manage.py makemigrations
	make precommit

migrate:
	python manage.py migrate

update:
	pur -r _requirements/base.txt
	pur -r _requirements/production.txt
