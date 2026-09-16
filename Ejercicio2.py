##control parqueo
print("Parqueo tarifado")
try:

    op=int(input("Seleccione tipo de vehicuo: (1.Auto-2.Moto-3.Camion):"))
    horas=float(input("Ingrese las horas: "))
    if horas<=0:
        print("Hora no valida")
    else:
        match op:
            case 1:
                a="Auto"
                tarifa=10
            case 2:
                a="Moto"
                tarifa=5
            case 3:
                a="Camion"
                tarifa=20
            case _:
                print("Opcion no valida")
        if horas>4:
            des=tarifa*0.15
            TarifaT=tarifa+des
            print(f"El monto final a pagar de {a} es:{TarifaT} con el recargo {des}")
        else:
            print(f"El monto a pagar de {a} es {tarifa}")
except ValueError:
    print("Valor no valido")
