#Función Quicksort. Pivot: primer valor. 

contador_primero = 0

def quicksort(arr):
    global contador_primero            
    contador_primero += 1

    if len(arr) <= 1:
        return arr
    else:
        pivot = arr[0]
        less = [x for x in arr[1:] if x <= pivot]
        greater = [x for x in arr[1:] if x > pivot]
        return quicksort(less) + [pivot] + quicksort(greater)
    
def get_contador_primero():
    return contador_primero

#Función Quicksort_media. Pivot: media de tres valores: el primero, el último y el del medio.


def mediana_de_tres(a, b, c):
    return sorted([a, b, c])[1]

contador_mediana = 0

def quicksort_mediana(arr):
    global contador_mediana
    contador_mediana += 1

    if len(arr) <= 1:
        return arr
    else:
        primero = arr[0]
        medio = arr[len(arr) // 2]
        ultimo = arr[-1]
        pivot = mediana_de_tres(primero, medio, ultimo)

        less = [x for x in arr if x < pivot]
        equal = [x for x in arr if x == pivot]
        greater = [x for x in arr if x > pivot]

        return quicksort_mediana(less) + equal + quicksort_mediana(greater)
    
def get_contador_mediana():
    return contador_mediana