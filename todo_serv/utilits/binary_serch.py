def binary_search(array, element, low=None, high=None):
    if low is None and high is None:
        low = 0
        high = len(array) - 1

    if high >= low:
        mid = (high + low) // 2

        if array[mid] == element:
            return array[mid]
        elif array[mid] > element:
            return binary_search(array, element, low, mid - 1)
        else:
            return binary_search(array, element, mid + 1, high)
    else:
        return None
