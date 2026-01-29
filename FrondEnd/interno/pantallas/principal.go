package pantalla

import (
	"fyne.io/fyne/v2"
	"fyne.io/fyne/v2/container"
	"fyne.io/fyne/v2/layout"
	"fyne.io/fyne/v2/widget"
)

func Principal(w fyne.Window) {
	// ===== HEADER =====
	lblTitulo := widget.NewLabelWithStyle(
		"Gestor de Proyectos",
		fyne.TextAlignLeading,
		fyne.TextStyle{Bold: true},
	)

	lblUsuario := widget.NewLabel("Usuario: Invitado")

	acciones := widget.NewSelect(
		[]string{"Registrar usuario", "Iniciar Sección"},
		func(opcion string) {
			switch opcion {
			case "Registrar usuario":
				Registro(w)
			case "Iniciar Sección":
				MostrarLogin(w)
			}
		},
	)

	acciones.SetSelected("Seleccione una opción")

	header := container.NewHBox(
		lblTitulo,
		layout.NewSpacer(),
		lblUsuario,
		acciones,
	)

	// ===== CONTENIDO CENTRAL =====
	descripcion := widget.NewLabel(
		"Bienvenido al sistema de gestión de proyectos.\n\n" +
			"Desde aquí podrá:\n" +
			"• Crear y organizar proyectos\n" +
			"• Asignar tareas\n" +
			"• Controlar fechas y estados\n" +
			"• Visualizar el progreso",
	)

	content := container.NewVBox(
		widget.NewSeparator(),
		widget.NewSeparator(),
		descripcion,
	)

	// ===== LAYOUT GENERAL =====
	mainLayout := container.NewVBox(
		container.NewPadded(header),
		container.NewPadded(content),
	)

	w.SetContent(mainLayout)
}
