temperatura_cpu = int(input("Ingrese la temperatura actual de la CPU en °C: "))

if temperatura_cpu > 90:
    print("PELIGRO: Temperatura crítica. Apagando sistema...")
elif temperatura_cpu > 75:
    print("Advertencia: Fan al 100% (Está calenta pero aguanta)")
else:
    print("Sistema operando en parámetros normales.")