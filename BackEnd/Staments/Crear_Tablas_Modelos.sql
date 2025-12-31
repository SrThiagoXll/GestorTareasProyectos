CREATE TABLE Usuario (
    Usuario_ID INT PRIMARY KEY IDENTITY(1,1),
    Nombre_Usuario VARCHAR(18) UNIQUE NOT NULL,
    Nombre_Completo VARCHAR(50) UNIQUE NOT NULL,
    Correo VARCHAR(100) UNIQUE NOT NULL,
    Contraseña VARCHAR(100) UNIQUE NOT NULL,
    Rol VARCHAR(30) NOT NULL
);

CREATE TABLE Proyecto (
    Proyecto_ID INT PRIMARY KEY IDENTITY(1,1),
    Nombre_Proyecto VARCHAR(50) NOT NULL,
    Descripción VARCHAR(155) NOT NULL,
    Fecha_Inicio DATE NOT NULL,
    Fecha_Final DATE NOT NULL,
    Estado_Proyecto VARCHAR(30) NOT NULL
);

CREATE TABLE Tarea (
    Tarea_ID INT PRIMARY KEY IDENTITY(1,1),
    Nombre_Tarea VARCHAR(50) NOT NULL,
    Descripción VARCHAR(155) NOT NULL,
    Fecha_Inicio DATE NOT NULL,
    Fecha_Final DATE NOT NULL,
    Estado_Tarea VARCHAR(30) NOT NULL,
    Prioridad VARCHAR(30),
    Proyecto_ID INT FOREIGN KEY REFERENCES Proyecto(Proyecto_ID)
);

CREATE TABLE Comentario (
    Comentario_ID INT PRIMARY KEY IDENTITY(1,1),
    Contenido VARCHAR(155) NOT NULL,
    Fecha DATE NOT NULL,
    Tarea_ID INT FOREIGN KEY REFERENCES Tarea(Tarea_ID),
    Usuario_ID INT FOREIGN KEY REFERENCES Usuario(Usuario_ID)
);

CREATE TABLE Actividad (
    Actividad_ID INT PRIMARY KEY IDENTITY(1,1),
    Tipo_Actividad VARCHAR(50) NOT NULL,
    Descripción VARCHAR(155) NOT NULL,
    Fecha_Actividad DATE NOT NULL,
    Usuario_ID INT FOREIGN KEY REFERENCES Usuario(Usuario_ID)
);

CREATE TABLE Documento (
    Documento_ID INT PRIMARY KEY IDENTITY(1,1),
    Nombre VARCHAR(255) NOT NULL,
    Ruta VARCHAR(255) UNIQUE,
    Tarea_ID INT FOREIGN KEY REFERENCES Tarea(Tarea_ID)
);

CREATE TABLE AsignacionTareas (
    Asignar_ID INT PRIMARY KEY IDENTITY(1,1),
    Fecha_Asignacion DATE,
    Fecha_Vencimiento DATE,
    Tarea_ID INT FOREIGN KEY REFERENCES Tarea(Tarea_ID),
    Usuario_ID INT FOREIGN KEY REFERENCES Usuario(Usuario_ID)
);

CREATE TABLE SubTarea (
    SubTarea_ID INT PRIMARY KEY IDENTITY(1,1),
    Nombre_SubTarea VARCHAR(50) NOT NULL,
    Descripción VARCHAR(155) NOT NULL,
    Fecha_Inicio DATE NOT NULL,
    Fecha_Final DATE NOT NULL
);

CREATE TABLE SubTarea_Tarea (
    SubTarea_Tarea_ID INT PRIMARY KEY IDENTITY(1,1),
    SubTarea_ID INT NOT NULL FOREIGN KEY REFERENCES SubTarea(SubTarea_ID),
    Tarea_ID INT NOT NULL FOREIGN KEY REFERENCES Tarea(Tarea_ID)
);
