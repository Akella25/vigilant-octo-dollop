def bubble_sort(array, field):
    n = len(array)
    for i in range(n-1):
        for j in range(0, n-i-1):
            if getattr(array[j], field) > \
                getattr(array[j + 1], field):
                array[j], array[j + 1] = array[j + 1], array[j]