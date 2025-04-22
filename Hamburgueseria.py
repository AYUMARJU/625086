inventario = 100
print(f"El inventario contiene {inventario} Hamburguesas")

while inventario > 0:
    if inventario <= 10:
        print("ADVERTENCIA: El inventario está casi vacio.")
    num_hamburguesas = int(input("cuantas hamburguesas quiere el cliente? "))
    if num_hamburguesas > inventario:
       print (f"NO hay suficientes hamburguesas en stock. Solo hay{inventario}")
    else:
        inventario -= num_hamburguesas
        print(f"El clienta ha pedido {num_hamburguesas} hamburguesas el inventario ahora tiene {inventario} hamburguesas")


                                 