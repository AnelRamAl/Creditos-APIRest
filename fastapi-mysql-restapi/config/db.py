from sqlalchemy import create_engine, MetaData
#                            user:contraseña@server:puerto/ DB
engine = create_engine("mysql+pymysql://anel:password@localhost:3306/prueba")

meta=MetaData()
conn = engine.connect()