#Programa que calcula totoal, cantidad y meedia de numero introducidos.

total = 0
cantidad = 0

while True:
    entrada = input('Introduzca un numero:')
    if entrada.lower() == 'fin':
        break
        
    try:
        
        numero = float(entrada)
        total = numero + total
        cantidad = cantidad + 1
        
    except ValueError:
        print("Entrada invalida")
        
if cantidad > 0:
    media = total / cantidad
else:
    media = 0
    
print(total, cantidad, media)
