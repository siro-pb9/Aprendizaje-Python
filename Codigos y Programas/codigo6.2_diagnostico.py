def diagnostico_cpu(temp):
    if temp < 50:
        return "Temperatura normal"
    elif temp >= 50 and temp < 80:
        return "precaucion"
    elif temp >= 80 and temp <= 100:
        return "Peligro"
    else:
        return "numero no valido, ingrese un numero entre 0 y 100"

while True:
    grados = int(input("Temperatura del CPU en grados Celsius: "))

    if grados == 0:
        print("Saliendo del programa...")
        break

    diagnostico = diagnostico_cpu(grados)
    print(f"Estado actual {diagnostico}")
