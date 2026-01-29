ALTER PROCEDURE sp_CrearProyectoConTareas_JSON
(
    @json NVARCHAR(MAX)
)
AS
BEGIN
    SET NOCOUNT ON;

    BEGIN TRY
        BEGIN TRANSACTION;

        DECLARE @Proyecto_ID INT;

        -- 1️⃣ Insertar Proyecto
        INSERT INTO Proyecto
        (
            Nombre_Proyecto,
            Descripción,
            Estado_Proyecto,
            Fecha_Inicio,
            Fecha_Final
        )
        SELECT
            Nombre_Proyecto,
            Descripcion,
            Estado,
            Fecha_Inicio,
            Fecha_Final
        FROM OPENJSON(@json)
        WITH
        (
            Nombre_Proyecto VARCHAR(50)  '$.Nombre_Proyecto',
            Descripcion     VARCHAR(155) '$.Descripcion',
            Estado          VARCHAR(30)  '$.Estado',
            Fecha_Inicio    DATE         '$.Fecha_Inicio',
            Fecha_Final     DATE         '$.Fecha_Final'
        );

        SET @Proyecto_ID = SCOPE_IDENTITY();

        -- 2️⃣ Insertar múltiples tareas
        INSERT INTO Tarea
        (
            Nombre_Tarea,
            Descripción,
            Fecha_Inicio,
            Fecha_Final,
            Estado_Tarea,
            Prioridad,
            Proyecto_ID
        )
        SELECT
            Nombre_Tarea,
            Descripcion,
            Fecha_Inicio,
            Fecha_Final,
            Estado,
            Prioridad,
            @Proyecto_ID
        FROM OPENJSON(@json, '$.tareas')
        WITH
        (
            Nombre_Tarea VARCHAR(50)  '$.Nombre_Tarea',
            Descripcion  VARCHAR(155) '$.Descripcion',
            Fecha_Inicio DATE         '$.Fecha_Inicio',
            Fecha_Final  DATE         '$.Fecha_Final',
            Estado       VARCHAR(30)  '$.Estado',
            Prioridad    VARCHAR(30)  '$.Prioridad'
        );

        COMMIT TRANSACTION;

        -- 3️⃣ DEVOLVER EL ID
        SELECT @Proyecto_ID AS Proyecto_ID;

    END TRY
    BEGIN CATCH
        ROLLBACK TRANSACTION;
        THROW;
    END CATCH
END;
GO
