def diagnostico_cpu(temp):
    if temp < 50:
        return "Temperatura normal"
    elif temp >= 50 and temp < 80:
        return "precaucion"
    elif temp >= 80 and temp <= 100:
        return "Peligro"
    elif temp == 0:
        return "maquina apagada"
    else:
        return "numero no valido, ingrese un numero entre 0 y 100"


temperaturas = [45, 60, 30, 95, 75, 82, 55]
while True:
    for temperatura in temperaturas:
        diagnostico = diagnostico_cpu(temperatura)
        print(f"Maquina X: {temperatura}°C --> {diagnostico}")
    break