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

show_urls:
	$(manage_py) show_urls

worker:
	cd my_app && celery -A settings worker -l info --autoscale=0,10

beat:
	cd my_app && celery -A settings beat -l info

superuser:
	$(manage_py) createsuperuser
pytest:
	pytest ./my_app/tests/ --cov=app --cov-report html && coverage report --fail-under=74

show-coverage:  ## open coverage HTML report in default browser
	python3 -c "import webbrowser; webbrowser.open('.pytest_cache/coverage/index.html')"
