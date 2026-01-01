package controller

import (
	"Gestor/interno/Models"
	"bytes"
	"encoding/json"
	"fmt"
	"net/http"
)

func CrearUsuario(usuario Models.Usuario) error {

	jsonData, err := json.Marshal(usuario)
	if err != nil {
		return fmt.Errorf("error generando JSON: %w", err)
	}

	resp, err := http.Post(
		"http://127.0.0.1:8000/Usuario/Crear_Usuario",
		"application/json",
		bytes.NewBuffer(jsonData),
	)
	if err != nil {
		return fmt.Errorf("error enviando al API: %w", err)
	}
	defer resp.Body.Close()

	if resp.StatusCode != http.StatusCreated {
		return fmt.Errorf("error API: %s", resp.Status)
	}

	return nil
}
