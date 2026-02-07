def calcular_promedio(fps_max, fps_min, fps_act):
    fps_suma = fps_max + fps_min + fps_act
    fps_prom = fps_suma / 3
    return fps_prom

fps_max =int(input("Ingrese el valor de fps_max: "))
fps_min =int(input("Ingrese el valor de fps_min: "))
fps_act =int(input("Ingrese el valor de fps_act: "))

fps_promedio = calcular_promedio(fps_max, fps_min, fps_act)

print(f"el promedio de FPS es: {fps_promedio:.2f} FPS")