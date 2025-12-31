from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from Modelos import UsuarioSql

engine = create_engine('mssql+pyodbc://sa:3024192892@DESKTOP-9J09P0C\\SQLEXPRESS/GestorTareas?driver=ODBC+Driver+17+for+SQL+Server', echo=True)
connection = engine.connect()
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

def init_db():
    
    UsuarioSql.Base.metadata.drop_all(bind=engine)
    UsuarioSql.Base.metadata.create_all(bind=engine)



    



