package Models

type Proyecto struct {
	Nombre_Proyecto string `json:"Nombre_Proyecto"`
	Descripción     string `json:"Descripción"`
	Fecha_Inicio    string `json:"Fecha_Inicio"`
	Fecha_Final     string `json:"Fecha_Final"`
	Estado_Proyecto string `json:"Estado_Proyecto"`
}
