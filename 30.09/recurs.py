# Реалізувати функцію merge_sort, яка при досягенні глибини рекурсії == 3
# буде виконувати сортування підсписку вставками (insertion_search)
import random


def insertion_sort(array):
    for i in range(1, len(array)):
        element = array[i]
        j = i - 1
        while j >= 0 and element < array[j]:
            array[j + 1] = array[j]
            j -= 1
        array[j + 1] = element


stop = 3


def merge_sort(arr, stop, i=0):
    i += 1
    if i != stop:
        if len(arr) > 1:
            mid = len(arr) // 2
            left = arr[:mid]
            right = arr[mid:]
            merge_sort(left, i)
            merge_sort(right, i)
            i = 0
            j = 0
            k = 0

            while i < len(left) and j < len(right):
                if left[i] <= right[j]:
                    arr[k] = left[i]
                    i += 1
                else:
                    arr[k] = right[j]
                    j += 1
                k += 1

            while i < len(left):
                arr[k] = left[i]
                i += 1
                k += 1

            while j < len(right):
                arr[k] = right[j]
                j += 1
                k += 1
    else:
        insertion_sort(arr)


rand_list = [random.randint(1, 100) for i in range(20)]
print(rand_list)
merge_sort(rand_list, stop)
print(rand_list)
