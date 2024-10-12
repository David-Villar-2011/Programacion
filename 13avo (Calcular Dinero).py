print("Vamos a calcular el dinero que tienes.")
print("Responde las siguientes preguntas: ")

mon_1_cts = input("Cuántas monedas de 1cts tienes: ") or "0"
mon_2_cts = input("Cuántas monedas de 2cts tienes: ") or "0"
mon_5_cts = input("Cuántas monedas de 5cts tienes: ") or "0"
mon_10_cts = input("Cuántas monedas de 10cts tienes: ") or "0"
mon_20_cts = input("Cuántas monedas de 20cts tienes: ") or "0"
mon_50_cts = input("Cuántas monedas de 50cts tienes: ") or "0"
mon_1_euro = input("Cuántas monedas de 1€ tienes: ") or "0"
mon_2_euro = input("Cuántas monedas de 2€ tienes: ") or "0"
billete_5 = input("Cuántos billetes de 5€ tienes: ") or "0"
billete_10 = input("Cuántos billetes de 10€ tienes: ") or "0"
billete_20 = input("Cuántos billetes de 20€ tienes: ") or "0"
billete_50 = input("Cuántos billetes de 50€ tienes: ") or "0"
billete_100 = input("Cuántos billetes de 100€ tienes: ") or "0"
billete_200 = input("Cuántos billetes de 200€ tienes: ") or "0"

mon_1_cts = float(mon_1_cts) * 0.01
mon_2_cts = float(mon_2_cts) * 0.02
mon_5_cts = float(mon_5_cts) * 0.05
mon_10_cts = float(mon_10_cts) * 0.1
mon_20_cts = float(mon_20_cts) * 0.2
mon_50_cts = float(mon_50_cts) * 0.5
mon_1_euro = float(mon_1_euro) * 1.0
mon_2_euro = float(mon_2_euro) * 2.0
billete_5 = float(billete_5) * 5.0
billete_10 = float(billete_10) * 10.0
billete_20 = float(billete_20) * 20.0
billete_50 = float(billete_50) * 50.0
billete_100 = float(billete_100) * 100.0
billete_200 = float(billete_200) * 200.0

total = (
    mon_1_cts
    + mon_2_cts
    + mon_5_cts
    + mon_10_cts
    + mon_20_cts
    + mon_50_cts
    + mon_1_euro
    + mon_2_euro
    + billete_5
    + billete_10
    + billete_20
    + billete_50
    + billete_100
    + billete_200
)


total = (
    mon_1_cts
    + mon_2_cts
    + mon_5_cts
    + mon_10_cts
    + mon_20_cts
    + mon_50_cts
    + mon_1_euro
    + mon_2_euro
)

if total > 1.0 or total == 0.0:
    print("Tienes " + str(total) + "€")

elif total < 1.0 and total > 0.0:
    total = total * 100
    total = int(total)
    print("Tienes " + str(total) + " céntimos")

input()