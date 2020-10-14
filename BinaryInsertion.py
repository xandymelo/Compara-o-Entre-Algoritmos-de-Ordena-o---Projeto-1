from random import shuffle

def binary_search(arr, val, start, end): 

    if start == end: 
        if arr[start] > val: 
            return start 
        else: 
            return start+1
  

    if start > end: 
        return start 
  
    mid = int((start+end)/2)
    if arr[mid] < val: 
        return binary_search(arr, val, mid+1, end) 
    elif arr[mid] > val: 
        return binary_search(arr, val, start, mid-1) 
    else: 
        return mid 
  
def insertion_sort(arr): 
    for i in range(1, len(arr)): 
        val = arr[i] 
        j = binary_search(arr, val, 0, i-1) 
        arr = arr[:j] + [val] + arr[j:i] + arr[i+1:]
    return arr
 

if __name__ == '__main__':
    #printar quantidade de trocas com a lista na forma crescente
    print(insertion_sort(list(range(40))))
    #printar quantidade de trocas com a lista na forma decrescente
    lista_decrescente_40 = list(range(40))
    lista_decrescente_40 = sorted(lista_decrescente_40,reverse=True)
    print(insertion_sort(lista_decrescente_40))
    #printar quantidade de trocas com a lista na forma aleatória
    lista_aleatoria_40 = list(range(40))
    shuffle(lista_aleatoria_40)
    print(insertion_sort(lista_aleatoria_40))
