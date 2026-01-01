package pantalla

import (
	controller "Gestor/interno/Api"
	funcion "Gestor/interno/Funcs"
	"Gestor/interno/Models"

	"fyne.io/fyne"
	"fyne.io/fyne/container"
	"fyne.io/fyne/dialog"
	"fyne.io/fyne/layout"
	"fyne.io/fyne/widget"
)

func Registro(w fyne.Window) {

	nombreUsuario := widget.NewEntry()
	nombreCompleto := widget.NewEntry()
	correo := widget.NewEntry()
	contraseña := widget.NewPasswordEntry()

	rol := widget.NewSelect(
		[]string{"Adm", "Usuario"},
		func(string) {},
	)

	// Título
	title := widget.NewLabelWithStyle(
		"REGISTRO DE USUARIO",
		fyne.TextAlignCenter,
		fyne.TextStyle{Bold: true},
	)

	section := widget.NewLabelWithStyle(
		"Datos personales",
		fyne.TextAlignLeading,
		fyne.TextStyle{Bold: true},
	)

	form := container.NewVBox(
		section,
		funcion.LabeledField("Usuario:", nombreUsuario),
		funcion.LabeledField("Nombre:", nombreCompleto),
		funcion.LabeledField("Correo electrónico:", correo),
		funcion.LabeledField("Contraseña:", contraseña),
		funcion.LabeledField("Rol:", rol),
	)

	// Botones
	btnRegistrar := widget.NewButton("REGISTRAR", func() {

		usuario := Models.Usuario{
			Nombre_Usuario:  nombreUsuario.Text,
			Nombre_Completo: nombreCompleto.Text,
			Correo:          correo.Text,
			Contraseña:      contraseña.Text,
			Rol:             rol.Selected,
		}

		err := controller.CrearUsuario(usuario)
		if err != nil {
			dialog.ShowError(err, w)
			return
		}
		d := dialog.NewInformation(
			"Éxito",
			"Usuario registrado correctamente",
			w,
		)

		d.SetOnClosed(func() {
			MostrarHome(w)
		})

	})

	btnLimpiar := widget.NewButton("LIMPIAR", func() {
		nombreUsuario.SetText("")
		nombreCompleto.SetText("")
		correo.SetText("")
		contraseña.SetText("")
		rol.ClearSelected()
	})
	btnCerrar := widget.NewButton("CERRAR", func() {
		funcion.MostrarHome(w)
	})

	buttons := container.NewHBox(
		layout.NewSpacer(),
		btnRegistrar,
		btnLimpiar,
		btnCerrar,
		layout.NewSpacer(),
	)

	// Contenido centrado tipo formulario
	content := container.NewVBox(
		title,
		widget.NewSeparator(),
		form,
		layout.NewSpacer(),
		buttons,
	)

	w.SetContent(
		container.NewCenter(
			container.NewPadded(content),
		),
	)

}
