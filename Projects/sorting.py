def bubble_sort(arr: list):
    is_sorted = False
    while not is_sorted:
        is_sorted = True
        for i in range(len(arr) - 1):
            if arr[i] > arr[i + 1]:
                is_sorted = False
                tmp = arr[i]
                arr[i] = arr[i + 1]
                arr[i + 1] = tmp
    return arr


def insertion_sort(arr: list):
    is_sorted = False
    while not is_sorted:
        is_sorted = True
        for i in range(len(arr) - 1):
            if arr[i] < arr[i + 1]:
                pass
            else:
                is_sorted = False
                tmp = arr[i]
                arr[i] = arr[i + 1]
                arr[i + 1] = tmp
                break
    return arr


def selection_sort(arr: list):
    for i in range(len(arr)):
        min_index = i
        for j in range(i + 1, len(arr)):
            if arr[j] < arr[min_index]:
                tmp = arr[j]
                arr[j] = arr[min_index]
                arr[min_index] = tmp
    return arr


def merge_sort(arr: list):
    if len(arr) > 1:
        mid = len(arr)//2
        split_arr = [arr[:mid], arr[mid:]]

        # if lists still weren't fully split down go deeper
        merge_sort(split_arr[0])
        merge_sort(split_arr[1])

        # merge and order sub-arrs
        i = j = k = 0
        while i < len(split_arr[0]) and j < len(split_arr[1]):
            if split_arr[0][i] <= split_arr[1][j]:
                arr[k] = split_arr[0][i]
                i += 1
            else:
                arr[k] = split_arr[1][j]
                j += 1
            k += 1

        # Check for dangling values
        while i < len(split_arr[0]):
            arr[k] = split_arr[0][i]
            i += 1
            k += 1

        while j < len(split_arr[1]):
            arr[k] = split_arr[1][j]
            j += 1
            k += 1

    return arr


def partition(array, low, high):
    pivot = array[high]
    i = low - 1
    for j in range(low, high):
        if array[j] <= pivot:
            i = i + 1
            (array[i], array[j]) = (array[j], array[i])

    (array[i + 1], array[high]) = (array[high], array[i + 1])

    return array, i + 1
  
  
# def quick_sort(array, low, high):
#     if low < high:
#         pi = partition(array, low, high)
#         return pi
        # quick_sort(array, low, pi - 1)
        # quick_sort(array, pi + 1, high)

def quick_sort(arr: list, *args):
    if len(arr) > 1:
        pivot = arr[-1]
        i = 0 - 1
        for j in range(0, len(arr) - 1):
            if arr[j] <= pivot:
                i += 1
                (arr[i], arr[j]) = (arr[j], arr[i])
        (arr[i + 1], arr[-1]) = (arr[-1], arr[i + 1])
        arr[:i + 1] = quick_sort(arr[:i + 1])
        arr[i + 1:] = quick_sort(arr[i + 1:])
    return arr