numbers = [1, 1, 2, 3, 4]
first = set(numbers)
second = {1, 5}

print(first | second)  # union of sets and no duplicates
print(first & second)  # intersection of sets
print(first - second)  # elements only in the first set
print(second - first)  # elements only in the second set
print(first ^ second)  # elements in first or second set but not both

if 1 in first:
    print("Yes")
