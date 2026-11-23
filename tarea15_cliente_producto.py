class Cliente:
    def __init__(self, nombre):
        self.nombre = nombre


class Producto:
    def __init__(self, nombre, precio):
        self.nombre = nombre
        self.precio = precio


def comprar_producto_cliente(cliente, producto, unidades):
    print(f"El cliente con nombre {cliente.nombre} ha comprado el producto con nombre {producto.nombre} por un precio unitario de {producto.precio} y un total de {unidades} unidades.")


cliente1 = Cliente("David")
producto1 = Producto("Camiseta", 15)

comprar_producto_cliente(cliente1, producto1, 3)