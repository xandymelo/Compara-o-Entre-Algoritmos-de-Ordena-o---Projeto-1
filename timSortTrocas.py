from random import shuffle
def insertion_sort(array, left=0, right=None):
    contador = 0
    if right is None:
        right = len(array) - 1

    for i in range(left + 1, right + 1):

        key_item = array[i]


        j = i - 1


        while j >= left and array[j] > key_item:

            array[j + 1] = array[j]
            j -= 1
            contador += 1


        array[j + 1] = key_item

    return [array,contador]


def merge(left, right):
    contador = 0
    if len(left) == 0:
        return right


    if len(right) == 0:
        return left

    result = []
    index_left = index_right = 0


    while len(result) < len(left) + len(right):

        if left[index_left] <= right[index_right]:
            result.append(left[index_left])
            contador += 1
            index_left += 1
        else:
            result.append(right[index_right])
            index_right += 1
            contador += 1


        if index_right == len(right):
            result += left[index_left:]
            break

        if index_left == len(left):
            result += right[index_right:]
            break

    return [result,contador]



def timsort(array):
    contador = 0
    min_run = 32
    n = len(array)


    for i in range(0, n, min_run):
        contador += insertion_sort(array, i, min((i + min_run - 1), n - 1))[1]


    size = min_run
    while size < n:

        for start in range(0, n, size * 2):

            midpoint = start + size - 1
            end = min((start + size * 2 - 1), (n-1))


            merged_array = merge(
                left=array[start:midpoint + 1],
                right=array[midpoint + 1:end + 1])
            contador += merged_array[1]


            #array[start:start + len(merged_array)] = merged_array[0]


        size *= 2

    return [array,contador]

if __name__ == '__main__':
    #printar quantidade de trocas com a lista na forma crescente
    print(timsort(list(range(10000)))[1])
    #printar quantidade de trocas com a lista na forma decrescente
    lista_decrescente_40 = list(range(10000))
    lista_decrescente_40 = sorted(lista_decrescente_40,reverse=True)
    print(timsort(lista_decrescente_40)[1])
    #printar quantidade de trocas com a lista na forma aleatória
    lista_aleatoria_40 = list(range(10000))
    shuffle(lista_aleatoria_40)
    print(timsort(lista_aleatoria_40)[1])
