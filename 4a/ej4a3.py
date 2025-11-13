"""
Enunciado:

Escribe una función llamada 'descending_list_iterator(numbers_list)' que tome una lista
de números como argumento y devuelva un iterador que genere los mismos
números de mayor a menor.

Parámetros:
    numbers_list (list): Lista de números enteros a ser ordenados.

Ejemplo:
    Entrada:
    [5, 1, 8, 3, 2]

    Salida:
    El iterador debería generar los números en el siguiente orden:
    8, 5, 3, 2, 1.

Enunciat:

Escriu una funció anomenada 'descending_list_iterator(numbers_list)' que prengui una llista
de números com a argument i torni un iterador que generi els mateixos
nombres de més gran a més petit.

Paràmetres:
     numbers_list (list): Llista de nombres enters a ser ordenats.

Exemple:
     Entrada:
     [5, 1, 8, 3, 2]

     Sortida:
     L'iterador hauria de generar els números en l'ordre següent:
     8, 5, 3, 2, 1.

"""


def descending_list_iterator(numbers_list:float):    # amb funció recursiva
    lista_local = numbers_list.copy()

    if not lista_local:
        return lista_local
    try:
        maxi = max(lista_local)
        lista_local.remove(maxi)
        return [maxi] + descending_list_iterator(lista_local)
    except TypeError:
        raise TypeError("Los valores de numbers_list deben ser int/float")


def descending_list_for(numbers_list):              # amb FOR
    lista_local = numbers_list.copy()

    if not lista_local:
        return lista_local
    
    nueva_lista = []
    try:
        for i in range(len(numbers_list)):
            nueva_lista.append(max(lista_local))
            lista_local.remove(max(lista_local))
        return nueva_lista
    except TypeError:
        raise TypeError("Los valores de numbers_list deben ser int/float")
    



# Si quieres probar tu código, descomenta las siguientes líneas y ejecuta el script
# Si vols provar el teu codi, descomenta les línies següents i executa l'script

numeros = [2, 3, 6, 9, 11, 12, 15, 18,6]
print(list(descending_list_iterator(numeros)))
print(descending_list_for(numeros))
