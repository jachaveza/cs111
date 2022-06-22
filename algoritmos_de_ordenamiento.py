import time

def insertion_sort(A):
    for j in range(1, len(A)):
        key = A[j]
        # Commentario
        i   = j - 1
        while i >= 0 and key < A[i]:
            print("Dentro del bucle WHILE")
            A[i + 1] = A[i]
            i = i - 1
        A[i+1] = key
    return A

def bubble_sort(L):
    n = len(L)
    for i in range(n):
        for j in range(n-1, i,-1):
            if L[j] < L[j-1]:
                temporal = L[i]
                L[i] = L[j-1]
                L[i-1] = temporal
    return L

A = [2,4,5,6,7,8,9,11,13]
B = A[::-1]
t_inicio = time.time()
print(insertion_sort(A))
t_final = time.time()
print("tiempo = {:.6f}".format(t_final - t_inicio))


print(bubble_sort(A))

