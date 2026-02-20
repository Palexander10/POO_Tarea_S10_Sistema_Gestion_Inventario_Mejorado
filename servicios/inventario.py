import os
from modelos.producto import Producto

class Inventario:
    def __init__(self, ruta_archivo="inventario.txt"):
        self.productos = []
        self.ruta_archivo = ruta_archivo
        # Al instanciar, automáticamente intentamos cargar los datos
        self.cargar_desde_archivo()

    def cargar_desde_archivo(self):
        """Lee el archivo de texto y reconstruye el inventario."""
        try:
            with open(self.ruta_archivo, 'r') as archivo:
                for linea in archivo:
                    linea = linea.strip()
                    if linea:
                        # Asumimos que el formato es: ID,Nombre,Cantidad,Precio
                        datos = linea.split(',')
                        if len(datos) == 4:
                            id_prod, nombre, cantidad, precio = datos
                            prod = Producto(id_prod, nombre, int(cantidad), float(precio))
                            self.productos.append(prod)
            print(f"✅ Inventario cargado exitosamente desde '{self.ruta_archivo}'.")
            
        except FileNotFoundError:
            # Si el archivo no existe, lo informamos y creamos uno vacío
            print(f"⚠️ Archivo '{self.ruta_archivo}' no encontrado. Se creará uno nuevo automáticamente.")
            # Creamos el archivo vacío para evitar errores futuros
            open(self.ruta_archivo, 'a').close()
            
        except PermissionError:
            print(f"❌ Error: No tienes permisos para leer el archivo '{self.ruta_archivo}'.")
            
        except ValueError:
            # Captura errores si el archivo está corrupto (ej: texto en lugar de números)
            print("❌ Error: Datos corruptos en el archivo. Verifica el formato (ID,Nombre,Cantidad,Precio).")
            
        except Exception as e:
            # Captura cualquier otro error inesperado
            print(f"❌ Error inesperado al cargar el archivo: {e}")

    def guardar_en_archivo(self):
        """Sobreescribe el archivo con la lista actual de productos."""
        try:
            with open(self.ruta_archivo, 'w') as archivo:
                for prod in self.productos:
                    archivo.write(prod.a_texto() + '\n')
            print("💾 Cambios guardados en el archivo exitosamente.")
            
        except PermissionError:
            print(f"❌ Error: No tienes permisos para escribir en '{self.ruta_archivo}'.")
            
        except Exception as e:
            print(f"❌ Error inesperado al guardar: {e}")

    # --- Métodos Modificados para usar guardar_en_archivo() ---

    def agregar_producto(self, producto):
        if self.buscar_por_id(producto.get_id()):
            print("⚠️ Error: Ya existe un producto con ese ID.")
        else:
            self.productos.append(producto)
            print("✅ Producto agregado al inventario en memoria.")
            self.guardar_en_archivo() # Guardamos en disco

    def eliminar_producto(self, id_prod):
        prod = self.buscar_por_id(id_prod)
        if prod:
            self.productos.remove(prod)
            print(f"✅ Producto con ID {id_prod} eliminado de la memoria.")
            self.guardar_en_archivo() # Guardamos en disco
        else:
            print("⚠️ Error: Producto no encontrado.")

    def actualizar_producto(self, id_prod, nueva_cantidad=None, nuevo_precio=None):
        prod = self.buscar_por_id(id_prod)
        if prod:
            if nueva_cantidad is not None:
                prod.set_cantidad(nueva_cantidad)
            if nuevo_precio is not None:
                prod.set_precio(nuevo_precio)
            print("✅ Producto actualizado en memoria.")
            self.guardar_en_archivo() # Guardamos en disco
        else:
            print("⚠️ Error: Producto no encontrado.")

    # --- Métodos de solo lectura (sin cambios) ---
    def buscar_por_nombre(self, nombre):
        return [p for p in self.productos if nombre.lower() in p.get_nombre().lower()]

    def mostrar_todos(self):
        if not self.productos:
            print("El inventario está vacío.")
        else:
            for prod in self.productos:
                print(prod)

    def buscar_por_id(self, id_prod):
        for prod in self.productos:
            if prod.get_id() == id_prod:
                return prod
        return None
    