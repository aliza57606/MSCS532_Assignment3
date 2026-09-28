import random
def partition(arr, low, high):
    pivot = arr[high]
    i = low - 1
    for j in range(low, high):
        if arr[j] <= pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]
    arr[i + 1], arr[high] = arr[high], arr[i + 1]
    return i + 1  

def randomized_partition(arr, low, high):
    random_index = random.randint(low, high)

    arr[random_index], arr[high] = arr[high], arr[random_index]

    return partition(arr, low, high)  

def randomized_quicksort(arr, low, high):
    if low < high:
        pivot_index = randomized_partition(arr, low, high)

        randomized_quicksort(arr, low, pivot_index - 1)
        randomized_quicksort(arr, pivot_index + 1, high)

if __name__ == "__main__":
    test_arrays = [
        [3, 9, 8, 5, 1, 7],
        [1, 2, 3, 4, 5],
        [5, 4, 3, 2, 1],
        [4, 2, 4, 1, 2, 4],
        []
    ]

    for arr in test_arrays:
        randomized_quicksort(arr, 0, len(arr) - 1)
        print(arr)