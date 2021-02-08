def mergesort(set):
    if len(set) > 1:
        mid = len(set) // 2
        leftarray = set[:mid]
        rightarray = set[mid:]

        # recursively split the arrays
        mergesort(leftarray)
        mergesort(rightarray)

        # merge results
        i=0
        j=0
        k=0

        # check greater value of the two
        while i < len(leftarray) and j < len(rightarray):
            if leftarray[i] < rightarray[i]:
                set[k] = leftarray[i]
                i += 1
            else:
                set[k] = rightarray[i]
                j += 1
            k += 1

        # add leftarray values
        while i < len(leftarray):
            dataset[k] = leftarray[i]
            i += 1
            k +=1

        # add rightarray values
        while j < len(rightarray):
            dataset[k] = rightarray[j]
            j += 1
            k +=1         