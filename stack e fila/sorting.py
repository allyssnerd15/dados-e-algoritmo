

def insertion_sort(lista):
    n = len(lista)
    for i in range(1, n):
        chave = lista[i]
        j = i - 1
        while j >= 0 and lista[j] > chave:
            lista[j+1] = lista[j]
            j = j - 1
        lista[j+1] = chave


def bubble_sort(lista):
    n = len(lista)
    for j in range(n-1):
        for i in range(n - 1):
            if lista[i] > lista[i+1]:
                #troca de elementos nas posições i e i+1
                lista[i], lista[i+1] =  lista[i+1], lista[i]
            


def select_sort(lista):
    n = len(lista)
    for j in range(n-1):
        min_index = j
        for i in range(j, n):
            if lista[i] < lista[min_index]:
                min_index=i
        #Maneira classica de trocar posição em uma lista
        if lista[j] > lista[min_index]:
            aux = lista[j]
            lista[j] = lista[min_index]
            lista[min_index] = aux