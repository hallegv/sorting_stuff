items = ["hey", "hey", "you", "you", "whats", "up", "omg"]

counter = dict()

for item in items:
    if(item in counter.keys()):
        counter[item] += 1
    else:
        counter[item] = 1

print(counter)