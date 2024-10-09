from paquete.helpers import *
def crear_matriz(filas:int,columnas:int,random:bool = False)->list:
    """crear matriz

    Args:
        matriz (list): 
        filas (int): cantidad de  filas
        columnas (int): cantidad de columnas
        ceros (bool) : si True,todos los elementos son cero

    Returns:
        list: matriz inicializada con ceros
    """
    matriz = [ ]
    for fila in range(filas):
        fila = []
        for columna in range(columnas):
            fila.append(0)

        matriz.append(fila)

    if random:
        for fila in range(filas):
            for columna in range(columnas):
                matriz[fila][columna] = numero_random(1,9)
    return matriz

def imprimir_matriz(matriz:list)->None:
    """imprimir matriz por consola

    Args:
        matriz (list): matriz
    """
    print()
    
    for fila in matriz:
        print(fila)

    print()

def busqueda_lineal_matriz(matriz : list, valor : any) -> list:
    """
    Realiza una busqueda sobre una matriz de forma lineal

    Parametros:
    matriz: representa el conjunto de datos sobre el cual se va a realizar la busqueda
    valor: valor del cual se desea saber su indice

    Retorno: 
    Retorna None si el valor no se encuentra o una lista con los indices del elemento
    encontrado
    """
    retorno = None
    for i in range(len(matriz)):
        for j in range(len(matriz[i])):
            if matriz[i][j] == valor:
                retorno = [i,j]
                break
    return retorno

def imprimir_tabla(matriz:list,cabecera:list=None)->None:
    """imprimir matriz bidimensional en filas(TABLA)

    Args:
        matriz (list): matriz
        cabecera(list): lista de strings que responden al nombre de cada columna(None por defecto)
        coincide el largo con el largo de cada fila 
    """
   
    matriz_print = matriz[:]    
    espacio_columnas = []

    if cabecera != None:
        matriz_print.insert(0,cabecera)
    
    filas = len(matriz_print)
    columnas = len(matriz_print[0])

    #espacio de cada columna
    for c in range(columnas):
        max = 0
        for f in range(filas):
            
            if len(str(matriz_print[f][c])) > max:
                max = len(str(matriz_print[f][c]))
        espacio_columnas.append(max)

    #Impresion
    linea = "_"
    cantidad = reduce_lista(lambda actual,siguiente: actual + siguiente,espacio_columnas)
    cantidad += len(cabecera) * 3
    for f in range(filas):
        for c in range(columnas):
            print(f"{matriz_print[f][c]:^{espacio_columnas[c]}}",end =" | " )
        print()
        print(linea*cantidad)    
            
    

