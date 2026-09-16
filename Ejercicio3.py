n=int(input("Ingrese numero del 1-10"))
if n<1 or n>10:
    print("Fuera de alcance")
else:
    for a in range(1,n+1):
        sumaX=0
        sumaY=0
        sumatotal=0
        for b in range(1,13):
            c=a*b
       
            print(f"{a} x {b}={c}")
            sumatotal+=c
    print(f"La suma total es: {sumatotal}")
