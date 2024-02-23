CREATE PROCEDURE ObtenerDatosTareaUsuario
AS
BEGIN
    SELECT TU.Usuario_ID, T.Nombre_tarea as 'Tarea',T.Descripción, ST.Nombre_SubTarea as 'SubTarea',ST.Descripción,T.Prioridad
    FROM Tarea_Usuario TU
    INNER JOIN dbo.Tarea T ON TU.Tarea_ID = T.Tarea_ID
    INNER JOIN dbo.SubTarea_Tarea STT ON TU.Tarea_ID = STT.Tarea_ID
    INNER JOIN dbo.SubTarea ST ON STT.SubTarea_ID = ST.SubTarea_ID;
END;

exec ObtenerDatosTareaUsuario