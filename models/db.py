from flask_sqlalchemy import SQLAlchemy

#Instância do gerenciador
db = SQLAlchemy()

instance = "mysql+pymysql://admintest:admintest@localhost:3306/irrigation"