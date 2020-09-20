# TODO APP feito com Flask

Sistema simples de Cadastro de tarefas. Projeto desenvolvido com o intuito de aprender mais sobre o framework flask.

## Para rodar o sistema

Windows:

	pip install -r requirements.txt
	set FLASK_APP=run.py
	flask db init
	flask db migrate
	flask db upgrade
	flask run
	
Linux, Mac:

	pip install -r requirements.txt
	export FLASK_APP=run.py
	flask db init
	flask db migrate
	flask db upgrade
	flask run