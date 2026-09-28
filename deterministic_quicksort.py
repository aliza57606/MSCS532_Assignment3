def partition_first(arr, low, high):
    pivot = arr[low]
    i = low + 1

    for j in range(low + 1, high + 1):
        if arr[j] <= pivot:
            arr[i], arr[j] = arr[j], arr[i]
            i += 1
    arr[low], arr[i - 1] = arr[i - 1], arr[low]
    return i - 1

def deterministic_quicksort(arr, low, high):
    if low < high:
        pivot_index = partition_first(arr, low, high)

        deterministic_quicksort(arr, low, pivot_index - 1)
        deterministic_quicksort(arr, pivot_index + 1, high)

if __name__ == "__main__":
    test_arrays = [
        [3, 9, 8, 5, 1, 7],
        [1, 2, 3, 4, 5],
        [5, 4, 3, 2, 1],
        [4, 2, 4, 1, 2, 4],
        []
    ]

    for arr in test_arrays:
        deterministic_quicksort(arr, 0, len(arr) - 1)
        print(arr)