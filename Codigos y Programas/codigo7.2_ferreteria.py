stock_taller = {
    "martillo": 5,
    "destornillador": 7,
    "llave_inglesa": 3,
    "alicates": 4
}

for herramienta, cantidad in stock_taller.items():
    print(f"\n analizando stock de {herramienta}... cantidad disponible: {cantidad}")
    
    if cantidad < 5:
        print(f" ¡ALERTA! Comprar más {herramienta}. Quedan solo {cantidad}")
    elif cantidad >= 5:
        print(f" Stock de {herramienta} suficiente. No es necesario comprar.")