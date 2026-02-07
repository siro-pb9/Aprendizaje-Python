import time # Importamos una librería para manejar tiempo (pausas)

contador = 5

print("Iniciando secuencia de despegue...")

# Mientras contador sea mayor a 0, repetimos
while contador > 0:
    print(f"T-Restante: {contador}")
    contador = contador - 1  # RESTAMOS 1. Esto es CLAVE para que el bucle no sea infinito
    time.sleep(1) # Esperamos 1 segundo para darle drama

print("¡Despegue!")