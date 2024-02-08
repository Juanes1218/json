import json

## EJERCICIO 1 ##

def obtener_fecha_pedido(pedido):
    return pedido["fecha"]

def ordenar_pedidos_por_fecha(pedidos):
    return sorted(pedidos, key=obtener_fecha_pedido, reverse=True)


with open("data.json") as archivo:
    datos = json.load(archivo)


pedidos = datos["ventas"]["pedidos"]
pedidos_ordenados = ordenar_pedidos_por_fecha(pedidos)

print("Pedidos ordenados por fecha:")
for pedido in pedidos_ordenados:
    print("ID del pedido:", pedido["id"])
    print("Total:", pedido["total"])
    print("Fecha:", pedido["fecha"])
    print("ID del cliente:", pedido["id_cliente"])
    print("ID del comercial:", pedido["id_comercial"])
    print()

## EJERCICIO 2 ##

print("####################")
print("####################")
print("####################")
print("####################")

def obtener_valor_total(pedido):
    return pedido["total"]

def obtener_pedidos_mas_altos(pedidos):
    pedidos_ordenados = sorted(pedidos, key=obtener_valor_total, reverse=True)
    pedidos_mas_altos = pedidos_ordenados[:2]
    return pedidos_mas_altos


with open("data.json") as archivo:
    datos = json.load(archivo)


pedidos = datos["ventas"]["pedidos"]

print("Los dos pedidos de mayor valor:")
for pedido in obtener_pedidos_mas_altos(pedidos):
    print("ID del pedido:", pedido["id"])
    print("Total:", pedido["total"])
    print("Fecha:", pedido["fecha"])
    print("ID del cliente:", pedido["id_cliente"])
    print("ID del comercial:", pedido["id_comercial"])
    print()


##EJERCICIO 3 ##

print("##################")
print("##################")
print("##################")
print("##################")
print("##################")



def obtener_clientes_con_pedidos(datos):
    clientes_con_pedidos = set()
    pedidos = datos["ventas"]["pedidos"]
    for pedido in pedidos:
        clientes_con_pedidos.add(pedido["id_cliente"])
    return clientes_con_pedidos

with open("data.json") as archivo:
    datos = json.load(archivo)
    clientes_con_pedidos = obtener_clientes_con_pedidos(datos)
    print("Clientes con pedidos:", clientes_con_pedidos)


##EJERCICIO 4 ##

print("##################")
print("##################")
print("##################")
print("##################")
print("##################")

def obtener_pedidos_2017_mayor_500(datos):
    pedidos_filtrados = []
    pedidos = datos["ventas"]["pedidos"]
    for pedido in pedidos:
        if pedido["fecha"].startswith("2017") and pedido["total"] > 500:
            pedidos_filtrados.append(pedido)
    return pedidos_filtrados

with open("data.json") as archivo:
    datos = json.load(archivo)
    pedidos_2017_mayor_500 = obtener_pedidos_2017_mayor_500(datos)
    for pedido in pedidos_2017_mayor_500:
        print("ID del pedido:", pedido["id"])
        print("Total:", pedido["total"])
        print("Fecha:", pedido["fecha"])
        print("ID del cliente:", pedido["id_cliente"])
        print("ID del comercial:", pedido["id_comercial"])
        print()