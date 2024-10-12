from tkinter import *
from math import *

# VISUALIZAR LA OPERACION EN LA PANTALLA


def btnClik(num):
    global operador
    operador = operador+str(num)
    input_text.set(operador)

# CÁLCULO Y MUESTRA DE RESULTADOS.


def resultado():
    global operador
    try:
        opera = str(eval(operador))
        input_text.set(opera)
    except:
        input_text.set("ERROR")
    operador = ""

# LIMPIEZA DE PANTALLA.


def clear():
    global operador
    operador = ("")
    input_text.set("0")


ventana = Tk()
ventana.title("CALCULADORA")
ventana.geometry("392x600")
ventana.configure(background="goldenrod1")
color_boton = ("DarkOrange1")

ancho_boton = 11
alto_boton = 3
input_text = StringVar()
operador = ""

Salida = Entry(ventana, font=('arial', 20, 'bold'), width=22,
               textvariable=input_text, bd=20, insertwidth=4, bg="DarkOrange1", justify="right")
Salida.grid(row=0, column=0, columnspan=4, padx=10, pady=20)

# AÑADIR BOTONES.
# CREAMOS NUESTROS BOTONES
Button(ventana, text="0", bg=color_boton, width=ancho_boton, height=alto_boton,
       command=lambda: btnClik(0)).grid(row=1, column=0, pady=20)
Button(ventana, text="1", bg=color_boton, width=ancho_boton, height=alto_boton,
       command=lambda: btnClik(1)).grid(row=1, column=1, pady=20)
Button(ventana, text="2", bg=color_boton, width=ancho_boton, height=alto_boton,
       command=lambda: btnClik(2)).grid(row=1, column=2, pady=20)
Button(ventana, text="3", bg=color_boton, width=ancho_boton, height=alto_boton,
       command=lambda: btnClik(3)).grid(row=1, column=3, pady=20)

Button(ventana, text="4", bg=color_boton, width=ancho_boton, height=alto_boton,
       command=lambda: btnClik(4)).grid(row=2, column=0, pady=20)
Button(ventana, text="5", bg=color_boton, width=ancho_boton, height=alto_boton,
       command=lambda: btnClik(5)).grid(row=2, column=1, pady=20)
Button(ventana, text="6", bg=color_boton, width=ancho_boton, height=alto_boton,
       command=lambda: btnClik(6)).grid(row=2, column=2, pady=20)
Button(ventana, text="7", bg=color_boton, width=ancho_boton, height=alto_boton,
       command=lambda: btnClik(7)).grid(row=2, column=3, pady=20)

Button(ventana, text="8", bg=color_boton, width=ancho_boton, height=alto_boton,
       command=lambda: btnClik(8)).grid(row=3, column=0, pady=20)
Button(ventana, text="9", bg=color_boton, width=ancho_boton, height=alto_boton,
       command=lambda: btnClik(9)).grid(row=3, column=1, pady=20)
Button(ventana, text="=", bg=color_boton, width=25, height=alto_boton,
       command=resultado).grid(row=3, column=2, pady=20, columnspan=2)

Button(ventana, text="+", bg=color_boton, width=ancho_boton, height=alto_boton,
       command=lambda: btnClik("+")).grid(row=4, column=0, pady=20)
Button(ventana, text="-", bg=color_boton, width=ancho_boton, height=alto_boton,
       command=lambda: btnClik("-")).grid(row=4, column=1, pady=20)
Button(ventana, text="×", bg=color_boton, width=ancho_boton, height=alto_boton,
       command=lambda: btnClik("*")).grid(row=4, column=2, pady=20)
Button(ventana, text="÷", bg=color_boton, width=ancho_boton, height=alto_boton,
       command=lambda: btnClik("/")).grid(row=4, column=3, pady=20)

Button(ventana, text="C", bg="red1", width=ancho_boton,
       height=alto_boton, command=clear).grid(row=5, column=3, pady=20)

clear()

ventana.mainloop()
