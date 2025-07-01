from pycurl import UPLOAD
import os

SECRET_KEY = 'FC3M1'

SGBD = 'mysql+mysqlconnector'
usuario = 'root'
senha = '1234567'
servidor = 'localhost'
database = 'games'

SQLALCHEMY_DATABASE_URI = f'{SGBD}://{usuario}:{senha}@{servidor}/{database}'
SQLALCHEMY_TRACK_MODIFICATIONS = False


UPLOAD_PATH = os.path.dirname(os.path.abspath(__file__)) + '/uploads'