def swap(value1:any,value2:any)->None:
    """intercambiar valor de variables

    Args:
        value1 (any): variable 1
        value2 (any): variable 2
    """
    aux = value1
    value1 = value2
    value2 = aux

def numero_random(min:int,max:int)->int:    
    """numero random

    Args:
        min (int): limite inferior
        max (int): limite superior

    Returns:
        int: numero aleatorio entre el rango
    """
    from random import randint
    if  type(min)  != int or type(max) != int:
        return
    
    if min > max:
        aux = min
        min = max
        max = aux

    return randint(min,max)

def limpiar()->None:
    """limpiar pantalla
    """
    import os
    os.system("cls")

def reduce_lista(funcion,lista:list)->any:
    """Compara dos elementos y retorna el resultado de una operacion
    Returns:
        any: el valor final que toma el resultado """
    resultado = lista[0]
    for elemento in lista[1:]:
        resultado = funcion(resultado,elemento)
    return resultado