items = [

    ("Product1", 10),
    ("Product2", 9),
    ("Product3", 12)

]


prices = list(map(lambda item: item[1], items))
print(prices)

print(lambda x: x[1] for x in items)
