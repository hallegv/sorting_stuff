# this ones my favorite 

def binarysearch(item, list): 
    lower = 0
    upper = len(list) - 1

    while lower <= upper:
        midpoint = (lower + upper) // 2

        if list[midpoint] == item:
            return midpoint
        
        if item > list[midpoint]:
            lower = midpoint + 1
        else:
            upper = midpoint - 1

    if lower > upper:
        return None
