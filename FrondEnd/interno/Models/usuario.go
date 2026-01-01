package Models

type Usuario struct {
	Nombre_Usuario  string `json:"Nombre_Usuario"`
	Nombre_Completo string `json:"Nombre_Completo"`
	Correo          string `json:"Correo"`
	Contraseña      string `json:"Contraseña"`
	Rol             string `json:"Rol"`
}
