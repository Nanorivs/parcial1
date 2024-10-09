from paquete.validaciones import *
from paquete.listas import *
from paquete.matrices import *


stock_sucursales = crear_matriz(4,4)
precios = [1500,2000,1000,3000]
productos = ["DETERGENTE","DESINFECTANTE","LAVANDINA","JABON_LIQUIDO"]
DETERGENTE = 0
DESINFECTANTE = 1
LAVANDINA = 2
JABON_LIQUIDO = 3
MIN_STOCK = 0
MAX_STOCK = 5000

def registrar_stock(sucursales:list,min:int=0,max:int=5000)-> None:
    
    for i,stock in enumerate(stock_sucursales):
        while True:
            limpiar()
            print(f"STOCK SUCURSAL {i+1}")
            print("Detergente: ")
            stock[DETERGENTE] = ingresar_numero_en_rango(min,max)
            print("Desinfectante: ")
            stock[DESINFECTANTE] = ingresar_numero_en_rango(min,max)
            print("Lavandina: ")
            stock[LAVANDINA] = ingresar_numero_en_rango(min,max)
            print("Jabon liquido: ")
            stock[JABON_LIQUIDO] = ingresar_numero_en_rango(min,max)

            if verificado(stock[DETERGENTE]) and verificado(stock[DESINFECTANTE]) and verificado(stock[LAVANDINA]) and verificado(stock[JABON_LIQUIDO]):

                stock_total = stock[DETERGENTE] + stock[DESINFECTANTE] + stock[LAVANDINA] + stock[JABON_LIQUIDO]
                if stock_total < 15001:
                    break
                else:
                    print("Upss,hay errores")
            
        
def total_stock_sucursal(lista_sucursales:list)->list:
    stock_sucursales = list()

    cant_productos = len(productos)

    for sucursal in lista_sucursales:
        total = 0
        for stock in range(cant_productos):
            total += sucursal[stock]
        stock_sucursales.append(total)

    return stock_sucursales

def productos_menor_stock(lista_sucursales:list,max_stock:int)->list:
    productos_menor_stock = list()

    cantidad_productos = len(lista_sucursales[0])
    
    for sucursal in lista_sucursales:
        min = max_stock

        for indice_producto in range(cantidad_productos):
            if sucursal[indice_producto] < min:
                min = sucursal[indice_producto]
                i = indice_producto
        
        productos_menor_stock.append(productos[i])

    return productos_menor_stock

def maximo_stock_de_producto(lista_sucursales:list)->list:

    max_stock_product = list()

    for indice_producto,producto in enumerate(productos):
    
       max = 0
       nombre = producto
       nro_sucursal = None
       for nro,sucursal in enumerate(stock_sucursales):
            
            if sucursal[indice_producto] > max:
                max = sucursal[indice_producto]
                nro_sucursal = nro + 1
      
       info = "||Producto: {}, Stock: {}, Sucursal: {} ||".format(nombre, max, nro_sucursal)
       max_stock_product.append(info)

    return max_stock_product

def sucursal_con_mayor_valor_stock(lista_sucursales:list)->str:
   
    nro_sucursal = None
    mayor_valor = 0
    for nro,sucursal in enumerate(stock_sucursales):
        total = 0
        for producto in range(len(productos)):
            total += stock_sucursales[nro][producto] * precios[producto]
           
        if total > mayor_valor :
            nro_sucursal = nro
            mayor_valor = total
    
    info = "||Sucursal con mayor valor: {}, Valor: ${}||".format(nro_sucursal,mayor_valor)
    return info
        
    
            
#1
registrar_stock(stock_sucursales,min=0,max=5000)

#2
total_stock_sucursales = total_stock_sucursal(stock_sucursales)
print(f"Total de stocks por sucursal: ")
print(total_stock_sucursales)

#3
productos_menos_stock = productos_menor_stock(stock_sucursales,max_stock=5000)
print(f"Productos con menor stock segun sucursal: ")
print(productos_menos_stock)

#4
max_stock_productos = maximo_stock_de_producto(stock_sucursales)
print("Maximo stock de cada producto en todas las sucursales ") #Lo tomé como el maximo stock que puede llegar a tener un producto
print(max_stock_productos)

#5
mayor_valor = sucursal_con_mayor_valor_stock(stock_sucursales)
print(mayor_valor)

