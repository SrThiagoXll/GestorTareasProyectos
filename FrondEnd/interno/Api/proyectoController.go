package controller

import "Gestor/interno/Models"

func ObtenerProyectos() []Models.Proyecto {
	return []Models.Proyecto{
		{
			Nombre_Proyecto: "Gestor Fyne",
			Estado_Proyecto: "Pendiente",
		},
		{
			Nombre_Proyecto: "API Proyectos",
			Estado_Proyecto: "Finalizado",
		},
		{
			Nombre_Proyecto: "Dashboard",
			Estado_Proyecto: "Pendiente",
		},
	}
}
