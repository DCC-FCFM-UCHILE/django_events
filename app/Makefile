precommit:
	isort . --skip ./sso --settings-path pyproject.toml
	black . --config pyproject.toml
	flake8 . --config .flake8
	djlint . --reformat

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

docs:
	mkdir -p ../docs/images
	python manage.py graph_models --pygraphviz  users ../docs/images/users.png
	python manage.py graph_models --pygraphviz events -g -o ../docs/images/events.png