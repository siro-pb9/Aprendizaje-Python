consumo_cpu = int(input("Consumo de CPU en watts: "))
consumo_gpu = int(input("Consumo de GPU en watts: "))
total_watts = consumo_cpu + consumo_gpu

print(f"El consumo total estimado es: {total_watts} Watts")