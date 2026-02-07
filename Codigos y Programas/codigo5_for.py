juegos = ["minecraft", "fortnite", "warzone", "GTA V"]

for juego in juegos:
    if juego == "warzone" or juego == "GTA V":
        print(f"Ajustando gráficos a MEDIO de {juego} para mantener 60 FPS")
    else:
        print(f"Configuración ULTRA aplicada para {juego}")
print("Optimización completa.")