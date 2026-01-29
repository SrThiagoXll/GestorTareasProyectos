package pantalla

import (
	controller "Gestor/interno/Api"
	funcion "Gestor/interno/Funcs"

	"fyne.io/fyne/v2"
	"fyne.io/fyne/v2/container"
	"fyne.io/fyne/v2/layout"
	"fyne.io/fyne/v2/widget"
)

var panelContenido *fyne.Container
var (
	lblTotalProyectos *widget.Label
	lblPendientes     *widget.Label
	lblFinalizados    *widget.Label
)

func PantallaInicio(w fyne.Window, nombreUsuario string) {

	// ===== HEADER =====
	titulo := widget.NewLabelWithStyle(
		"Gestor de Proyectos",
		fyne.TextAlignLeading,
		fyne.TextStyle{Bold: true},
	)

	lblUsuario := widget.NewLabel("Usuario: " + nombreUsuario)

	btnSalir := widget.NewButton("Salir", func() {
		Principal(w)
	})

	header := container.NewHBox(
		titulo,
		layout.NewSpacer(),
		lblUsuario,
		btnSalir,
	)

	proyectos := controller.ObtenerProyectos()
	resumen := funcion.CrearResumen()
	funcion.CalcularResumen(proyectos)

	panelCentral := container.NewVBox(
		resumen,
		widget.NewSeparator(),
	)

	// ===== SIDEBAR =====
	btnNuevo := widget.NewButton("➕ Nuevo Proyecto", func() {
		MostrarCrearProyectoEnPanel(w, panelCentral)
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
		container.NewPadded(panelCentral),
	)
	body.Offset = 0.25

	mainLayout := container.NewVBox(
		container.NewPadded(header),
		widget.NewSeparator(),
		body,
	)

	w.SetContent(mainLayout)
}
