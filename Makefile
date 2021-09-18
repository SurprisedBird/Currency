SHELL := /bin/bash

manage_py := python my_app/manage.py

runserver:
	$(manage_py) runserver 0:8000

migrate:
	$(manage_py) migrate

makemigrations:
	$(manage_py) makemigrations

shell:
	$(manage_py) shell_plus --print-sql

worker:
	cd my_app && celery -A settings worker -l info --autoscale=0,10

beat:
	cd my_app && celery -A settings beat -l info
