def fibonacci_iterativo(n):
    if n <= 0:
        return []
    elif n == 1:
        return [0]
    elif n == 2:
        return [0, 1]
    
    fib_sequence = [0, 1]
    for i in range(2, n):
        fib_sequence.append(fib_sequence[-1] + fib_sequence[-2])
    return fib_sequence


def fibonacci_recursivo(n):
    if n <= 0:
        return 0
    elif n == 1:
        return 0
    elif n == 2:
        return 1
    return fibonacci_recursivo(n-1) + fibonacci_recursivo(n-2)

# Ejemplo de uso
n = 10

print("Fibonacci (Interactivo):", fibonacci_iterativo(n))
print("Fibonacci (Recursivo):", [fibonacci_recursivo(i) for i in range(1,n+1)])