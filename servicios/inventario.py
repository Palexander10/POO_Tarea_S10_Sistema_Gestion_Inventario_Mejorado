from modelos.producto import Producto

class Inventario:
    def __init__(self):
        # Lista que almacenará los objetos de tipo Producto
        self.productos = []

    def agregar_producto(self, producto):
        
        # Añade un nuevo producto si el ID no existe ya.
        
        if self.buscar_por_id(producto.get_id()):
            print("Error: Ya existe un producto con ese ID.")
        else:
            self.productos.append(producto)
            print("Producto agregado exitosamente.")

    def eliminar_producto(self, id_prod):
        
        #Elimina un producto buscando por su ID.
        
        prod = self.buscar_por_id(id_prod)
        if prod:
            self.productos.remove(prod)
            print(f"Producto con ID {id_prod} eliminado.")
        else:
            print("Error: Producto no encontrado.")

    def actualizar_producto(self, id_prod, nueva_cantidad=None, nuevo_precio=None):
        
        # Actualiza cantidad o precio. Solo actualiza si el valor no es None.
        
        prod = self.buscar_por_id(id_prod)
        if prod:
            if nueva_cantidad is not None:
                prod.set_cantidad(nueva_cantidad)
            if nuevo_precio is not None:
                prod.set_precio(nuevo_precio)
            print("Producto actualizado correctamente.")
        else:
            print("Error: Producto no encontrado.")

    def buscar_por_nombre(self, nombre):
        
        # Busca productos que contengan el texto (coincidencia parcial).
        # Retorna una lista de productos encontrados.
        
        resultados = [p for p in self.productos if nombre.lower() in p.get_nombre().lower()]
        return resultados

    def mostrar_todos(self):
        
        # Imprime todos los productos del inventario.
        
        if not self.productos:
            print("El inventario está vacío.")
        else:
            for prod in self.productos:
                print(prod)

    # Método auxiliar (privado sugerido) para no repetir código
    def buscar_por_id(self, id_prod):
        for prod in self.productos:
            if prod.get_id() == id_prod:
                return prod
        return None