def quicksort(set, first, last):
    if first < last:
        pivot = partition(set, first, last)
        quicksort(set, first, pivot - 1)
        quicksort(set, pivot + 1, last)

def partition(values, first, last):
    pivotvalue = values[first]
    lower = first + 1
    upper = last

    done = False
    while not done:
        while lower <= upper and values[lower] <= pivotvalue:
            lower += 1
        while upper >= lower and values[upper] >= pivotvalue:
            upper -= 1
        if (upper < lower):
            done = True
        else:
            temp = values[lower]
            values[lower] = values[upper]
            values[upper] = temp

    temp = values[first]
    values[first] = values[upper]
    values[upper] = temp

    return upper