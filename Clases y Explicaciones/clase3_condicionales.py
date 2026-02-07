# Datos de entrada
consumo_total = int(input("Ingresá el consumo total de la PC (Watts): "))
fuente_watts = int(input("¿De cuántos Watts es tu fuente?: "))

print("--- Analizando ---")

# Acá arranca la decisión
if fuente_watts >= consumo_total:
    # Fíjate que esta línea tiene un espacio (tabulación) a la izquierda
    print("Todo OK: La fuente banca el sistema.")
    print("Podés jugar tranquilo.")
else:
    # Esto se ejecuta SI NO se cumple la condición de arriba
    print("ALERTA: La fuente es muy chica.")
    print(f"Te faltan {consumo_total - fuente_watts} Watts para arrancar.")

# Esta línea no tiene tabulación, así que se ejecuta SIEMPRE, pase lo que pase
print("--- Fin del análisis ---")