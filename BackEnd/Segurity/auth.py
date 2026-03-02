import os
from datetime import datetime, timedelta, timezone
import re

import jwt
from jwt import PyJWTError
from pwdlib import PasswordHash

SECRET_KEY = "asdfghjklñqwertyuiopasdfghjklñqwertyuiopasdfghjklñqwertyuiop"
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 60

pwd_context = PasswordHash.recommended()


def hash_password(password: str) -> str:
    return pwd_context.hash(password)


def verify_password(plain_password: str, hashed_password: str) -> bool:
    try:
        return pwd_context.verify(plain_password, hashed_password)
    except Exception:
        return False


def crear_Token(data: dict):
    payload = data.copy()
    payload["exp"] = datetime.now(timezone.utc) + timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    token = jwt.encode(payload, SECRET_KEY, algorithm=ALGORITHM)
    return token


def create_access_token(data: dict, expires_delta: timedelta | None = None):
    to_encode = data.copy()
    if expires_delta:
        expire = datetime.now(timezone.utc) + expires_delta
    else:
        expire = datetime.now(timezone.utc) + timedelta(minutes=60)
    to_encode.update({"exp": expire})
    encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
    return encoded_jwt

def decode_token(token: str):
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        return payload
    except PyJWTError:
        return None

def validar_password(password: str) -> tuple[bool, str]:

    if len(password) < 5:
        return False, "La contraseña debe tener mínimo 5 caracteres"

    patron = r'^(?=.*[a-z])(?=.*[A-Z])(?=.*\d).+$'

    if not re.match(patron, password):
        return False, "Debe tener al menos una mayúscula, una minúscula y un número"
    
    return True,""    
