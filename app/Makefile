# makefile

precommit:
	black . --config pyproject.yml
	isort . --resolve-all-configs
	flake8 . --config .flake8

bandit:
	bandit -r .

rate:
	pylint *

deadcode:
	vulture . --min-confidence 100

healthcheck:
	make rate
	make deadcode

migrations:
	python manage.py makemigrations
	make precommit

migrate:
	python manage.py migrate

update:
	pur -r _requirements/base.txt
	pur -r _requirements/production.txt
