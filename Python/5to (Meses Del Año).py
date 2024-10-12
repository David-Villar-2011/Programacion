mes = input("Introduce un mes del año: ")

if mes == "Enero":
    print("31 días")
elif mes == "Febrero":
    bisiesto = input("Es año bisiesto: ")
    if bisiesto == "Sí":
        print("29 días ")
    else:
        print("28 días ")
elif mes == "Marzo":
    print("31 días")
elif mes == "Abril":
    print("30 días")
elif mes == "Mayo":
    print("31 días")
elif mes == "Junio":
    print("30 días")
elif mes == "Julio":
    print("31 días")
elif mes == "Agosto":
    print("31 días")
elif mes == "Septiembre":
    print("30 días")
elif mes == "Octubre":
    print("31 días")
elif mes == "Noviembre":
    print("30 días")
elif mes == "Diciembre":
    print("31 días")
else:
    print("Mes desconocido.")

input()