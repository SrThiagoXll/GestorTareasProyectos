package main

import (
	pantalla "Gestor/interno/pantallas"

	"fyne.io/fyne"
	"fyne.io/fyne/app"
	"fyne.io/fyne/container"
	"fyne.io/fyne/widget"
)

func main() {
	a := app.New()
	w := a.NewWindow("Sistema de Usuarios")
	w.Resize(fyne.NewSize(500, 400))

	// Contenido central
	content := widget.NewLabelWithStyle(
		"Bienvenido al Sistema\n\nSeleccione una opción del menú",
		fyne.TextAlignCenter,
		fyne.TextStyle{Bold: true},
	)

	w.SetContent(container.NewCenter(content))

	// ===== MENÚ =====
	menuRegistrar := fyne.NewMenuItem("Registrar Usuario", func() {
		pantalla.Registro(w)
	})

	menuLogin := fyne.NewMenuItem("Login", func() {
		pantalla.MostrarLogin(w)
	})

	menuSalir := fyne.NewMenuItem("Salir", func() {
		// w.Close()
	})

	menuUsuarios := fyne.NewMenu("Usuarios",
		menuRegistrar,
		menuLogin,
	)

	menuArchivo := fyne.NewMenu("Archivo", menuSalir)

	mainMenu := fyne.NewMainMenu(
		menuArchivo,
		menuUsuarios,
	)

	w.SetMainMenu(mainMenu)
	w.ShowAndRun()
}
