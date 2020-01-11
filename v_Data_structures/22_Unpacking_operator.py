# first = [1, 2]
# second = [3]

# values = [*first, *second, * "Hello"]
# print(values)

first = dict(x=1)
second = dict(x=10, y=2)
combined = {**first, **second, "z": 1}
print(combined)
