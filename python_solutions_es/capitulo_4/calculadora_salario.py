#Codigo para calcular el salario

def calculo_salario(horas, tarifa):
    if horas > 40:
        extras = (horas - 40) * (tarifa * 1.5)
        salario = 40 * tarifa + extras
    else:
        salario = horas * tarifa
    return salario

try:
    horas = float(input("Introduzca las horas: "))
    tarifa = float(input("Introduzca la tarifa por hora: "))
    salario = calculo_salario(horas, tarifa)
    print(f"Salario: ${salario}")
except ValueError:
    print("Error, por favor introduzca un numero valido.")
