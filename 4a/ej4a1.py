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


def find_intersection_for(list_1, list_2):
    interseccion = []
    if not list_1 or not list_2:
        return set()
    else:
        try:
            for i in list_1:
                if i in list_2:
                    interseccion.append(i)
            if len(interseccion) > 0:
                return set(interseccion)
            else:
                return set()
        except Excepcion as error:
            return f"Ha habido un error: {error}"
    
def find_intersection_while(list_1, list_2):
    interseccion = []
    if not list_1 or not list_2:
        return set()
    else:
        try:
            i = 0
            while i < len(list_1):
                if list_1[i] in list_2:
                    interseccion.append(list_1[i])
                i += 1
            if len(interseccion) > 0:
                return set(interseccion)
            else:
                return set()
        except Excepcion as error:
            return f"Ha habido un error: {error}"


# Si quieres probar tu código, descomenta las siguientes líneas y ejecuta el script
# Si vols provar el teu codi, descomenta les línies següents i executa l'script
vacia = []
print(find_intersection_for([1, 2, 7, 3, 6],[3, 4, 5, 6]))
# print(find_intersection_while(['apple', 'banana', 'orange'], ['banana', 'kiwi', 'apple']))
