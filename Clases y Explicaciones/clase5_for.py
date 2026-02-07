# Definimos una lista (como una caja de herramientas)
componentes = ["Procesador", "Placa de Video", "Memoria RAM", "Disco M.2"]

print("--- Iniciando Inventario ---")

# EL BUCLE FOR
# Traducción: "Para cada 'item' que encuentres EN 'componentes'..."
for componente in componentes:
    print(f"Revisando: {componente}")
    print("Estado: OK")
    print("-" * 10) # Separador facha

print("Inventario finalizado.")

# Esto cuenta del 0 al 4 (El límite superior nunca se incluye en Python)
for numero in range(5):
    print(f"Contando: {numero}")

     # Ejemplo 1: Pares (Saltando de 2 en 2)
#    "Arranca en 0, cortá en 10, saltá de a 2"
#print("Pares:")
#for i in range(0, 10, 2):
#    print(i) 
#   Salida: 0, 2, 4, 6, 8

#    Ejemplo 2: Cuenta Regresiva (Paso Negativo)
#   "Arranca en 10, cortá en 0, restá 1"
#print("\nDespegue:")
#for i in range(10, 0, -1):
#    print(i)
#   Salida: 10, 9, 8... hasta 1