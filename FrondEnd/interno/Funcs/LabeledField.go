package funcion

import (
	"time"

	"fyne.io/fyne/v2"
	"fyne.io/fyne/v2/container"
	"fyne.io/fyne/v2/layout"
	"fyne.io/fyne/v2/widget"
)

func LabeledField(label string, field fyne.CanvasObject) fyne.CanvasObject {
	return container.NewVBox(
		widget.NewLabel(label),
		container.NewGridWrap(
			fyne.NewSize(240, 36),
			field,
		),
	)
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

	var popup *widget.PopUp

	btnSelect := widget.NewButton("Seleccionar", func() {
		onSelect(selected.Format("2006-01-02"))
		popup.Hide() // 🔥 cerrar correctamente
	})

	content := container.NewVBox(
		container.NewHBox(btnPrev, layout.NewSpacer(), btnNext),
		label,
		btnSelect,
	)

	popup = widget.NewModalPopUp(
		container.NewPadded(content),
		w.Canvas(),
	)
}
