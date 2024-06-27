# Definir los productos y sus precios
productos = {
    "arroz": 2.50,
    "leche": 1.50,
    "sal": 0.75,
    "azúcar": 1.00,
    "aceite": 3.00
}

# Lista para almacenar los productos seleccionados
carro_de_compras = []

# Función para agregar productos al carro de compras
def agregar_producto():
    print("Productos disponibles:")
    for producto, precio in productos.items():
        print(f"{producto}: ${precio}")
    
    producto_seleccionado = input("Ingrese el nombre del producto que desea agregar al carro: ")
    
    # Validar si el producto ingresado existe
    if producto_seleccionado in productos:
        carro_de_compras.append(producto_seleccionado)
        print(f"{producto_seleccionado} ha sido agregado al carro de compras.")
    else:
        print("El producto ingresado no existe.")

# Función para mostrar los productos en el carro de compras
def ver_canasta():
    print("Productos en el carro de compras:")
    for producto in carro_de_compras:
        print(producto)

# Función para calcular el total a pagar
def ver_total():
    total = sum(productos[producto] for producto in carro_de_compras)
    print(f"Total a pagar: ${total}")

# Menú principal
while True:
    print("\nBienvenido al sistema de ventas de supermercado")
    print("1. Agregar productos")
    print("2. Ver canasta")
    print("3. Ver total")
    print("4. Salir")
    
    opcion = input("Ingrese el número de la opción que desea: ")
    
    if opcion == "1":
        agregar_producto()
    elif opcion == "2":
        ver_canasta()
    elif opcion == "3":
        ver_total()
    elif opcion == "4":
        print("Gracias por usar nuestro sistema de ventas. ¡Hasta luego!")
        break
    else:
        print("Opción no válida. Por favor, ingrese un número del 1 al 4.")