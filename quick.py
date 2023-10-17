import random

def partition(arr, low, high):
    # Escolhe um índice aleatório entre low e high
    random_index = random.randint(low, high)
    
    # Troca o elemento aleatório com o último elemento para usá-lo como pivô
    arr[random_index], arr[high] = arr[high], arr[random_index]
    
    pivot = arr[high]
    i = low - 1

    for j in range(low, high):
        if arr[j] < pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]

    arr[i + 1], arr[high] = arr[high], arr[i + 1]
    return i + 1

def quicksort(arr, low, high):
    if low < high:
        pivot = partition(arr, low, high)
        quicksort(arr, low, pivot - 1)
        quicksort(arr, pivot + 1, high)

# Exemplo de uso:
arr = [10, 7, 8, 9, 1, 5]
quicksort(arr, 0, len(arr) - 1)
print("Matriz ordenada:", arr)