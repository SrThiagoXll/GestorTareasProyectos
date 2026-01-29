package main

import (
	pantalla "Gestor/interno/Pantallas"

	"fyne.io/fyne/v2"
	"fyne.io/fyne/v2/app"
)

func main() {
	a := app.New()
	w := a.NewWindow("Gestor de Proyectos")
	w.Resize(fyne.NewSize(900, 550))

	pantalla.Principal(w)

	w.ShowAndRun()
}
