#Interes compuesto

def solicitar_capital_inicial():
    """
    Funcion que solicita al usuario el capital inicial y valida que sea un numero positivo.
    Retorna el capital inicial.
    """
    while True:
        try:
            capital_inicial = float(input("Introduce el capital inicial (positivo): "))
            if capital_inicial > 0:
                return capital_inicial
            else:
                print("ERROR: El capital debe ser un numero positivo. Intentalo de nuevo.")
        except ValueError:
            print("ERROR: Por favor, ingrese un número valido.")


def solicitar_tasa_interes_anual():
    """
    Funcion que solicita al usuario la tasa de interes anual y valida que sea un numero positivo.
    Retorna la tasa de interes.
    """
    while True:
        try:
            tasa_interes = float(input("Introduce la tasa de interes inicial (positivo): "))
            if tasa_interes > 0:
                return tasa_interes / 100
            else:
                print("ERROR: La tasa de interes debe ser un numero positivo. Intentalo de nuevo.")
        except ValueError:
            print("ERROR: Por favor, ingrese un número valido.")

def solicitar_numero_años():
    """
    Funcion que solicita al usuario el numero de años y valida que sea un numero entero positivo.
    Retorna el numero de años.
    """
    while True:
        try:
            numero_años = int(input("Introduce el número de años (entero positivo): "))
            if numero_años > 0:
                return numero_años
            else:
                print("ERROR: El numero de años debe ser un numero entero.")
        except ValueError:
            print("ERROR: Por favor, ingrese un numero valido.")

def solicitar_capitalizaciones_anuales():
    """
    Funcion que solicita al usuario las capitalizaciones anuales y valida que sea un numero entero positivo.
    Retorna la capitalizacion.
    """
    while True:
        try:
            capitalizaciones = int(input("Introduce la capitalizacion por año (entero positivo): "))
            if capitalizaciones > 0:
                return capitalizaciones 
            else:
                print("ERROR: La capitalizacion tiene que ser un número entero.")
        except ValueError:
            print("ERROR: Por favor, ingrese un número valido.")

def calcular_interes_compuesto(capital, tasa, capitalizaciones, años):
    monto_final = capital * (1 + tasa / capitalizaciones) ** (capitalizaciones * años) 
    return monto_final


def main():
    print("Bievenido a la calculadora de interes compuesto :D")
    
    capital_inicial = solicitar_capital_inicial()
    tasa_interes = solicitar_tasa_interes_anual()
    numero_años = solicitar_numero_años()
    capitalizacion_anual = solicitar_capitalizaciones_anuales()
    monto_final = calcular_interes_compuesto(capital_inicial, tasa_interes, capitalizacion_anual, numero_años)

    print(f"El monto final despues de {numero_años} años sera: {monto_final:.2f}")

if __name__ == "__main__":
    main()