import time
import timeit
import sys
from modulo import get_contador_primero, quicksort, quicksort_media, get_contador_media

sys.setrecursionlimit(20000)

#Método Quicksort con lista ordenada y el primer valor como pivote 

A = list(range(1, 1001))
print(quicksort(A))

time.sleep(5)

#Método Quicksort con lista ordenada y la media entre 3 valores como pivote. Esos 3
#valores son el primer valor, el ultimo y el del medio. 

B = list(range(1, 1001))
print(quicksort_media(B))

time.sleep(5)

# Medir tiempo y llamadas recursivas para cada pivote: 
start_time = timeit.default_timer()
quicksort(A.copy())
end_time = timeit.default_timer()
print("Tiempo para una lista con pivote en primer elemento:", end_time - start_time)
print("Llamadas recursivas (pivote primero):", get_contador_primero())


start_time_media = timeit.default_timer()
quicksort_media(B.copy())
end_time_media = timeit.default_timer()
print("Tiempo para una lista con pivote en la media de 3:", end_time_media - start_time_media)
print("Llamadas recursivas (pivote media de 3):", get_contador_media())