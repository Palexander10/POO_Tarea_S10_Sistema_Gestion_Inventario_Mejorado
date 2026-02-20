from modelos.producto import Producto
from servicios.inventario import Inventario
import os

def limpiar_pantalla():
    os.system('cls' if os.name == 'nt' else 'clear')

def menu():
    print("Iniciando sistema de inventario...")
    # Al crear la instancia, se ejecuta cargar_desde_archivo() automáticamente
    mi_inventario = Inventario("inventario.txt")

    while True:
        print("\n" + "="*40)
        print("   SISTEMA DE GESTIÓN DE INVENTARIO")
        print("="*40)
        print("1. Añadir producto")
        print("2. Eliminar producto")
        print("3. Actualizar producto")
        print("4. Buscar producto por nombre")
        print("5. Listar todos los productos")
        print("6. Salir")
        print("="*40)
        
        opcion = input("Seleccione una opción: ")

        if opcion == '1':
            print("\n--- Añadir Producto ---")
            id_p = input("Ingrese ID único: ")
            nombre = input("Ingrese nombre: ")
            try:
                cantidad = int(input("Ingrese cantidad: "))
                precio = float(input("Ingrese precio: "))
                nuevo_prod = Producto(id_p, nombre, cantidad, precio)
                mi_inventario.agregar_producto(nuevo_prod)
            except ValueError:
                print("❌ Error: La cantidad y el precio deben ser números válidos.")

        elif opcion == '2':
            print("\n--- Eliminar Producto ---")
            id_p = input("Ingrese el ID del producto a eliminar: ")
            mi_inventario.eliminar_producto(id_p)

        elif opcion == '3':
            print("\n--- Actualizar Producto ---")
            id_p = input("Ingrese el ID del producto a actualizar: ")
            print("Deje vacío y presione Enter si no desea modificar el campo.")
            q_str = input("Nueva cantidad: ")
            p_str = input("Nuevo precio: ")

            try:
                cantidad = int(q_str) if q_str.strip() else None
                precio = float(p_str) if p_str.strip() else None
                mi_inventario.actualizar_producto(id_p, cantidad, precio)
            except ValueError:
                print("❌ Error: Ingresaste un valor no numérico.")

        elif opcion == '4':
            print("\n--- Buscar Producto ---")
            nombre = input("Ingrese nombre a buscar: ")
            resultados = mi_inventario.buscar_por_nombre(nombre)
            if resultados:
                for r in resultados:
                    print(r)
            else:
                print("⚠️ No se encontraron coincidencias.")

        elif opcion == '5':
            print("\n--- Inventario Completo ---")
            mi_inventario.mostrar_todos()

        elif opcion == '6':
            print("Saliendo del sistema de inventarios. ¡Hasta luego!")
            break
        else:
            print("❌ Opción no válida. Intente de nuevo.")

if __name__ == "__main__":
    menu()