import conexion


# Gestion de productos
productos = []
nombre = input("Bienvenido, escriba su nombre: ")
if nombre == "":
    print("Error, fin del programa")
else:
    while True:
        numero = input(
            f'Bienvenido {nombre}: seleccione una de las opciones\n''1-Añadir producto\n''2-Borrar producto\n''3-Consultar producto\n''4-Salir\n: ')
        match numero:
            case "1":
                while True:
                    caso_1 = input('Seleccione una opcion\n''1-Añadir producto\n''2-Volver\n: ')
                    if caso_1 == "1":

                        conexion.añadir_producto()

                        print("Productos guardados:")

                        print(productos)

                    elif caso_1 == "2":
                        break
                    else:
                        print("Esa no es una opcion valida")
            case "2":
                while True:
                    caso_2 = input("Que vamos a hacer:\n""1-Eliminar producto\n""2-Volver\n: ")
                    if caso_2 == "1":
                        conexion.eliminar_producto()
                        break
                    elif caso_2 == "2":
                           break
                else:
                    print("Eso no es una opcion valida")
            case "3":
                while True:
                    caso_3 = input("Seleccione lo que hacemos:\n""1-Consultar productos\n""2-Volver\n: ")
                    if caso_3 == "1":
                        print("Lista de productos:")
                        conexion.mostrar_productos()
                    elif caso_3 == "2":
                        break
                    else:
                        print("Numero invalido")
            case "4":
                print(f"Hasta luego!!{nombre}")
                break
            case _:
                print("Esa no es una opcion valida")

