import tkinter as tk
from tkinter import ttk
import subprocess

# Crear y configurar ventana principal básica
ventana = tk.Tk()
ventana.geometry("550x250+400+200")
ventana.title("Organizador")

# Guardar la referencia a la imagen de fondo (debe ser un archivo .png que tkinter pueda manejar)
imagen_fondo = tk.PhotoImage(file="C:\\Users\\david\\OneDrive\\Documents\\GitHub\\Programacion\\Python\\Organizador\\ventana.png")

# Crear el fondo y asignarle la imagen
fondo = tk.Label(ventana, image=imagen_fondo)
fondo.place(relwidth=1, relheight=1)

# Imagenes de los botones
imagen1 = tk.PhotoImage(file="C:\\Users\\david\\OneDrive\\Documents\\GitHub\\Programacion\\Python\\Organizador\\logo1.png")
imagen2 = tk.PhotoImage(file="C:\\Users\\david\\OneDrive\\Documents\\GitHub\\Programacion\\Python\\Organizador\\logo2.png")
imagen3 = tk.PhotoImage(file="C:\\Users\\david\\OneDrive\\Documents\\GitHub\\Programacion\\Python\\Organizador\\logo3.png")

# Funciones para abrir aplicaciones
def abrir_calculadora():
    subprocess.Popen(["calc.exe"])

def abrir_reloj():
    subprocess.Popen(["start", "ms-clock:"], shell=True)

def abrir_edge():
    subprocess.Popen(["start", "msedge"], shell=True)

# Crear los botones
Boton1 = ttk.Button(ventana, image=imagen1, command=abrir_calculadora)
Boton1.place(x=50, y=50)

Boton2 = ttk.Button(ventana, image=imagen2, command=abrir_reloj)
Boton2.place(x=200, y=50)

Boton3 = ttk.Button(ventana, image=imagen3, command=abrir_edge)
Boton3.place(x=350, y=50)

ventana.mainloop()