from random import shuffle
def mergesort(lista, inicio=0, fim=None):
    contador = 0
    if fim is None:
        fim = len(lista)
    if(fim - inicio > 1):
        meio = (fim + inicio)//2
        contador += 1
        x = mergesort(lista, inicio, meio)
        contador += x
        y = mergesort(lista, meio, fim)
        contador += y
        z = merge(lista, inicio, meio, fim)
        contador += z

    return contador

def merge(lista, inicio, meio, fim):
    cont = 0
    left = lista[inicio:meio]
    right = lista[meio:fim]
    top_left, top_right = 0, 0
    for k in range(inicio, fim):
        if top_left >= len(left):
            lista[k] = right[top_right]
            top_right = top_right + 1
            cont += 1
        elif top_right >= len(right):
            lista[k] = left[top_left]
            top_left = top_left + 1
            cont += 1
        elif left[top_left] < right[top_right]:
            lista[k] = left[top_left]
            top_left = top_left + 1
            cont += 1
        else:
            lista[k] = right[top_right]
            top_right = top_right + 1
            cont += 1
    return cont


if __name__ == '__main__':
    #printar quantidade de trocas com a lista na forma crescente
    print(mergesort(list(range(10000))))
    #printar quantidade de trocas com a lista na forma decrescente
    lista_decrescente_40 = list(range(10000))
    lista_decrescente_40 = sorted(lista_decrescente_40,reverse=True)
    print(mergesort(lista_decrescente_40))
    #printar quantidade de trocas com a lista na forma aleatória
    lista_aleatoria_40 = list(range(10000))
    shuffle(lista_aleatoria_40)
    print(mergesort(lista_aleatoria_40))