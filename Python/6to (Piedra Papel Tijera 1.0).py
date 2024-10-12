from time import sleep
import random

print("===================================================================")
print("                    PIEDRA PAPEL O TIJERA 0.1")
print("===================================================================")

print("1) Piedra")
print("2) Papel")
print("3) Tijera")
selección = input("Que desea sacar: ")

selección_comutadora = random.randint(1,3)
selección_comutadora = str(selección_comutadora)

def quien_gana ():
    if selección_comutadora == str(1) and selección == str(1):
        print("Empate 😐 ")
    elif selección_comutadora == str(2) and selección == str(2):
        print("Empate 😐 ")
    elif selección_comutadora == str(3) and selección == str(3):
        print("Empate 😐 ")
    elif selección_comutadora == str(1) and selección == str(2):
        print("Enorabuena ganaste!!! 🙂 ")
    elif selección_comutadora == str(1) and selección == str(3):
        print("Gana la computadora. ☹️ ")
    elif selección_comutadora == str(2) and selección == str(1):
        print("Gana la computadora. ☹️ ")
    elif selección_comutadora == str(2) and selección == str(3):
        print("Enorabuena ganaste !!! 🙂 ")
    elif selección_comutadora == str(3) and selección == str(1):
        print("Enorabuena ganaste!!! 🙂 ")
    else:
        print("Gano la computadora. ☹️ ")

quien_gana()

sleep(10)