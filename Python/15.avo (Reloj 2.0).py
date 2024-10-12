import datetime
from tkinter import *

ventana = Tk()
ventana.geometry('350x150+1015+100')
ventana.configure(bg="gray")
ventana.wm_attributes("-transparentcolor", "gray")
ventana.overrideredirect(1)
def salir(*args):
    ventana.destroy()
    ventana.quit()

hora = Label(ventana, font=("Arial", 50, "bold"), fg="white", bg="gray")
hora.grid(row=0, column=0)

def actualizar_hora ():
    HoraActual = datetime.datetime.now()
    tiempo = datetime.datetime.strftime(HoraActual, "%X")
    hora.configure(text=tiempo)
    ventana.after(1000, actualizar_hora)



fecha = Label(ventana, font=("Arial", 20, "bold"), fg="white", bg="gray")
fecha.grid(row=1, column=0)

def actualizar_fecha ():
    FechaActual = datetime.datetime.now()
    tiempo = datetime.datetime.strftime(FechaActual, '%A' ' ' '%d' ' / ' '%m' ' / ' '%Y')
    fecha.configure(text=tiempo)
    ventana.after(1000, actualizar_fecha)

ventana.bind("<KeyPress-Escape>", salir)

actualizar_fecha()
actualizar_hora()
ventana.mainloop()