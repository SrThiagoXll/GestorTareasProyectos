package pantalla

import (
	funcion "Gestor/interno/Funcs"

	"fyne.io/fyne"
	"fyne.io/fyne/container"
	"fyne.io/fyne/layout"
	"fyne.io/fyne/widget"
)

func MostrarLogin(w fyne.Window) {

	usuario := widget.NewEntry()
	contraseña := widget.NewPasswordEntry()

	form := container.NewVBox(
		widget.NewLabelWithStyle("Login", fyne.TextAlignCenter, fyne.TextStyle{Bold: true}),
		widget.NewSeparator(),

		funcion.LabeledField("Usuario", usuario),
		funcion.LabeledField("Contraseña", contraseña),

		layout.NewSpacer(),

		widget.NewButton("Ingresar", func() {
			// Aquí validas login con la API
		}),
	)

	w.SetContent(container.NewCenter(container.NewPadded(form)))
}
