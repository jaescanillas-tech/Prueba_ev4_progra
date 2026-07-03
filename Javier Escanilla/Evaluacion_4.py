import os

libros = {}
contador = 1

def limpiar():
    os.system('cls')

def titulo():
    print("="*60)
    print(" *** GESTOR DE LIBROS ***")
    print("="*60, '\n')

def menu():
    print("*** MENU PRINCIPAL ***\n")
    print("1.- Agregar Libro")
    print("2.- Buscar Libro")
    print("3.- Eliminar Libro")
    print("4.- Actualizar Disponibilidad")
    print("5.- Mostrar Libros")
    print("6.- Salir")

def agregar():
    global contador, libros

    nombre = input("Ingrese el nombre del libro: ")
    copias = int(input("Ingrese las copias: "))
    prestamo = int(input("Ingrese el préstamo: "))

    if validar_libro(nombre, copias, prestamo):
        libros[contador] = {
            'nombre': nombre,
            'copias': copias,
            'prestamo': prestamo,
            'disponible': 'DISPONIBLE'
        }
        print(f"Libro agregado con ID {contador}")
        contador += 1

def eliminar():
    print("Eliminación de Libro")
    b_nombre = input("Ingrese el nombre del libro a eliminar: ")
    for i in libros:
        if libros[i]['nombre'] == b_nombre:
            libros[i] = None
            break



def validar_libro(n, c, p):
    if n.strip() == '':
        raise ValueError("El nombre del libro no puede quedar vacío")
    elif c < 0:
        raise ValueError("Las copias deben ser mayores o iguales a 0")
    elif p <= 0:
        raise ValueError("El préstamo debe ser mayor que 0")
    else:
        return True

def validador_op(op):
    if op.strip() == "":
        raise ValueError("La opción no puede quedar vacía")
    elif op.isdigit():
        if int(op) <= 6:
            return True
        else:
            raise ValueError("La opción debe estar entre 1 y 6")
    else:
        raise ValueError("Debe ingresar un número")

def validador_dispo():
    for i in libros:
        if libros[i]['copias'] == 0:
            libros[i]['disponible'] == 'SIN COPIAS'
        elif libros[i]['copias'] > 0:
            libros[i]['disponible'] == 'DISPONIBLE'

def buscar():
    print("Busqueda por nombre")
    b_nombre = input("Ingrese el nombre del libro: ")
    for i in libros:
        if libros[i]['nombre'] == b_nombre:
            print("libro encontrado")
            print(f"Nombre: {libros[i]['nombre']}")
            print(f"Copias: {libros[i]['copias']}")
            print(f"Prestamo: {libros[i]['prestamo']}")
            print(f"Disponibilidad: {libros[i]['disponible']}")
            return True
    return False


def main():
    while True:
        try:
            titulo()
            menu()
            opcion = input("Ingresa la opción deseada: ")

            if validador_op(opcion):
                if opcion == "1":
                    limpiar()
                    titulo()
                    print("*** Agregar Libro ***")
                    agregar()
                elif opcion == "2":
                    limpiar()
                    titulo()
                    print("*** Buscar Libro ***")
                    if buscar():
                        print("Volviendo...")
                    else:
                        print("=== Titulo no encontrado ===")
                elif opcion == "3":
                    limpiar()
                    titulo()
                    print("*** Eliminar Libro ***")
                    eliminar()
                elif opcion == "4":
                    limpiar()
                    titulo()
                    validador_dispo()
                    print("=== Disponibilidad Actualizada ===")
                elif opcion == "5":
                    limpiar()
                    titulo()
                    print("*** Mostrar Libros ***")
                    print("=== Lista de Libros ===")
                    if libros != None:
                        for i in libros:
                            print(f"\nNombre: {libros[i]['nombre']}")
                            print(f"Copias: {libros[i]['copias']}")
                            print(f"Prestamo: {libros[i]['prestamo']}")
                            print(f"Disponibilidad: {libros[i]['disponible']}")
                    else:
                        print("=== No hay titulos disponible ===")
                        
                elif opcion == "6":
                    print("Saliendo...")
                    break
            input("\nPresione Enter para continuar...")
            limpiar()

        except ValueError as e:
            limpiar()
            print("*"*60)
            print(f"ERROR: {e}")
            print("*"*60)
            input("\nPresione Enter para continuar...")

if __name__ == '__main__':
    limpiar()
    main()