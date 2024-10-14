fruta = "maracuya"
indice = len(fruta) - 1 # comienza en el ultimo indice

while indice >= 0:   # el bucle continua hasta que el indice sea 0 o mayor
    letra = fruta[indice]
    print(letra)
    indice -= 1  # podemos usar tambien (indice = indice - 1), decrementa para contar desde atras