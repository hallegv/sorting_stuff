items = ["hey", "hey", "you", "you", "whats", "up", "omg"]

def find_max(items):
    if len(items) = 1:
        return items[0]

    option1 = items[0]
    option2 = find_max(items[1:])

    if option1 > option2:
        return option1
    else:
        return option2