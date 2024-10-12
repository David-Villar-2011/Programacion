import datetime
from tkinter import *

def acutualizar_hora():
    tiempo = datetime.datetime.now()
    informacion = ("{:02d}:{:02d}:{:02d}".format(tiempo.hour,tiempo.minute,tiempo.second))
    texto.configure(text=informacion)
    ventana.after(1000, acutualizar_hora)

ventana = Tk()
ventana.geometry("545x180")
ventana.title("Reloj")

texto = Label(ventana, font=("Arial",100,"bold"))
texto.place(x=0, y=0)

acutualizar_hora()
ventana.mainloop()