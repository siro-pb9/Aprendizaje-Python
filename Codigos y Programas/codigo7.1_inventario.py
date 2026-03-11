stock = {
    "tornillos": 100,
    "capacitores": 50,
    "soldadores": 2,
}

print(f"Stock inicial de capacitores: {stock['capacitores']} unidades")

#viene cliente y compra 10 capacitores

stock["capacitores"] = stock["capacitores"] - 10

#compra de multimetro

stock["multimetros"] = 1

print("\n--- ACTUALIZACIÓN DE STOCK ---")
print(stock)