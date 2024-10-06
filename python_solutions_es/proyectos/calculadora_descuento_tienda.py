#Calculadora de descuento en tienda

def calcular_descuento(total_compra):
    if total_compra > 300:
        descuento = 0.30
    elif total_compra > 200:
        descuento = 0.20
    elif total_compra > 100:
        descuento = 0.10
    else:
        descuento = 0.00  #no hay descuento

    total_con_descuento = total_compra - (total_compra * descuento)
    return total_con_descuento, descuento
    
while True:
    try:
        total_compra = float(input("Introduzca el total de su compra: $"))
        total_con_descuento, descuento = calcular_descuento(total_compra)
    
        if descuento > 0:
            print(f"Se ha aplicado un {int(descuento * 100)}% de descuento.")
        else:
            print("No se ha aplicado ningun descuento.")

        print(f"El total con descuento es: ${total_con_descuento:.2f}")

        #preguntamos al usuario si quiere calcular otro descuento
        continuar = input("Desea calcular otro descuento? (q(salir)/ c(continuar)): ").lower()
        if continuar == "q":
            print("Cerrando el programa... bip boop.  :D")
            break
    except ValueError:
        print("Error, por favor ingresa un numero valido para el total de la compra.")