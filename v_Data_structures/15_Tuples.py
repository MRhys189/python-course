point = 1, 2  # or point=(1,2) for python to read it as a tuple
point2 = (1, 2) + (3, 4)
# print(type(point))
# print(type(point))
point3 = tuple([1, 2, 3, 4])
print(point3)
print(point3[0:2])
w, x, y, z = point3
if 10 in point3:
    print("exists")
else:
    print("It doesn't exist")
