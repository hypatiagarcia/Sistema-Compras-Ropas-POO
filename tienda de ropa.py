#Sistema de Compras de Ropas con POO

class Producto:
    def __init__(self, nombre, precio, talla):
        self.nombre = nombre #el nombre tambien podria entenderse como la categoria del producto
        self.precio = precio
        self.talla = talla
    def obtener_precio(self):
        return self.precio
    def mostrar_informacion(self):
        return f"Producto: {self.nombre} -  Precio: ${self.precio} - Talla: {self.talla}"


class Tienda:
    def __init__(self):
        self.productos = []
    def agg_producto(self, producto):
        self.productos.append(producto)
    def mostrar_productos(self):
        print("\nProductos disponibles:")
        for i, producto in enumerate(self.productos):
            print(f"{i}. {producto.mostrar_informacion()}")
    def procesar_compra(self, indices_seleccionados):
        total = 0
        print("\nProductos seleccionados:")
        for indice in indices_seleccionados:
            producto = self.productos[indice - 1]
            print(producto.mostrar_informacion())
            total += producto.obtener_precio()
        print(f"Total a pagar: ${total:}")


camisa = Producto("Camisa Blanca", 20.0, "M")
pantalon = Producto("Pantalón Negro", 30.0, "L")
zapato = Producto("Zapato Deportivo", 50.0, 42)

tienda = Tienda()
tienda.agg_producto(camisa)
tienda.agg_producto(pantalon)
tienda.agg_producto(zapato)


print("Bienvenido a la tienda de ropa!")
comprando = True
indices_seleccionados = []

while comprando:
    tienda.mostrar_productos()
    seleccion = input("Selecciona el número del producto que queres ('0' para finalizar la compra): ")
    if seleccion == '0':
        comprando = False
    elif seleccion.isdigit() and 1 <= int(seleccion) <= len(tienda.productos):
        indices_seleccionados.append(int(seleccion))
        print("Producto fue añadido.")
    else:
        print("Error, intenta de nuevo.")
        
if indices_seleccionados:
    tienda.procesar_compra(indices_seleccionados)
else:
    print("Gracias por visitar la tienda!")