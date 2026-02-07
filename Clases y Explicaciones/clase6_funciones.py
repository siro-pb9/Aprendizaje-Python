# 1. DEFINIMOS la herramienta (La fabricamos)
def gb_a_tb(gigabytes):
    # 1024 GB es 1 TB
    terabytes = gigabytes / 1024
    return terabytes  # Devolvemos el valor procesado, osea: el codigo nos va a mostrar el resultado de la division, osea: el valor en TB

# -----------------------------------------------
# 2. USAMOS la herramienta (La sacamos de la caja)

disco1 = 500  # GB
disco2 = 2000 # GB

# 3. Llamamos a la función y guardamos el resultado
tb_disco1 = gb_a_tb(disco1)
tb_disco2 = gb_a_tb(disco2)

print(f"Disco 1: {disco1} GB son {tb_disco1:.2f} TB")
print(f"Disco 2: {disco2} GB son {tb_disco2:.2f} TB")