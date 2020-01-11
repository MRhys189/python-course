# numbers = [3, 51, 2, 8, 6]
# # numbers.sort(reverse=True) #sorts in descending
# # numbers.sort() sorts in ascending order
# print(sorted(numbers, reverse=True))  # sorted() will not modify original list
# print(numbers)
items = [

    ("Product1", 10),
    ("Product2", 9),
    ("Product3", 12)

]


def sort_item(item):
    return item[1]


items.sort(key=sort_item)
print(items)

# without "key=" in line 19 there is an error which
# is the first parameter of the function
