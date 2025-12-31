alter procedure ObtenerComentarioTarea
as
begin 
    select U.Usuario_ID,U.Nombre_Usuario,T.Nombre_Tarea,C.Contenido,C.Fecha,T.Descripción,T.Estado_Tarea,T.Fecha_Final
    from Comentario C
    inner join Tarea T on C.Tarea_ID = T.Tarea_ID
    inner join Usuario U on C.Usuario_ID = U.Usuario_ID;
end
exec ObtenerComentarioTarea