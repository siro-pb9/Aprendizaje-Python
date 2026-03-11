# 1. CREACIÓN (El Mapeo Inicial)
# A diferencia de las listas [] que usan números (0, 1, 2...),
# los diccionarios {} usan "CLAVES" (Etiquetas) para guardar valores.
sensores_auto = {
    "RPM": 1500,              # Clave: "RPM" -> Valor: 1500
    "Temperatura_Agua": 90,   # Clave: "Temperatura_Agua" -> Valor: 90
    "Litros_Nafta": 45,       # Clave: "Litros_Nafta" -> Valor: 45
    "Luces_Prendidas": False  # También guarda Booleanos
}

print("--- LECTURA INICIAL DE SENSORES ---")
# Imprimimos todo el paquete junto para ver qué hay
print(sensores_auto)
print("-" * 30)


# 2. LECTURA PUNTUAL (Consultar un dato específico)
# Queremos saber SOLO la nafta.
# En una lista sería: lista[2]. Acá es directo por nombre:
nivel_actual = sensores_auto["Litros_Nafta"]

print(f"Combustible actual: {nivel_actual} Litros")


# 3. ACTUALIZACIÓN (Modificar un valor existente)
# El auto avanzó y consumió 5 litros.
# Lógica: Valor Nuevo = Valor Viejo - 5
sensores_auto["Litros_Nafta"] = sensores_auto["Litros_Nafta"] - 5

print(f"¡Consumo detectado! Nafta restante: {sensores_auto['Litros_Nafta']} Litros")


# 4. AGREGADO (Meter un dato nuevo al sistema)
# Le instalamos un Turbo al auto. Esa clave NO existía antes.
# Python detecta que es nueva y la crea.
sensores_auto["Presion_Turbo"] = 1.2  # BARs

print("\n--- ACTUALIZACIÓN DE HARDWARE ---")
print("Se detectó nuevo sensor: Turbo")
print(sensores_auto) # Fijate que ahora aparece al final