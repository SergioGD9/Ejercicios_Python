def eliminar_duplicados(numeros):
    # Creamos una lista vacía para almacenar números unicos
    numeros_unicos = []
    # Interar a través de la lista de números
    for num in numeros:
        # Si el número no esta en la lista de números unicos lo añadimos
        if num not in numeros_unicos:
            numeros_unicos.append(num)
    return numeros_unicos
    
# Solicitamos la entrada de números    
entrada = input("Introduce una lista de números separado por espacios: ")

# Convertimos la entrada en una lista de entros
numeros = list(map(int, entrada.split()))

# Eliminamos los duplicados
numeros_sin_duplicados = eliminar_duplicados(numeros)

# Mostramos la lista son los duplicados
print("Listado sin duplicados:", numeros_sin_duplicados)
    