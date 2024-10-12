from tkinter import *

def send_data():
    nombre_usuario_data = nombre_usuario.get()
    password_data = str(password.get())
    nombre_completo_data = nombre_completo.get()
    edad_data = str(edad.get())

    print(nombre_usuario_data, "\t", password_data, "\t", nombre_completo_data, "\t", edad_data)

    nuevo_archivo = open("Registro.xls", "a")
    nuevo_archivo.write(nombre_usuario_data)
    nuevo_archivo.write("\t")
    nuevo_archivo.write(password_data)
    nuevo_archivo.write("\t")
    nuevo_archivo.write(nombre_completo_data)
    nuevo_archivo.write("\t")
    nuevo_archivo.write(edad_data)
    nuevo_archivo.write("\n")
    nuevo_archivo.close()

    nombre_usuario_entry.delete(0,END)
    password_entry.delete(0,END)
    nombre_completo_entry.delete(0,END)
    edad_entry.delete(0,END)

ventana = Tk()
ventana.geometry("650x550")
ventana.title("Ventana de registro")
ventana.resizable(False,False)
ventana.config(background="#213141")
primer_titulo = Label(text="Foro de Registro", font=("Cambria", 13), bg="#56CD63", fg="white", width="550", height="2")
primer_titulo.pack()

nombre_usuario = Label(text="Nombre de Usuario", bg="#FFEEDD")
nombre_usuario.place(x=22 ,y=70)
password = Label(text="Contraseña", bg="#FFEEDD")
password.place(x=22 ,y=130)
nombre_completo = Label(text="Nombre Completo", bg="#FFEEDD")
nombre_completo.place(x=22 ,y=190)
edad = Label(text="Edad", bg="#FFEEDD")
edad.place(x=22 ,y=250)

nombre_usuario = StringVar()
password = StringVar()
nombre_completo = StringVar()
edad = StringVar()

nombre_usuario_entry = Entry(textvariable=nombre_usuario, width="40")
password_entry = Entry(textvariable=password, width="40", show="*")
nombre_completo_entry = Entry(textvariable=nombre_completo, width="40")
edad_entry = Entry(textvariable=edad, width="40")

nombre_usuario_entry.place(x=22, y=100)
password_entry.place(x=22, y=160)
nombre_completo_entry.place(x=22, y=220)
edad_entry.place(x=22, y=280)

enviar_boton = Button(ventana, text="Enviar información", command=send_data, width="30", height="2", bg="#00CD63")
enviar_boton.place(x=22, y=320)

ventana.mainloop()