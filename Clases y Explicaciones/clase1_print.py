# Esto es un comentario. El intérprete lo ignora, es para nosotros los humanos.

# 1. Asignamos valores a variables (Guardamos datos en RAM)
usuario = "Siro"          # Esto es un String (Texto)
edad = 18                 # Esto es un Integer (Número entero)
tiene_gpu = True          # Esto es un Boolean (Verdadero/Falso - 1 o 0)

# 2. Mostramos los datos en pantalla (Output)
print("--- Sistema Iniciado ---")
print(f"Usuario detectado: {usuario}")
print(f"Edad del operario: {edad}")
print(f"¿Estado de GPU operativa?: {tiene_gpu}")

# 3. Hacemos un cálculo simple en el momento
anio_nacimiento = 2026 - edad
print(f"Año estimado de fabricación del usuario: {anio_nacimiento}")