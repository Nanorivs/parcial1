from paquete.helpers import *
def busqueda_lineal(lista : list, valor : any) -> int:
    """
    Realiza una busqueda sobre una lista de forma lineal

    Args:
    lista(list): representa el conjunto de datos sobre el cual se va a realizar la busqueda
    valor(any): valor del cual se desea saber su indice

    Return: 
    indice(int): del elemento encontrado
    None: si no esta el elemento
    """
    retorno = None
    for i in range(len(lista)):
        if lista[i] == valor:
            retorno = i
            break
    return retorno



def busqueda_binaria(lista, valor):
    """ Realiza una busqueda sobre una lista ordenada de forma binaria

    Args:
    lista(list): representa el conjunto de datos sobre el cual se va a realizar la busqueda
    valor(any): valor del cual se desea saber su indice

    Returns:
    None: si el valor no se encuentra 
    int: el indice del primer elemento hayado
    """
    
    izquierda = 0
    derecha =  len(lista) - 1
    retorno = None

    while izquierda <= derecha:
        medio = (izquierda + derecha) // 2

        if valor == lista[medio]:
            retorno = medio
            break
        else:
            if valor > lista[medio]:
                izquierda = medio + 1
            else:
                derecha = medio - 1
    return retorno

def promedio_lista(lista:list)->float:
    """promedio de una lista

    Args:
        lista (list): lista

    Returns:
        float: promedio de los elementos que son numeros enteros de una lista
    """
    total = 0
    cantidad_numeros = 0
    for numero in lista:
            total += numero
            cantidad_numeros += 1
    return total / cantidad_numeros
    

def for_each_lista(funcion,lista:list)->None:
    """Recorrer y modificar lista original
    Args:
        funcion (_type_): función que modifica un elemento de la lista
        lista (list): lista que será recorrida y modificada en cada índice por la funcion
    """
    for i in range(len(lista)):
        lista[i] = funcion(lista[i])
           
def mapear_lista(procesadora,lista:list)->list:
    """Crear lista con elementos seleccionados
    Args:
        procesadora:funcion que utiliza un argumento (elemento de la lista)
        lista: De la cual se crea la nueva lista
    Returns:
        lista: Se retonarna una nueva lista
    """
    lista_retorno = []
    for elemento in lista:
        lista_retorno.append(procesadora(elemento))
    return lista_retorno

def filtrar_lista(filtrador,lista:list)->list:
    """Crear nueva lista filtrando lista original con función bool
    Args:
        filtrador: Función que debe ser utilizada como un bool 
        lista: Si se cumple el filtrador, se añade el elemento a la nueva lista
    Returns:
        lista : Se retorna una lista NUEVA con los elementos filtrados
    """
    lista_retorno = []
    for elemento in lista:
        if filtrador(elemento):
                lista_retorno.append(elemento)
    return lista_retorno        

  
def ordenar_lista(funcion_criterio,lista:list):
    """ Args:
        funcion criterio:  compara dos elementos continuos y debe devolver un valor booleano.
        Si se cumple el bool se swapean los elementos
        lista : (list)"""
    TAM = len(lista)
    for i in range(TAM-1):
        for j in range(i+1,TAM):
            if funcion_criterio(lista[i],lista[j]):
                swap_lista(lista,i,j)

def swap_lista(lista:list,i=int,j=int)->None:
    """
    Args:
        lista (list): intercambiar posicion de dos elementos de una lista
        i (int, optional): indice del primer elemento
        j (int, optional): indice del segundo elemento
    """
    aux = lista[i]
    lista[i] = lista[j]
    lista[j] = aux

def imprimir_lista_en_fila(lista:list)->None:
    """Args:
        lista (list):es recorrida para mostrar sus elementos 
        uno por fila"""
    for elemento in lista:
        print(elemento)