#Calculadora de gastos semanales

presupuesto_semanal = 500.0

gastos = []

gastos.append(float(input("Ingresa los gastos del lunes: ")))
gastos.append(float(input("Ingrese los gastos del martes: ")))
gastos.append(float(input("ingrese los gastos del miercoles: ")))
gastos.append(float(input("Ingrese los gastos del jueves: ")))
gastos.append(float(input("Ingrese los gastos del viernes: ")))
gastos.append(float(input("Ingrese los gastos del sabado: ")))
gastos.append(float(input("Ingrese los gastos del domingo: ")))

total_gastos = sum(gastos)

if total_gastos > presupuesto_semanal:
    print(f"Has excedido tu presupuesto semanal. Te has pasado por ${total_gastos - presupuesto_semanal:.2f}.")
elif total_gastos < presupuesto_semanal:
    print(f"Estas dentro de tu prespuesto. Te sobraron ${presupuesto_semanal - total_gastos:.2f}. ")
else:
    print("Haz gastado excactamente tu prespuesto semanal.")

print(f"El total de tus gastos esta semana es: {total_gastos:.2f}")