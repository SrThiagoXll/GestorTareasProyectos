alter procedure ObtenerTareaProyecto
as 
begin 
    select P.Proyecto_ID,T.Tarea_ID,P.Nombre_Proyecto,P.Descripción,T.Nombre_Tarea,T.Descripción,T.Fecha_Inicio,T.Fecha_Final
    from Tarea T
    inner join Proyecto P on T.Proyecto_ID = P.Proyecto_ID
end

exec ObtenerTareaProyecto