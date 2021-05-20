import os


SECRET_KEY = os.getenv('SECRET_KEY', 'secret string')
# MONGODB_SETTINGS ={
#     'db': 'vis',
#     'host': '103.219.39.150',
#     'port': 20055
# }
HOST = '127.0.0.1'
PORT = '3306'
DATABASE = 'airpollution'
USERNAME = 'root'
PASSWORD = '123456'

DB_URI = "mysql+pymysql://{username}:{password}@{host}:{port}/{db}?charset=utf8".format(username=USERNAME,password=PASSWORD, host=HOST,port=PORT, db=DATABASE)

SQLALCHEMY_DATABASE_URI = DB_URI
SQLALCHEMY_TRACK_MODIFICATIONS = False
SQLALCHEMY_ECHO = True




