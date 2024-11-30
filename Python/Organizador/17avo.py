import tkinter as tk
from tkinter import ttk

# Crear y configurar ventana principal básica
ventana = tk.Tk()
ventana.geometry("550x250+400+200")
ventana.title("Organizador")

# Imagenes
imagen1 = tk.PhotoImage(file="C:\\Users\\david\\OneDrive\\Documents\\GitHub\\Programacion\\Python\\Organizador\\logo1.png")

# Crear otras ventanas
    # None

# Crear botones
Boton1 = ttk.Button(ventana, image=imagen1)
Boton1.place(x=50, y=50)

Boton2 = ttk.Button(ventana)
Boton2.place(x=200, y=50)

ventana.mainloop()