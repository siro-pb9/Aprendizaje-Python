# --- CLASE 8: ITERAR DICCIONARIOS ---

# 1. Tenemos nuestro diccionario (Placa madre y sus voltajes esperados)
voltajes_mother = {
    "VCC_CORE": 1.2,
    "RAM_VDD": 1.35,
    "STANDBY_5V": 5.0,
    "CHIPSET": 1.05
}

print("--- INICIANDO DIAGNÓSTICO DE PUNTOS DE MEDICIÓN ---")

# 2. EL BUCLE FOR CON .items()
# Fíjate que ahora inventamos DOS variables temporales separadas por coma:
# 'punto' va a guardar el nombre (la clave)
# 'medicion' va a guardar el número (el valor)

for punto, medicion in voltajes_mother.items():
    
    # Adentro del bucle podemos hacer lo que queramos con esos dos datos
    # Por ejemplo, imprimirlos prolijamente:
    print(f"Testeando {punto}... Lectura: {medicion}V")
    
    # 3. COMBINANDO CON LÓGICA (If/Else)
    # Vamos a hacer que el sistema nos avise si un voltaje es muy alto
    if medicion >= 5.0:
        print(f"  -> [ADVERTENCIA] El riel {punto} maneja alta tensión.")
    else:
        print(f"  -> [OK] Tensión de {punto} en parámetros seguros.")

print("\n--- DIAGNÓSTICO FINALIZADO ---")