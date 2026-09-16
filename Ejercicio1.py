n=0
while n<=0:
    n=int(input("Ingrese numero entero: "))
    if n<=0:
        print("Error el numero debe ser mayor a 0")
a,b=0,1
resultado=[]
for _ in range(n):
    resultado.append(str(a))
    a,b=b,a+b
print("Los primero",n,"terminos son:")
print("-".join(resultado))