SGBD = 'mysql+mysqlconnector'  # Ou 'mysql+pymysql' se for usar pymysql
usuario = 'root'
senha = '1234567'
servidor = 'db'  # nome do serviço do MySQL no docker-compose
database = 'games'

SQLALCHEMY_DATABASE_URI = f'{SGBD}://{usuario}:{senha}@{servidor}/{database}'
