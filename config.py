import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

class Config:
    SECRET_KEY = 'uma_chave_secreta_qualquer'
    SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(BASE_DIR, 'site.db')
    SQLALCHEMY_TRACK_MODIFICATIONS = False
