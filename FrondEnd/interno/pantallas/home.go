package pantalla

import (
	"fyne.io/fyne"
	"fyne.io/fyne/container"
	"fyne.io/fyne/widget"
)

func MostrarHome(w fyne.Window) {
	content := widget.NewLabelWithStyle(
		"Bienvenido al Sistema\n\nSeleccione una opción del menú",
		fyne.TextAlignCenter,
		fyne.TextStyle{Bold: true},
	)

	w.SetContent(container.NewCenter(content))
}
