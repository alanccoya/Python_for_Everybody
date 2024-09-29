#Calculador de horas extras

try:
    horas = float(input("Introduzca las horas:"))        #Usamos "float" para que el programa pueda leer decimales. 
    tarifa = float(input("Introduzca la tariifa por hora:"))
    if horas > 40:  
        extras = horas - 40     #Hacemos esta operacion "horas - 40" para calcular horas extras.        
        salario = (40 * tarifa) + (extras * tarifa * 1.5)
    else:
        salario = horas * tarifa
    print("Salario:", salario)

except ValueError:
    print("Error, por favor introduzca un numero.")
