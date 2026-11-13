print("¡Bienvenido a la Escuela Internacional de Gastronomía!")

cantidad_chefs = 0

while cantidad_chefs <= 0:
    try:
        cantidad_chefs = int(input("Ingrese la cantidad de chefs que desea registrar: "))
        if cantidad_chefs <= 0:
            print("¡Ingrediente inválido! Ingresa un entero positivo para continuar el registro.")
    except ValueError:
        print("¡Ingrediente inválido! Ingresa un entero positivo para continuar el registro.")
        cantidad_chefs = 0

chefs_maestros = 0
chefs_aprendices = 0

for i in range(cantidad_chefs):
    print("\nRegistro del Chef", i + 1)

    codigo_culinario = input("Ingrese el código culinario: ")

    while len(codigo_culinario) < 8 or " " in codigo_culinario:
        print("El código debe tener al menos 8 caracteres y no contener espacios.")
        codigo_culinario = input("Ingrese nuevamente el código culinario: ")

    experiencia = 0

    while experiencia <= 0:
        try:
            experiencia = int(input("Ingrese la experiencia culinaria en años: "))
            if experiencia <= 0:
                print("¡Error gastronómico! Ingresa un número entero positivo para la experiencia culinaria.")
        except ValueError:
            print("¡Error gastronómico! Ingresa un número entero positivo para la experiencia culinaria.")
            experiencia = 0

    if experiencia > 5:
        print("Clasificación: Chef Maestro")
        chefs_maestros += 1
    else:
        print("Clasificación: Chef Aprendiz")
        chefs_aprendices += 1

print("\n¡La escuela cuenta con", chefs_maestros, "Chefs Maestros y", chefs_aprendices, "Chefs Aprendices! ¡A cocinar!")
print("Total de chefs registrados:", cantidad_chefs)
