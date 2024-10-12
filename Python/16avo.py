import tkinter as tk

# Configurar Ventana
ventana = tk.Tk()
ventana.wm_state("zoomed")
ventana.title("Batalla Narval")

frame =tk.Frame(ventana)
frame.place(relx=0.5, rely=1, anchor="s", y=-30)

def crar_tablero(frame):
    botones = []
    for fila in range(10):
        fila_botones = []
        for columna in range(10):
            boton = tk.Button(frame, width=5, height=2)
            boton.grid(row=fila, column=columna, padx=10, pady=10)
            fila_botones.append(boton)
        botones.append(fila_botones)
    return botones

tablero = crar_tablero(frame)
ventana.mainloop()