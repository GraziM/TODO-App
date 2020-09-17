# TODO APP feito com Flask

Sistema simples de Cadastro de tarefas. Projeto desenvolvido com o intuito de aprender mais sobre o framework flask.

## Para rodar o sistema

    pip install -r requirements.txt
    set FLASK_APP=run.py
    set SECRET_KEY=secretkey 
    set SQLALCHEMY_DATABASE_URI=sqlite:///site.db
    flask db init
    flask db migrate
    flask db upgrade
    flask run
