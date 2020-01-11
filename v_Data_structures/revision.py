# letters = ["a", "b", "c"]
# items = (0, "a")
# index, letter = items
# for letter, index in enumerate(letters):
#     print(index, letter)

# letters = ["a", "b", "c"]
# letters.append("d")
# print(letters)
# letters.insert(2, "z")
# print(letters)
# letters.remove("z")
# print(letters)

# numbers = [3, 51, 2, 8, 6]
# # numbers.sort(reverse=True)
# print(sorted(numbers, reverse=True ))
# print(numbers)

# items = [
#     ("Product1", 10),
#     ("Product2", 9),
#     ("Product3", 12),

# ]

# Labmda functions
# def sort_item(item):
#     return item[1]


# items.sort(key=lambda item: item[1])
# print(items)


# Map functions
from sys import getsizeof
from array import array
from collections import deque
items = [
    ("Product1", 10),
    ("Product2", 9),
    ("Product3", 12),

]

# prices = []
# for item in items:
#     prices.append(item[1])
# print(prices)
# using lambda function instead below
# prices = list(map(lambda item: item[1], items))
# print(prices)


# Filter functions
items = [
    ("Product1", 10),
    ("Product2", 9),
    ("Product3", 12),

]

# filtered = []
# for item in items:
#     if item[1] <= 10:
#         filtered.append(item[1])
# print(filtered)

# filtered = list(filter(lambda item: item[1] >= 10, items))
# print(filtered)


# Comprehension
items = [
    ("Product1", 10),
    ("Product2", 9),
    ("Product3", 12),

]
# prices = list(map(lambda item: item[1], items))
prices = [item[1] for item in items]
print(prices)

# filtered = list(filter(lambda item: item[1] >= 10, items))
filtered = [item[1] for item in items if item[1] >= 10]
print(filtered)

# zip functions
list1 = [1, 2, 3]
list2 = [10, 20, 30]
print(list(zip("abc", list1, list2)))

# stacks
browsing_session = []
browsing_session.append(1)
browsing_session.append(2)
browsing_session.append(3)
print(browsing_session)
last = browsing_session.pop()
print(last)
print(browsing_session)
print("redirect", browsing_session[-1])

#  Queues
queue = deque([])
queue.append(1)
queue.append(2)
queue.append(3)
queue.popleft()
print(queue)

# Tuples
point = tuple([1, 2, 3])
print(point[0])

x, y, z = point
if 10 in point:
    print("exists")

# Swapping variables
x = 10
y = 11

x, y = y, x
print("x", x)
print("y", y)

# Arrays

array("i", [1, 2, 3])

# sets
numbers = [1, 1, 2, 3, 4]
uniques = set(numbers)
set1 = {1, 2}
set2 = {3, 4}
print(set1 | set2)

if 1 in set1:
    print("yes")

# Dictionaries
point = {"x": 1, "y": 2}
point = dict(x=1, y=2)
point["z"] = 20
for key in point:
    print(key, point[key])

for key, value in point.items():
    print(key, value)

# Dictionary comprehensions

values = {x: (x*2) for x in range(5)}
print(values)

# Generator objects
values = ((x*2) for x in range(1000))
print("gen:", getsizeof(values))

# Unpacking operator
numbers = [1, 2, 3]
print(numbers)
values = list(range(5))
values = [*range(5), *"Hello"]
print(values)

first = {"x": 1}
second = {"x": 10, "y": 2}
combined = {**first, **second, "z": 1}
print(combined)
