# Pedimos datos al usuario
# La ejecución se frena acá hasta que escribas y des Enter
nombre_pc = input("Ingrese el nombre para este equipo: ")

# Definimos el hardware (Hardcoded por ahora)
cpu = "Ryzen 7 5700"
gpu = "RTX 3080 TI"  # ¡Alta placa, por cierto!
ram = "32 GB (2x16 GB) DDR4 3200 MHz"
mother = "Asus ROG Strix B550-F"

print("--- Especificaciones del Sistema ---")
# Usamos la variable que ingresó el usuario
print(f"Hostname: {nombre_pc}")
print(f"Procesador: {cpu}")
print(f"Tarjeta Gráfica: {gpu}")
print(f"Memoria RAM: {ram}")
print(f"Placa Madre: {mother}")