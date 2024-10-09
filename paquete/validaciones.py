from paquete.helpers import *
def ingresar_numero()->int:
    """ingresar numero

    Returns:
        int: retorna un numero,caso contrario None
    """
    
    numero = input()

    if numero == "":
        return
    
    for caracter in numero:
        if caracter < "0" or caracter > "9":
            return
        
    numero = int(numero)
    return numero

def ingresar_cadena()->str:
    """Verificar cadena

    Returns:
        str: cadena de letras
        None: si la cadena no tiene solo letras
    """
    cadena = input()

    if cadena == "":
        return 

    for caracter in cadena:
        if not ('A' <= caracter <= 'Z'  or 'a' <= caracter <= 'z'):
            return
        
    return cadena

def ingresar_cadena_especifica(cadenas:list,upper:bool = False,solo_letras:bool=False)->str:
    """Ingresar una cadena 

    Args:
        cadenas (list): cadenas aceptadas
        upper(bool) : True para devolver cadena en mayuscula,
        False para minusculas(por defecto)

    Returns:
        str: cadena
        None: si no se ha ingresado cadena admitida
    """
    cadena = None
    if solo_letras:
        cadena = ingresar_cadena()
    else:
        cadena = input()
        
    if verificado(cadena):
        if upper:
            cadena = cadena.upper()
        else:
            cadena = cadena.lower()
        
        for valor_aceptado in cadenas:
            if cadena == valor_aceptado:
                return cadena

    return


def verificar_tipo(value: any, tipo_esperado: type) -> bool:
    """Verificar si la variable es del tipo especificado.

    Args:
        value (any): La variable a verificar.
        tipo_esperado (type): El tipo esperado de la variable.

    Returns:
        bool: True si la variable es del tipo especificado, False en caso contrario.
    """
    return isinstance(value, tipo_esperado)

def es_matriz_multiplicable(matriz1:list,matriz2:list)->bool:
    """Verifica si la cantidad de columnas de m1 es igual a cantidad filas de m2

    Args:
        matriz1 (list): matriz 1
        matriz2 (list): matriz 2

    Returns:
        bool: True si pueden multiplicarse,False si no
    """
    columnas_matriz1 = len(matriz1[0])
    filas_matriz2 = len(matriz2)

    return columnas_matriz1 == filas_matriz2

def es_lista_homogenea(lista:list,valor:any)->bool:
    """Verifica si todos los elementos de una lista son iguales al valor dado

    Args:
        lista (list): lista
        valor (any): valor a comparar

    Returns:
        bool: True si todos los elementos son igual al valor dado
    """
    for elemento in lista:
        if elemento != valor:
            return False
    return True

def validar_digitos_numero(cantidad_caracteres:int,numero:int)->bool:
    """validar cantidad de digitos de un numero

    Args:
        cantidad_caracteres (int): cantidad de digitos deseada
        numero (int): numero a verificar

    Returns:
        bool: True si el numero cumple con la cantidad de digitos
    """
    numero = str(numero)
    return len(numero) == cantidad_caracteres

def numero_en_rango(numero:int,min:int,max:int)->bool:
    """ingresar numero en rango

    Args:
        min(int): cota inferior
        max(int): cota superior

    Returns:
        bool : Si el numero está dentro del rango
    """
    return numero >= min and numero <= max
                 
def ingresar_numero_en_rango(min:int,max:int)->int:
    """ingresar numero en rango

    Args:
        min(int): cota inferior
        max(int): cota superior

    Returns:
        int : Si el numero está dentro del rango
        None: si el numero no esta dentro del rango
    """
    numero = ingresar_numero()

    if numero != None:
        if numero >= min and numero <= max:
            return numero
        
    return 

def verificado(value:any)->bool:
    """Verifica que una varible no esté vacia

    Args:
        value (any): valor

    Returns:
        bool: True si no está vacia
    """
    return value is not None and value != ""
