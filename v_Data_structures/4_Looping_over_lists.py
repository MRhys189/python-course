letters = ["a", "b", "c"]
items = (0, "a")
index, letter = items  # with brackets items is a tuple
# the enumerate() will return a tuple like line 2 which can then be unpacked on the same line
for index, letter in enumerate(letters):
    print(index, letter)
