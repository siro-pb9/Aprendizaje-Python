import time

contraseña_real = "admin1234"
se_introdujo_contraseña = False

while se_introdujo_contraseña == False:
    print("Por favor, Introduzca su contraseña.")
    time.sleep(2) 
    contraseña_introducida = input("Introduce la contraseña: ")
    if contraseña_introducida == contraseña_real:
        se_introdujo_contraseña = True
    elif contraseña_introducida != contraseña_real:
        print(f"la contraseña {contraseña_introducida} es Incorrecta. Inténtelo de nuevo.")
        
 
print("Acceso Concedido. Bienvenido al Sistema")