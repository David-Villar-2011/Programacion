from tkinter import *
from tkinter import ttk

# Crear ventana principal
ventana = Tk()
ventana.title("Calculadora")
ventana.geometry("392x600")

# Variable para mostrar el resultado en la pantalla
input_text = StringVar()

# Crear la pantalla para mostrar los resultados
Pantalla = Entry(ventana, textvariable=input_text, justify="right", font=("Arial", 25, "bold"))
Pantalla.grid(row=0, column=0, columnspan=4, padx=10, pady=20)

# Función para actualizar el valor de la pantalla cuando se presiona un botón
def AñadirNumero(num):
    IntroducirTexto = input_text.get()
    input_text.set(IntroducirTexto + str(num))

def CalcularResultado():
    try:
        resultado = eval(input_text.get())
        input_text.set(resultado)
    except Exception as e:
        input_text.set("Error")

def AñadirOperador(operador):
    IntroducirTexto = input_text.get()
    input_text.set(IntroducirTexto + operador)

def BorrarTodo():
    input_text.set("")

# Crear los botones numericos
Boton1 = ttk.Button(ventana, text="1", command=lambda: AñadirNumero(1), padding=10)
Boton1.grid(row=1, column=0, padx=10, pady=10)

Boton2 = ttk.Button(ventana, text="2", command=lambda: AñadirNumero(2), padding=10)
Boton2.grid(row=1, column=1, padx=10, pady=10)

Boton3 = ttk.Button(ventana, text="3", command=lambda: AñadirNumero(3), padding=10)
Boton3.grid(row=1, column=2, padx=10, pady=10)

Boton4 = ttk.Button(ventana, text="4", command=lambda: AñadirNumero(4), padding=10)
Boton4.grid(row=2, column=0, padx=10, pady=10)

Boton5 = ttk.Button(ventana, text="5", command=lambda: AñadirNumero(5), padding=10)
Boton5.grid(row=2, column=1, padx=10, pady=10)

Boton6 = ttk.Button(ventana, text="6", command=lambda: AñadirNumero(6), padding=10)
Boton6.grid(row=2, column=2, padx=10, pady=10)

Boton7 = ttk.Button(ventana, text="7", command=lambda: AñadirNumero(7), padding=10)
Boton7.grid(row=3, column=0, padx=10, pady=10)

Boton8 = ttk.Button(ventana, text="8", command=lambda: AñadirNumero(8), padding=10)
Boton8.grid(row=3, column=1, padx=10, pady=10)

Boton9 = ttk.Button(ventana, text="9", command=lambda: AñadirNumero(9), padding=10)
Boton9.grid(row=3, column=2, padx=10, pady=10)

Boton0 = ttk.Button(ventana, text="0", command=lambda: AñadirNumero(0), padding=10)
Boton0.grid(row=4, column=0, padx=10, pady=10)

# Crear boton especial
BotonIgual = ttk.Button(ventana, text="=", command=CalcularResultado, padding=10, width=32)
BotonIgual.grid(row=4, column=1, columnspan=2)

# Crear botones de operaciones
BotonSuma = ttk.Button(ventana, text="+", command=lambda: AñadirOperador("+"), padding=10, width=22)
BotonSuma.place(y=350, x=15)

BotonResta = ttk.Button(ventana, text="-", command=lambda: AñadirOperador("-"), padding=10, width=22)
BotonResta.place(y=350, x=200)

BotonMultiplicacion = ttk.Button(ventana, text="×", command=lambda: AñadirOperador("*"), padding=10, width=22)
BotonMultiplicacion.place(y=410, x=15)

BotonDivision = ttk.Button(ventana, text="÷", command=lambda: AñadirOperador("/"), padding=10, width=22)
BotonDivision.place(y=410, x=200)

BotonCA = ttk.Button(ventana, text="CA", command=lambda: BorrarTodo(), padding=10, width=53)
BotonCA.place(y=480, x=15)

ventana.mainloop()
