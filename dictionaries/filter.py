filter = dict()

items = ["hey", "hey", "you", "you", "whats", "up"]

for key in items:
    filter[key] = 0

result = set(filter.keys())
print(result)