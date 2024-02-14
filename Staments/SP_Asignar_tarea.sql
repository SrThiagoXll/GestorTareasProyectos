alter procedure ObtenerAsignacionTarea
as 
BEGIN
    select U.Usuario_ID,U.Nombre_Usuario,T.Nombre_Tarea,T.Descripción,T.Estado_Tarea,T.Prioridad,T.Fecha_Inicio,A.Fecha_Vencimiento
    from AsignacionTareas A
    inner join Tarea T on A.Tarea_ID = T.Tarea_ID
    inner join Usuario U on A.Usuario_ID = U.Usuario_ID
end

exec ObtenerAsignacionTarea