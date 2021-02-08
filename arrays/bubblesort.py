def bubblesort(set): 
    # countdown from end of array
    for i in range(len(set) - 1, 0, -1):
        for j in range(i):
            if set[j] > set[j + 1]:
                temp = set[j]
                set[j] = set[j + 1]
                set[j + 1] = temp