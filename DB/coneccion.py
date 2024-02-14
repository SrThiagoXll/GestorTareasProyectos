from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

engine = create_engine('mssql+pyodbc://rexistenciar:3024192892@DESKTOP-AIG4BPM\\SQLEXPRESS/GestorTareas?driver=ODBC+Driver+17+for+SQL+Server', echo=True)
connection = engine.connect()
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

def init_db():
    from Models import UsuarioSql
    UsuarioSql.Base.metadata.drop_all(bind=engine)
    UsuarioSql.Base.metadata.create_all(bind=engine)



    



