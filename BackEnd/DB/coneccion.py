from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from Modelos import UsuarioSql

engine = create_engine('mssql+pyodbc://@localhost\\SQLEXPRESS/GestorTareasDB?driver=ODBC+Driver+17+for+SQL+Server', echo=True)
connection = engine.connect()
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

def init_db():
    
    UsuarioSql.Base.metadata.create_all(bind=engine)



    



