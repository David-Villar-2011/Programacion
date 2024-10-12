import random as rd
from time import sleep


print("Te haré una nueva contraseña:")
print("Loading...")
sleep(3)

print("Tu contraseña es...")
sleep(1)


# Variables
letrasMi = "abcdefghijklmnñopqrstuvwxy"
letrasMa = "ABCDEFGHIJKLMNÑOPQRSTUVWXYZ"
números = "1234567890"
símbolos = "!·$%&/?¿¡'|@#€*-_<>"

unidos = (f"{letrasMi} - {letrasMa} - {números} - {símbolos}")

contraseña = "".join(rd.sample(unidos, 10))
print(contraseña)

input()
