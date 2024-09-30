#Calculadora de impuestos sobre la renta

ingreso= float(input("Por favor, ingresa tu ingreso anual:"))

if ingreso < 0:
    print("El ingreso no puede ser negativo.")
else:
    if ingreso <= 10000:
        tasa = 0.10
    elif ingreso <= 50000:
        tasa = 0.20
    else:
        tasa = 0.30
    impuesto = ingreso * tasa
    print(f"Debes pagar ${impuesto:.2f} en impuestos.")
