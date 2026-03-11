'''En este codido se aplica TODO lo que se vio en las anteriores calses, es por eso que este codigo va a tener anotaciones
en cada fragmento, para que puedas entender como se aplican las herramientas vistas en cada clase.'''



nombres = ["Servidor A", "Servidor B", "Servidor C", "Servidor D", "Servidor E", "Servidor F", "Servidor G", "Servidor H"] # Lista de nombres de servidores
pings = [23,     14,     250,   400,    12,     60,     310,    8] # Lista de pings correspondientes a cada servidor. El orden es importante, el primer ping corresponde al Servidor A, el segundo ping corresponde al servidor B y así sucesivamente.

def clasificar_ping(ms): # Esta función recibe un valor de ping en milisegundos y lo califica segun su valor. 
    if ms < 50: # Si el ping es menor a 50 ms, se considera "Excelente"
        return "Excelente"
    elif ms >= 50 and ms < 200: # Si el ping está entre 50 ms y 200 ms, se considera "Bueno"
        return "Bueno"
    elif ms >= 200: # Si el ping es mayor o igual a 200 ms, se considera "LAG"
        return "LAG"

def calcular_promedio(datos): # Esta función recibe una lista de datos y calcula su promedio. 
    cantidad = len(datos) # Primero calcula la cantidad de datos usando len(), la funcion "len()" sirve para contar la cantidad de elementos que hay en una lista. 
    suma = sum(datos) # Luego calcula la suma de los datos usando sum(), la función "sum()" sirve para sumar todos los elementos de una lista.         
    return suma / cantidad # Finalmente, devuelve el resultado de dividir la suma por la cantidad, lo que nos da el promedio.

for nombre, ping in zip(nombres, pings): # Este bucle recorre cada nombre y ping simultáneamente usando zip(). Zip empareja elementos de dos listas en tuplas.
    clasificar = clasificar_ping(ping) # Para cada ping, se llama a la función "clasificar_ping" y se guarda el resultado en la variable "clasificar". Esto nos da la clasificación del ping actual (por ejemplo, "Excelente", "Bueno" o "LAG").
    print(f"{nombre} - Estado: {clasificar}") # Luego, se imprime el nombre del servidor y su estado usando un f-string para mostrar ambos datos obtenidos.

print(f"El ping promedio es: {calcular_promedio(pings)} ms") # Finalmente, se imprime el ping promedio calculado por la función "calcular_promedio". Esto nos da una idea general del rendimiento de la red en base a los pings registrados.

'''En este código se aplican herramientas vistas en las clases anteriores, como funciones, listas, bucles y condicionales,
 para crear un programa que monitorea el estado de una red a través de los pings de varios servidores.
 Cada ping se clasifica según su valor, y al final se calcula e imprime el ping promedio.
 Es importante que en la funcion "def calcular_promedios(datos):" no se use algo como "suma = sum(pings)"
 ¿Por qué? Porque si mañana tenés otra lista llamada "pings_backup", "Temperatura", "Velocidad" o lo que sea, 
 tu función vieja no serviría (porque estaba "atada" a la variable pings). En cambio, al usar "datos" como parámetro,
   tu función es más flexible y puede trabajar con cualquier lista que le pases, no solo con la lista de pings.'''

'''ademas se usa una funcion nueva en este código, que es "zip()". 
Zip es una función que toma dos o más listas y las combina en una sola lista de tuplas.
EJEMPLO TEORICO:
lista1 = [1, 2, 3]
lista2 = ['a', 'b', 'c']
combinada = zip(lista1, lista2)
print(list(combinada)) # Esto imprimiría: [(1, 'a'), (2, 'b'), (3, 'c')]
En este ejemplo, zip toma el primer elemento de lista1 (1) y el primer elemento de lista2 ('a') y los combina en una tupla (1, 'a').'''
