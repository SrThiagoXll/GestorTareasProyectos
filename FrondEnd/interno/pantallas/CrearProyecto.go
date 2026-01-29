package pantalla

import (
	funcion "Gestor/interno/Funcs"

	"fyne.io/fyne/v2"
	"fyne.io/fyne/v2/container"
	"fyne.io/fyne/v2/dialog"
	"fyne.io/fyne/v2/widget"
)

func MostrarCrearProyectoEnPanel(w fyne.Window, panel *fyne.Container) {

	// ---------- Entrys ----------
	entryNombre := widget.NewEntry()
	entryNombre.SetPlaceHolder("Nombre del proyecto")

	entryDescripcion := widget.NewMultiLineEntry()
	entryDescripcion.SetPlaceHolder("Descripción del proyecto")

	entryFechaInicio := widget.NewEntry()
	//entryFechaInicio.Disable()

	entryFechaFinal := widget.NewEntry()
	//entryFechaFinal.Disable()

	estadoSelect := widget.NewSelect(
		[]string{"Pendiente", "En Progreso", "Finalizado"},
		func(string) {},
	)
	estadoSelect.SetSelected("Pendiente")

	// ---------- Selector de fecha ----------
	mostrarSelectorFecha := func(entry *widget.Entry) {
		funcion.MostrarCalendario(w, func(fecha string) {
			entry.SetText(fecha)
		})
	}

	// ---------- Botones calendario ----------
	btnFechaInicio := widget.NewButton("📅", func() {
		mostrarSelectorFecha(entryFechaInicio)
	})

	btnFechaFinal := widget.NewButton("📅", func() {
		mostrarSelectorFecha(entryFechaFinal)
	})

	// ---------- Botón guardar ----------
	btnGuardar := widget.NewButton("Guardar Proyecto", func() {

		if entryNombre.Text == "" ||
			entryDescripcion.Text == "" ||
			entryFechaInicio.Text == "" ||
			entryFechaFinal.Text == "" ||
			estadoSelect.Selected == "" {
			dialog.ShowInformation(
				"Validación",
				"Nombre, Descripcion fecha de inicio, Fecha Final y Estado son obligatorios",
				w,
			)
			return
		}

		// Aquí luego conectas BD o API
		dialog.ShowInformation(
			"Éxito",
			"Proyecto creado correctamente",
			w,
		)
	})

	// ---------- Formulario ----------
	form := container.NewVBox(
		widget.NewLabelWithStyle(
			"Nuevo Proyecto",
			fyne.TextAlignLeading,
			fyne.TextStyle{Bold: true},
		),

		widget.NewForm(
			widget.NewFormItem("Nombre", entryNombre),
			widget.NewFormItem("Descripción", entryDescripcion),
			widget.NewFormItem(
				"Fecha inicio",
				container.NewBorder(nil, nil, nil, btnFechaInicio, entryFechaInicio),
			),
			widget.NewFormItem(
				"Fecha final",
				container.NewBorder(nil, nil, nil, btnFechaFinal, entryFechaFinal),
			),
			widget.NewFormItem("Estado", estadoSelect),
		),

		btnGuardar,
	)

	// ---------- Reemplazar contenido del panel ----------
	panel.Objects = []fyne.CanvasObject{form}
	panel.Refresh()
}
