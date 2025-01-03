from tkinter import *
import datetime

Ventana = Tk()
Ventana.wm_attributes("-transparentcolor", "Gray")
Ventana.overrideredirect(1)

Hora = Label(Ventana, font=("Arial", 50, "bold"), fg="white", bg="gray")
Hora.grid(row=0, column=0)

def ActualizarHora():
    HoraActual = datetime.datetime.now()
    Tiempo = datetime.datetime.strftime(HoraActual, "%X")
    Hora.configure(text=Tiempo)
    Ventana.after(1000, ActualizarHora)

    Segundos = HoraActual.second

    if Segundos == 0:
        Hora = Label(Ventana, font=("Arial", 50, "bold"), fg="Green", bg="gray")
        Hora.grid(row=0, column=0)

ActualizarHora()
Ventana.mainloop()