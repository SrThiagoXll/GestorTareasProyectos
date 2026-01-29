import os
import shutil
from fastapi import APIRouter,File, Form,UploadFile,Depends,HTTPException,status
from fastapi.responses import FileResponse
from Modelos.UsuarioSql import Documento, Tarea
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

        

router = APIRouter(prefix="/documentos", tags=["Documentos"])

UPLOAD_DIR = "uploads/tareas"
os.makedirs(UPLOAD_DIR, exist_ok=True)

@router.post("/subir",status_code=status.HTTP_201_CREATED)
async def subir_documento(
    tarea_id: int = Form(...),
    file: UploadFile = File(...),
    db: Session = Depends(get_db)
):
    
    tarea = db.query(Tarea).filter(Tarea.Tarea_ID == tarea_id).first()
    if not tarea:
        raise HTTPException(
            status_code=404,
            detail="La tarea no existe"
        )

    # 1️⃣ Validar archivo
    if not file.filename:
        raise HTTPException(status_code=400, detail="Archivo inválido")

    # 2️⃣ Crear nombre único
    extension = os.path.splitext(file.filename)[1]
    nombre_unico = f"{uuid.uuid4()}{extension}"
    ruta_archivo = os.path.join(UPLOAD_DIR, nombre_unico)

    # 3️⃣ Guardar archivo en disco
    with open(ruta_archivo, "wb") as buffer:
        shutil.copyfileobj(file.file, buffer)

    # 4️⃣ Guardar en BD
    documento = Documento(
        Nombre=file.filename,
        Ruta=ruta_archivo,
        Tarea_ID=tarea_id
    )

    db.add(documento)
    db.commit()
    db.refresh(documento)

    return {
        "mensaje": "Documento subido correctamente",
        "documento_id": documento.Documento_ID,
        "nombre": documento.Nombre
    }

@router.get("/descargar/{documento_id}")
def descargar_documento(
    documento_id: int,
    db: Session = Depends(get_db)
):
    # 1️⃣ Buscar documento
    documento = db.query(Documento).filter(
        Documento.Documento_ID == documento_id
    ).first()

    if not documento:
        raise HTTPException(
            status_code=404,
            detail="Documento no encontrado"
        )

    # 2️⃣ Verificar archivo físico
    if not os.path.exists(documento.Ruta):
        raise HTTPException(
            status_code=404,
            detail="Archivo no encontrado en el servidor"
        )

    # 3️⃣ Enviar archivo
    return FileResponse(
        path=documento.Ruta,
        filename=documento.Nombre,
        media_type="application/octet-stream"
    )


