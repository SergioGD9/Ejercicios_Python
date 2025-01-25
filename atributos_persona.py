class Persona:
    def __init__(self, altura, peso, edad, sexo, nombre):
        self.altura = altura
        self.peso = peso
        self.edad = edad
        self.sexo = sexo
        self.nombre = nombre

# Diccionario para almacenar los avatares
avatares = {}

while True:
    nombre = input("Introduce el nombre: ")
    if nombre in avatares:
        print("El nombre ya está en uso. Por favor, elige otro nombre.")
        continue

    altura = float(input("Introduce la altura: "))
    peso = float(input("Introduce el peso: "))
    edad = int(input("Introduce la edad: "))
    sexo = input("Introduce el sexo: ")

    avatar = Persona(altura, peso, edad, sexo, nombre)
    avatares[nombre] = avatar

    print(f'Dime el nombre del avatar {avatar.nombre}')
    print(f'Dime el peso del avatar {avatar.peso}')
    print(f'Dime la edad del avatar {avatar.edad}')
    print(f'Dime el sexo del avatar {avatar.sexo}')
    print(f'Dime la altura del avatar {avatar.altura}')

    continuar = input("¿Quieres crear otro avatar? (s/n): ")
    if continuar.lower() != 's':
        break

# Mostrar todos los avatares creados
print("\nAvatares creados:")
for nombre, avatar in avatares.items():
    print(f'Nombre: {avatar.nombre}, Altura: {avatar.altura}, Peso: {avatar.peso}, Edad: {avatar.edad}, Sexo: {avatar.sexo}')