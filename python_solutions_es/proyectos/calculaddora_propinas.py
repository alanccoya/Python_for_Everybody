#Calculadora de propinas!

#solicitar el total de la cuenta
total_cuenta = float(input("Por favor, ingrese el total de la cuenta:"))

#solicitar evalucion del servicio recivido 
servicio = input("Como fue el servicio? (bueno, regular, malo):").lower()

if servicio == "bueno":
    porcentaje_propina = 0.20
elif servicio == "regular":
    porcentaje_propina = 0.15
elif servicio == "malo":
    porcentaje_propina = 0.10
else:
    print("Nivel de servicio no válido.")
    porcentaje_propina = 0

#Calculamos el monto de la propina
propina = total_cuenta * porcentaje_propina
#calculamos el total con propina
total_con_propina =  total_cuenta * propina

print(f"La propina es: {propina:.2f}")
print(f"El total a pagar con propina es: {total_con_propina:.2f}")
