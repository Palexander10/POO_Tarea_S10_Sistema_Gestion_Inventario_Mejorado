from modelos.producto import Producto
from servicios.inventario import Inventario
import os

def limpiar_pantalla():
    # Limpia la consola según el sistema operativo 
    os.system('cls' if os.name == 'nt' else 'clear')

def menu():
    # Instanciamos la clase Inventario
    mi_inventario = Inventario()

    while True:
        print("\n--- SISTEMA DE GESTIÓN DE INVENTARIO ---")
        print("1. Añadir producto")
        print("2. Eliminar producto")
        print("3. Actualizar producto")
        print("4. Buscar producto por nombre")
        print("5. Listar todos los productos")
        print("6. Salir")
        
        opcion = input("Seleccione una opción: ")

        if opcion == '1':
            print("\n--- Añadir Producto ---")
            id_p = input("Ingrese ID único: ")
            nombre = input("Ingrese nombre: ")
            try:
                cantidad = int(input("Ingrese cantidad: "))
                precio = float(input("Ingrese precio: "))
                # Creamos el objeto Producto
                nuevo_prod = Producto(id_p, nombre, cantidad, precio)
                # Lo pasamos al inventario
                mi_inventario.agregar_producto(nuevo_prod)
            except ValueError:
                print("Error: La cantidad y el precio deben ser números.")

        elif opcion == '2':
            id_p = input("Ingrese el ID del producto a eliminar: ")
            mi_inventario.eliminar_producto(id_p)

        elif opcion == '3':
            id_p = input("Ingrese el ID del producto a actualizar: ")
            print("Deje vacío si no desea modificar el campo.")
            q_str = input("Nueva cantidad (Enter para omitir): ")
            p_str = input("Nuevo precio (Enter para omitir): ")

            cantidad = int(q_str) if q_str else None
            precio = float(p_str) if p_str else None

            mi_inventario.actualizar_producto(id_p, cantidad, precio)

        elif opcion == '4':
            nombre = input("Ingrese nombre a buscar: ")
            resultados = mi_inventario.buscar_por_nombre(nombre)
            if resultados:
                print("\n--- Resultados de búsqueda ---")
                for r in resultados:
                    print(r)
            else:
                print("No se encontraron coincidencias.")

        elif opcion == '5':
            print("\n--- Inventario Completo ---")
            mi_inventario.mostrar_todos()

        elif opcion == '6':
            print("Saliendo del sistema...")
            break
        else:
            print("Opción no válida.")

if __name__ == "__main__":
    menu()