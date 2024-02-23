from sqlalchemy import Column,ForeignKey,String,Integer,Date,DateTime
from sqlalchemy.orm import relationship, declarative_base

Base = declarative_base()

class Usuario(Base):
    __tablename__ = "Usuario"
    Usuario_ID = Column(Integer,primary_key=True,autoincrement=True)
    Nombre_Usuario = Column(String(18),unique=True,nullable=False)
    Nombre_Completo = Column(String(50),unique=True,nullable=False)
    Correo = Column(String(100),unique=True,nullable=False)
    Contraseña = Column(String(100),unique=True,nullable=False)
    Rol = Column(String(30),nullable=False)

    comentario = relationship("Comentario",back_populates="usuario")
    actividad = relationship("Actividad",back_populates="usuario")
    asignacion = relationship("Asignacion",back_populates="usuario")

class Proyecto(Base):
    __tablename__ = "Proyecto"
    Proyecto_ID = Column(Integer,primary_key=True,autoincrement=True)
    Nombre_Proyecto = Column(String(50),nullable=False)
    Descripción = Column(String(155),nullable=False)
    Fecha_Inicio = Column(Date,nullable=False)
    Fecha_Final = Column(Date,nullable=False)
    Estado_Proyecto = Column(String(30),nullable=False) # por hacer, en progreso, completado, etc.

    tarea = relationship('Tarea',back_populates='proyecto')

class Tarea(Base):
    __tablename__ = "Tarea"
    Tarea_ID = Column(Integer,primary_key=True,autoincrement=True)
    Nombre_Tarea = Column(String(50),nullable=False)
    Descripción = Column(String(155),nullable=False)
    Fecha_Inicio = Column(Date,nullable=False)
    Fecha_Final = Column(Date,nullable=False)
    Estado_Tarea = Column(String(30),nullable=False) # por hacer, en progreso, completado, etc.
    Prioridad = Column(String(30)) # baja, media, alta
    Proyecto_ID = Column(Integer, ForeignKey('Proyecto.Proyecto_ID'))

    proyecto = relationship("Proyecto",back_populates="tarea")
    comentario = relationship("Comentario",back_populates="tarea")
    documento = relationship("Documento",back_populates="tarea")
    asignacion = relationship("Asignacion",back_populates="tarea")

class Comentario(Base):
    __tablename__ = "Comentario"
    Comentario_ID = Column(Integer,primary_key=True,autoincrement=True)
    Contenido = Column(String(155),nullable=False)
    Fecha = Column(Date,nullable=False)
    Tarea_ID = Column(Integer,ForeignKey('Tarea.Tarea_ID'))
    Usuario_ID = Column(Integer,ForeignKey('Usuario.Usuario_ID'))

    tarea = relationship("Tarea",back_populates="comentario")
    usuario = relationship("Usuario",back_populates="comentario")

class Actividad(Base):
    __tablename__ = "Actividad"
    Actividad_ID = Column(Integer,primary_key=True,autoincrement=True)
    Tipo_Actividad = Column(String(50),nullable=False)
    Descripción = Column(String(155),nullable=False)
    Fecha_Actividad = Column(Date,nullable=False)
    Usuario_ID = Column(Integer,ForeignKey('Usuario.Usuario_ID'))

    usuario = relationship("Usuario",back_populates="actividad")

class Documento(Base):
    __tablename__ = "Documento"
    Documento_ID = Column(Integer,primary_key=True,autoincrement=True)
    Nombre = Column(String(255),nullable=False)
    Ruta = Column(String(255),unique=True)
    Tarea_ID = Column(Integer,ForeignKey('Tarea.Tarea_ID'))

    tarea = relationship("Tarea",back_populates="documento")

class Asignacion(Base):
    __tablename__ = "AsignacionTareas"
    Asignar_ID = Column(Integer,primary_key=True,autoincrement=True)
    Fecha_Asignacion = Column(Date)
    Fecha_Vencimiento = Column(Date)
    Tarea_ID = Column(Integer,ForeignKey('Tarea.Tarea_ID'))
    Usuario_ID = Column(Integer,ForeignKey('Usuario.Usuario_ID'))

    tarea = relationship("Tarea",back_populates="asignacion")
    usuario = relationship("Usuario",back_populates="asignacion")

class SubTarea(Base):
    __tablename__ = "SubTarea"
    SubTarea_ID = Column(Integer,primary_key=True,autoincrement=True)
    Nombre_SubTarea = Column(String(50),nullable=False)
    Descripción = Column(String(155),nullable=False)
    Fecha_Inicio = Column(Date,nullable=False)
    Fecha_Final = Column(Date,nullable=False)