
print("¡Bienvenido al sistema de gestión de camarotes del Crucero Atlántico!")

camarotes_disponibles = 120
historial_reservas = 0
opcion = 0

while opcion != 5:

    print("\n=== MENÚ PRINCIPAL ===")
    print("1.- Camarotes disponibles")
    print("2.- Reservar camarote")
    print("3.- Cancelar camarote")
    print("4.- Historial de reservas")
    print("5.- Salir")

    try:
        opcion = int(input("Ingrese una opción: "))
    except ValueError:
        print("Ha ocurrido un error")
        opcion = 0

    if opcion == 1:
        print("Camarotes disponibles:", camarotes_disponibles)

    elif opcion == 2:
        cantidad_reservar = 0

        while cantidad_reservar <= 0 or cantidad_reservar > camarotes_disponibles:
            try:
                cantidad_reservar = int(input("Ingrese la cantidad de camarotes a reservar: "))

                if cantidad_reservar <= 0:
                    print("La cantidad debe ser mayor a 0.")

                elif cantidad_reservar > camarotes_disponibles:
                    print("No hay suficientes camarotes disponibles.")

            except ValueError:
                print("Ingrese un número entero válido.")
                cantidad_reservar = 0

        camarotes_disponibles -= cantidad_reservar
        historial_reservas += cantidad_reservar

        print("Reserva realizada correctamente.")

    elif opcion == 3:
        cantidad_cancelar = 0

        while cantidad_cancelar <= 0 or cantidad_cancelar > 90 or cantidad_cancelar > historial_reservas:
            try:
                cantidad_cancelar = int(input("Ingrese la cantidad de camarotes a cancelar: "))

                if cantidad_cancelar <= 0:
                    print("La cantidad debe ser mayor a 0.")

                elif cantidad_cancelar > 90:
                    print("No puede superar la capacidad máxima de 90 camarotes.")

                elif cantidad_cancelar > historial_reservas:
                    print("No puede cancelar más camarotes de los reservados.")

            except ValueError:
                print("Ingrese un número entero válido.")
                cantidad_cancelar = 0

        camarotes_disponibles += cantidad_cancelar
        historial_reservas -= cantidad_cancelar

        print("Cancelación realizada correctamente.")

    elif opcion == 4:
        print("Total de reservas activas:", historial_reservas)

    elif opcion == 5:
        print("Gracias por utilizar nuestro software, hasta la próxima.")

    else:
        print("Opción inválida. Ingrese una opción del 1 al 5.")
