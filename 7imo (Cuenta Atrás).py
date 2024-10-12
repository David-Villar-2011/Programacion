from time import sleep
import winsound

tiempo = input("Cántos segundos quieres: ")
pitidos = input("Cuántos pitidos quieres: ")

for i in range(int(tiempo), 0 , -1):
    print(i)
    sleep(1)
for i in range(int(pitidos)):
    frequency = 10000
    duration = 1000
    winsound.Beep(frequency, duration)
    sleep(0.5)

input()