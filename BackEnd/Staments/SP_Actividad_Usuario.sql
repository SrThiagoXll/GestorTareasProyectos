alter procedure ObtenerActividadUsuario 
    AS 
    BEGIN
        select U.*,A.*
        from Actividad A
        inner join Usuario U on A.Usuario_ID = U.Usuario_ID 
    END

EXEC sp_rename 'sp_Usuario_Actividad','ObtenerActividadUsuario';
exec ObtenerActividadUsuario;