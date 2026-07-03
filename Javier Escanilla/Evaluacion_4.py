import time
import os

def limpiar():
    os.system('cls')

def titulo():
    print("="*60)
    print(" *** GESTOR DE LIBROS ***")
    print("="*60, '\n')
    return

def menu():
    print("*** MENU PRINCIPAL ***\n")
    print("1.- Agregar Libro")
    print("2.- Buscar Libro")
    print("3.- Eliminar Libro")
    print("4.- Actualizar Disponibilidad")
    print("5.- Mostrar Libros")
    print("6.- Salir")

def Libro(nombre, copias, prestamo):
    Libro = {
        0: {'nombre': nombre, 'copias': copias, 'prestamo': prestamo}
    }
    
    print(Libro[1])
    return

def agregar():
    while True:
        nombre = input("ingrese el nombre del libro: ")
        copias = int(input("ingrese las copias: "))
        prestamo = int(input("ingrese el prestamo: "))
        
        if validar_libro(nombre, copias, prestamo):
            print('validado')
            

def validar_libro(n, c, p):
    if n.strip() == '':
        raise ValueError("El nombre del libro no puede quedar vacio")
    #cambiar tipo y validar como str para luego cambiarlo a int
    elif not c >= 0:
        raise ValueError("las copias deben ser entero mayo a 0")
    elif not p > 0:
        raise ValueError("No puede quedar en 0")
    else:
        return n, c, p, True


def eliminar():
    pass

def validador_op(op):
    
    if op.strip() == "":
        raise ValueError("La opcion no puede quedar vacía")
    elif op.isdigit():
        if op.isdigit() <= 6:
            return True
    


def main():
    while True:
        try:
            titulo()
            menu()
            opcion = input("Ingresa la opcion deseada: ")
            if validador_op(opcion):
                if opcion == "1":
                    titulo()
                    print("*** Agregar Libro ***")
                    agregar()


        except ValueError as e:
            limpiar()
            print("*"*60)
            print(f"ERROR: {e}")
            print("*"*60)

if __name__ == '__main__':
    limpiar()
    main()