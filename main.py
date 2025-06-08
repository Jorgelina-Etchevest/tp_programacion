import time
import timeit

#Método Quicksort con lista ordenada y el primer valor como pivote 

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


# Lista 
A = list(range(1, 101))
print(quicksort(A))

time.sleep(15)

#Método Quicksort con lista ordenada y la media entre 3 valores como pivote. Esos 3
#valores son el primer valor, el ultimo y el del medio. 

def mediana_de_tres(a, b, c):
    return sorted([a, b, c])[1]

contador_media = 0

def quicksort_media(arr):
    global contador_media
    contador_media += 1

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

        return quicksort_media(less) + equal + quicksort_media(greater)

B = list(range(1, 101))
print(quicksort_media(B))

time.sleep(15)

# Medir tiempo y llamadas recursivas para cada pivote: 
start_time = timeit.default_timer()
quicksort(A.copy())
end_time = timeit.default_timer()
print("Tiempo para una lista con pivote en primer elemento:", end_time - start_time)
print("Llamadas recursivas (pivote primero):", contador_primero)


start_time = timeit.default_timer()
quicksort_media(B.copy())
end_time = timeit.default_timer()
print("Tiempo para una lista con pivote en la media de 3:", end_time - start_time)
print("Llamadas recursivas (pivote media de 3):", contador_media)