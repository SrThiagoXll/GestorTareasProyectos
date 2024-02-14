from fastapi import APIRouter,File,UploadFile,Depends,HTTPException
from Models.UsuarioSql import Documento
from sqlalchemy.orm import Session
from Model.Archivo import Archivo
from DB.coneccion import SessionLocal
import uuid

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close

        

router = APIRouter()

