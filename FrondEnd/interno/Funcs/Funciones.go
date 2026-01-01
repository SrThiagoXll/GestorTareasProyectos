package funcion

import (
	"fyne.io/fyne"
	"fyne.io/fyne/container"
	"fyne.io/fyne/widget"
)

// func LabeledField(label string, field fyne.CanvasObject) fyne.CanvasObject {
// 	lbl := widget.NewLabel(label)
// 	lbl.Alignment = fyne.TextAlignLeading
// 	lbl.TextStyle = fyne.TextStyle{Bold: true}

// 	// Limita el ancho del Entry
// 	fieldContainer := container.NewHBox(
// 		container.NewGridWrap(fyne.NewSize(220, 36), field),
// 	)

//		return container.NewVBox(lbl, fieldContainer)
//	}
func LabeledField(label string, field fyne.CanvasObject) fyne.CanvasObject {
	return container.NewVBox(
		widget.NewLabel(label),
		container.NewGridWrap(
			fyne.NewSize(240, 36),
			field,
		),
	)
}

func MostrarHome(w fyne.Window) {
	content := widget.NewLabelWithStyle(
		"Bienvenido al Sistema\n\nSeleccione una opción del menú",
		fyne.TextAlignCenter,
		fyne.TextStyle{Bold: true},
	)

	w.SetContent(container.NewCenter(content))
}
