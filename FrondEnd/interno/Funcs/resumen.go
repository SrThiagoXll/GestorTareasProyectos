package funcion

import (
	"Gestor/interno/Models"
	"fmt"
	"image/color"
	"strings"

	"fyne.io/fyne/v2"
	"fyne.io/fyne/v2/container"
	"fyne.io/fyne/v2/widget"
)

var (
	lblTotalProyectos *widget.Label
	lblPendientes     *widget.Label
	lblFinalizados    *widget.Label
)

func CrearResumen() fyne.CanvasObject {
	lblTotalProyectos = widget.NewLabelWithStyle("0", fyne.TextAlignCenter, fyne.TextStyle{})
	lblPendientes = widget.NewLabelWithStyle("0", fyne.TextAlignCenter, fyne.TextStyle{})
	lblFinalizados = widget.NewLabelWithStyle("0", fyne.TextAlignCenter, fyne.TextStyle{})

	return container.NewGridWithColumns(
		3,
		crearCard("📁 Proyectos", lblTotalProyectos, color.NRGBA{202, 87, 107, 255}),
		crearCard("⏳ Pendientes", lblPendientes, color.NRGBA{167, 73, 75, 255}),
		crearCard("✔ Finalizados", lblFinalizados, color.NRGBA{99, 48, 53, 255}),
	)
}

func CalcularResumen(proyectos []Models.Proyecto) {
	total := len(proyectos)
	pendientes := 0
	finalizados := 0

	for _, p := range proyectos {
		switch strings.ToLower(p.Estado_Proyecto) {
		case "pendiente":
			pendientes++
		case "finalizado":
			finalizados++
		}
	}

	lblTotalProyectos.SetText(fmt.Sprintf("%d", total))
	lblPendientes.SetText(fmt.Sprintf("%d", pendientes))
	lblFinalizados.SetText(fmt.Sprintf("%d", finalizados))
}
