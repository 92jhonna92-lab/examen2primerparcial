import validador
try:

    a=input("ingrese usuario")
    b=input("ingrese contraseña")
    if validador.admin(a,b):
        print("Acceso concedido")
    else:
        print("Acceso denegado")
except ValueError:
    print("Valor no valido")
