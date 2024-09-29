try:
    horas = float(input("Introduzca las horas:"))
    tarifa = float(input("Introduzca la tarifa por hora:"))
    if horas > 40:
        extras = horas - 40
        salario = (40 * tarifa) + (extras * tarifa * 1.5)
    else:
        salario = horas * tarifa
    print("Salario:", salario)
except ValueError:
    print("Error, por por favor introduzca un numero valido.")