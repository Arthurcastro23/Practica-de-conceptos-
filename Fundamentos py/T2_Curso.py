print("\n##### Registro y analisis de ventas #####\n")
print("Instrucciones de uso:\n")
print("Al terminar de registrar los productos vendidos escriba 'fin' para ver las ganancias\n")

def regProductos():
    productos = []

    while True: #Ciclo while para registrar los productos
        nombre = input("Nombre del producto: ")
#Si el usuario escribe 'fin', se termina el registro y vemos las ganancias
        if nombre == "fin":
            break
#Buscar si el producto ya fue registrado
        encontrado = False #logica booleana para saber si el producto ya existe
        for p in productos: #Iterar sobre la lista de productos
            if p["nombre"] == nombre: #Si el producto ya existe en la lista, actualiza su cantidad
                print( f"Producto ya registrado. Precio existente: ${p['precio']}")
                cantidad = int(input("Ingrese la cantidad adicional vendida: "))
        #Actualizar la cantidad del producto
                p["cantidad"] += cantidad
                total_prod = p["precio"] * p["cantidad"]

                print( f"Cantidad total de {nombre}: {p['cantidad']}")
                print( f"Total generado por {nombre}: ${total_prod}")
    #Marcar que el producto fue encontrado
                encontrado = True # Logica booleana para indicar que el producto ya existe
                break

        if not encontrado: #Si el producto no fue encontrado, se registra uno nuevo
            precio = float(input("Precio del producto: "))
            cantidad = int(input("Cantidad vendida: "))
        # prod es un diccionario que almacena la informacion del producto
            prod = { "nombre": nombre,"precio": precio,"cantidad": cantidad}
#.append lo usamos para agregar el diccionario prod a la lista productos
            productos.append(prod)

    return productos

#Funcion para calcular las ventas totales y el producto mas vendido
def Ventas(productos):
    if len(productos) == 0:
        print("No se registro la cantidad del producto")
        return
#Declaramos las variables para mostrar los resultados
    total = 0
    mas_vendido = ""
    mayor_cantidad = 0
#Iteramos para calcular las ventas totales y el producto mas vendido
    for p in productos:
        total += p["precio"] * p["cantidad"] #Ventas totales

        if p["cantidad"] > mayor_cantidad:
            mayor_cantidad = p["cantidad"]
            mas_vendido = p["nombre"]

    print("\n##### VENTAS #####\n")
    print("Ganancias totales:", total)
    print(f"Producto más vendido: {mas_vendido}, {mayor_cantidad} unidades")


productos = regProductos()
Ventas(productos)
