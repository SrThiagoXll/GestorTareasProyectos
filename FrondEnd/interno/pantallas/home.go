package pantalla

import (
	funcion "Gestor/interno/Funcs"
	pantalla "Gestor/interno/pantallas/Proyecto"

	"fyne.io/fyne/v2"
	"fyne.io/fyne/v2/container"
	"fyne.io/fyne/v2/layout"
	"fyne.io/fyne/v2/widget"
)

var panelContenido *fyne.Container

func PantallaInicio(w fyne.Window, nombreUsuario string) {

	// ===== HEADER =====
	titulo := widget.NewLabelWithStyle(
		"Gestor de Proyectos",
		fyne.TextAlignLeading,
		fyne.TextStyle{Bold: true},
	)

	lblUsuario := widget.NewLabel("Usuario: " + nombreUsuario)

	btnSalir := widget.NewButton("Salir", func() {
		funcion.MostrarHome(w)
	})

	header := container.NewHBox(
		titulo,
		layout.NewSpacer(),
		lblUsuario,
		btnSalir,
	)

	// ===== PANEL CENTRAL =====
	panelContenido = container.NewVBox(
		widget.NewLabelWithStyle(
			"Proyecto: Demo",
			fyne.TextAlignLeading,
			fyne.TextStyle{Bold: true},
		),
		widget.NewSeparator(),
		widget.NewLabel("Seleccione una opción del menú"),
	)

	// ===== SIDEBAR =====
	btnNuevo := widget.NewButton("➕ Nuevo Proyecto", func() {
		pantalla.MostrarCrearProyectoEnPanel(w, panelContenido)
	})

	sidebar := container.NewVBox(
		widget.NewLabelWithStyle(
			"Menú",
			fyne.TextAlignLeading,
			fyne.TextStyle{Bold: true},
		),
		widget.NewSeparator(),
		btnNuevo,
		layout.NewSpacer(),
	)

	// ===== LAYOUT GENERAL =====
	body := container.NewHSplit(
		container.NewPadded(sidebar),
		container.NewPadded(panelContenido),
	)
	body.Offset = 0.25

	mainLayout := container.NewVBox(
		container.NewPadded(header),
		widget.NewSeparator(),
		body,
	)

	w.SetContent(mainLayout)
}
