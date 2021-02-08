def is_sorted(list):
   # nice one ! i love booleans 
    return all(list[i] <= list[i + 1] for i in range(len(list) - 1))

# brute force (blech)
    # for i in range(0, len(list) - 1):
    #     if list[i] > list[i + 1]:
    #         return False
    # return True  
