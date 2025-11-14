"""
Enunciado:
Dadas dos listas de elementos, implementa una función llamada
find_intersection(list_1, list_2) que retorne la intersección de ambas listas.

Parámetros:
    list_1 (List): Lista de elementos
    list_2 (List): Lista de elementos

Ejemplo:
    Entrada:
    list_1 = [1, 2, 3, 4, 5]
    list_2 = [4, 5, 6, 7, 8]

    Salida:
    [4, 5]

Enunciat:
Donades dues llistes d'elements, implementa una funció anomenada
find_intersection(list_1, list_2) que retorni la intersecció de les dues llistes.

Paràmetres:
     list_1 (List): Llista d'elements
     list_2 (List): Llista d'elements

Exemple:
     Entrada:
     list_1 = [1, 2, 3, 4, 5]
     list_2 = [4, 5, 6, 7, 8]

     Sortida:
     [4, 5]

"""

list_1 = [1, 2, 3, 4, 5]
list_2 = [4, 5, 6, 7, 8]


def find_intersection(list_1, list_2):
    intersection = []
    i = 0
    intersection_found = False
    for value in list_1:
        if value == list_2[i]:
            intersection_found = True
            intersection.append(value)
            i += 1
        else:
            if intersection_found == True:
                intersection = []
                intersection_found = False
                i = 0
                if value == list_2[i]:
                    intersection_found = True
                    intersection.append(value)
                    i += 1
    return intersection


# Si quieres probar tu código, descomenta las siguientes líneas y ejecuta el script
# Si vols provar el teu codi, descomenta les línies següents i executa l'script

print(find_intersection([1, 2, 3, 4], [3, 4, 5, 6]))
print(find_intersection(['apple', 'banana', 'orange'], ['banana', 'kiwi', 'apple']))