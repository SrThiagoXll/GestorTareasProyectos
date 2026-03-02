from fastapi import APIRouter, Depends, HTTPException,status
from sqlalchemy.orm import Session
from Model.Usuario import UsuarioOut
from DB.coneccion import SessionLocal
from fastapi.security import OAuth2PasswordBearer
import jwt


from Model.Login import LoginRequest
from Modelos.UsuarioSql import Usuario
from Segurity.auth import verify_password,create_access_token, SECRET_KEY, ALGORITHM

router = APIRouter(tags=["Login"])

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


oauth2_scheme = OAuth2PasswordBearer(tokenUrl="login")

def get_current_user(
    token: str = Depends(oauth2_scheme),
    db: Session = Depends(get_db)
):
    credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="No autorizado",
        headers={"WWW-Authenticate": "Bearer"},
    )

    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        user_id: str | None = payload.get("sub")

        if user_id is None:
            raise credentials_exception

    except jwt.PyJWTError:
        raise credentials_exception

    user = db.query(Usuario).filter(
        Usuario.Usuario_ID == user_id
    ).first()

    if user is None:
        raise credentials_exception

    return user

def authenticate_user(db_user, password: str):

    if not db_user:
        return False

    if not verify_password(password, db_user.Contraseña):
        return False

    return db_user


@router.get("/me")
async def me(user: Usuario = Depends(get_current_user)):
    return {
        "id": user.Usuario_ID,
        "username": user.Nombre_Usuario,
        "Rol": user.Rol
    }

@router.post("/login")
async def login(
    data: LoginRequest,
    db: Session = Depends(get_db)
):

    user = db.query(Usuario).filter(
        Usuario.Nombre_Usuario == data.username
    ).first()

    if not user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Usuario o contraseña incorrectos"
        )
    
    if not verify_password(data.password, user.Contraseña):
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Usuario o contraseña incorrectos"
        )

    access_token = create_access_token(
        data={
            "sub": str(user.Usuario_ID),
            "username": user.Nombre_Usuario
        }
    )

    return {
        "access_token": access_token,
        "token_type": "bearer",
        "usuario": UsuarioOut.model_validate(user)
    }