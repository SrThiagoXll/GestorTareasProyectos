package funcion

import (
	"time"

	"fyne.io/fyne/v2"
	"fyne.io/fyne/v2/container"
	"fyne.io/fyne/v2/layout"
	"fyne.io/fyne/v2/widget"
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

func MostrarCalendario(w fyne.Window, onSelect func(string)) {

	selected := time.Now()
	label := widget.NewLabel(selected.Format("2006-01-02"))

	btnPrev := widget.NewButton("<", func() {
		selected = selected.AddDate(0, -1, 0)
		label.SetText(selected.Format("2006-01-02"))
	})

	btnNext := widget.NewButton(">", func() {
		selected = selected.AddDate(0, 1, 0)
		label.SetText(selected.Format("2006-01-02"))
	})

	btnSelect := widget.NewButton("Seleccionar", func() {
		onSelect(selected.Format("2006-01-02"))
	})

	content := container.NewVBox(
		container.NewHBox(btnPrev, layout.NewSpacer(), btnNext),
		label,
		btnSelect,
	)

	widget.ShowModalPopUp(
		container.NewPadded(content),
		w.Canvas(),
	)
}
