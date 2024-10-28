# Função Quick Sort
def quick_sort(lista):
    # Caso base: lista com 0 ou 1 elemento já está ordenada
    if len(lista) <= 1:
        return lista
    
    # Escolhendo o último elemento como pivô
    pivô = lista[-1]
    
    # Separando os elementos em menores e maiores que o pivô
    menores = [x for x in lista[:-1] if x <= pivô]
    maiores = [x for x in lista[:-1] if x > pivô]
    
    # Chamada recursiva para ordenar cada parte e combiná-las
    return quick_sort(menores) + [pivô] + quick_sort(maiores)

# Testando a função
numeros = [29, 10, 14, 37, 13]
numeros_ordenados = quick_sort(numeros)

# Exibindo o resultado
print("Lista ordenada:", numeros_ordenados)
