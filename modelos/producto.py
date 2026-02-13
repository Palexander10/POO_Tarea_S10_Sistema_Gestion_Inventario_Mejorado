class Producto:
    def __init__(self, id_prod, nombre, cantidad, precio):
        """
        Constructor de la clase Producto.
        :param id_prod: Identificador único del producto.
        :param nombre: Nombre del producto.
        :param cantidad: Cantidad en stock.
        :param precio: Precio unitario.
        """
        self._id = id_prod          # Usamos guion bajo para indicar que es 'protegido'
        self._nombre = nombre
        self._cantidad = cantidad
        self._precio = precio

    # GETTERS
    def get_id(self):
        return self._id

    def get_nombre(self):
        return self._nombre

    def get_cantidad(self):
        return self._cantidad

    def get_precio(self):
        return self._precio

    # SETTERS
    def set_nombre(self, nombre):
        self._nombre = nombre

    def set_cantidad(self, cantidad):
        self._cantidad = cantidad

    def set_precio(self, precio):
        self._precio = precio

    # Método para representación en texto
    def __str__(self):
        return (
            f"ID: {self._id} | "     
            f"Nombre: {self._nombre} | "
            f"Cantidad: {self._cantidad} | "
            f"Precio: ${self._precio:.2f}"
            )
    