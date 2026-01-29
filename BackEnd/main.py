from  fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from Routers.usuarios import router as usuario_router
from Routers.Usuario import router as Usuario_router
from Routers.Archivo import router as Archivo_router
from Routers.Proyecto import router as Proyecto_router
from Routers.Asignar import router as Asignar_router
from Routers.Tarea import router as Tarea_router
from Routers.SubTarea import router as SubTarea_router
from Routers.Actividad import router as Actividad_router
from Routers.Comentario import router as Comentaro_router
from Routers.Usuario_Actividad import router as UsuarioActivida_router
from Routers.Comentario_Tarea_Usuario import router as ObtenerComentarioTarea_router
from Routers.Asignar_Tarea import router as ObtenerTarea_router
from Routers.Tarea_Proyecto import router as TareaProyecto_router
from Routers.Tarea_Usuario import router as TareaUsuario_router
from Routers.SubTarea_Tarea import router as SubTarea_Tarea_router
from Routers.Login import router as Login_router 
from Routers.Proyectos_Por_Usuario import router as ProyectoPorUsuario_router
from Routers.Crear_Proyecto_Con_Tareas import router as ProyectoTarea_router


app = FastAPI(
    title="Gestion de tareas",
    description="Un servicio de gestor de bases de datos",
    version="0.2.0",
    openapi_version="3.2.1"
    )

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(Actividad_router)
app.include_router(usuario_router)
app.include_router(Usuario_router)
app.include_router(Archivo_router)
app.include_router(Proyecto_router)
app.include_router(Asignar_router)
app.include_router(Tarea_router)
app.include_router(SubTarea_router)
app.include_router(Comentaro_router)
app.include_router(UsuarioActivida_router)
app.include_router(ObtenerComentarioTarea_router)
app.include_router(ObtenerTarea_router)
app.include_router(TareaProyecto_router)
app.include_router(TareaUsuario_router)
app.include_router(SubTarea_Tarea_router)
app.include_router(Login_router)
app.include_router(ProyectoPorUsuario_router)
app.include_router(ProyectoTarea_router)
