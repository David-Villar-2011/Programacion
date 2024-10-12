def Jugar():

    import random

    # Variables
    NumUsuario = None
    NumOrdenador = random.randint(0, 10)
    Intentos = 10

    # Bienvenida
    print("ADIVINA EL NÚMERO:")
    print("Hola, estoy pensando en un número al azar del 0 al 10, intenta adivinarlo")

    while Intentos > 0:
        try:
            NumUsuario = int(input("Introduce un número: "))
            
            if NumUsuario == NumOrdenador:
                print("¡Felicidades! Has acertado.")
                VolverJugar()

            elif NumUsuario < NumOrdenador:
                Intentos = Intentos-1

                print(f"El número es demasiado bajo. Te quedan {Intentos} intentos.")
            else:
                Intentos = Intentos-1
            
                print(f"El número es demasiado alto. Te quedan {Intentos} intentos.")
        except ValueError:
            print("Por favor, introduce un número válido.")
        
        if Intentos == 0:
            print(f"Lo siento, se te acabaron los intentos. El número era {NumOrdenador}.")
            VolverJugar()

def VolverJugar():
    Volver_Jugar = input("Quieres volver a jugar (Y/N): ")

    if Volver_Jugar == ("Y") or Volver_Jugar == ("y"):
        return Jugar()
    
    elif Volver_Jugar == ("N") or Volver_Jugar == ("n"):
        exit()

    else:
        print("Los siento no te he entendido.")
        return VolverJugar()

Jugar()