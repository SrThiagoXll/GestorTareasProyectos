package pantalla

import (
	funcion "Gestor/interno/Funcs"

	"fyne.io/fyne/v2"
	"fyne.io/fyne/v2/container"
	"fyne.io/fyne/v2/dialog"
	"fyne.io/fyne/v2/layout"
	"fyne.io/fyne/v2/widget"
)

func MostrarLogin(w fyne.Window) {

	usuario := widget.NewEntry()
	contraseña := widget.NewPasswordEntry()

	btnLogin := widget.NewButton("Ingresar", func() {
		if usuario.Text == "" {
			dialog.ShowInformation("Error", "Ingrese usuario", w)
			return
		}

		PantallaInicio(w, usuario.Text)
	})

	form := container.NewVBox(
		widget.NewLabelWithStyle("Login", fyne.TextAlignCenter, fyne.TextStyle{Bold: true}),
		widget.NewSeparator(),
		funcion.LabeledField("Usuario", usuario),
		funcion.LabeledField("Contraseña", contraseña),
		layout.NewSpacer(),
		btnLogin,
	)

	w.SetContent(container.NewCenter(container.NewPadded(form)))
}
