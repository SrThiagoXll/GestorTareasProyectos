package funcion

import (
	"image/color"

	"fyne.io/fyne/v2"
	"fyne.io/fyne/v2/canvas"
	"fyne.io/fyne/v2/container"
	"fyne.io/fyne/v2/widget"
)

func crearCard(titulo string, valor *widget.Label, bgColor color.Color) fyne.CanvasObject {
	bg := canvas.NewRectangle(bgColor)
	bg.SetMinSize(fyne.NewSize(160, 90))

	contenido := container.NewVBox(
		widget.NewLabelWithStyle(
			titulo,
			fyne.TextAlignCenter,
			fyne.TextStyle{Bold: true},
		),
		valor,
	)

	return container.NewStack(
		bg,
		container.NewCenter(contenido),
	)
}
