import os
BASEDIR = os.path.abspath(os.path.dirname(__file__))

class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY') or '*nm*+1%yq*g(+)1bh5j$tn0h%(rd-=#)1yn7h44)4ch'
    SQLALCHEMY_DATABASE_URI = os.environ.get('SQLALCHEMY_DATABASE_URI') or \
        'sqlite:///' + os.path.join(BASEDIR, 'data.sqlite')
    SQLALCHEMY_TRACK_MODIFICATIONS = False