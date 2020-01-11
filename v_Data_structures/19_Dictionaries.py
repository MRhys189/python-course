# point = {"x":1, "y":2}
point = dict(x=1, y=2)  # better approach than line 1
# the index is the name of the key thus we can't access the key value using numeric index
print(point["x"])
point["x"] = 10  # changes the value
point["z"] = 20  # adds another value
print(point)  # the index is the name of the key
if "a" in point:
    print(point["a"])
print(point.get("a", 0))  # if key doesn't exist(a) it returns 0
del point["x"]
print(point)
for key, value in point.items():  # for each iteration the loop variable holds the key
    print(key, value)  # creates a tuple
