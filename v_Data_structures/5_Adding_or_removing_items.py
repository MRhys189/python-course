letters = ["a", "b", "c"]

# Add
letters.append("d")
letters.insert(0, "-")

# remove
letters.pop(0)
letters.remove("b")  # removes the first occurence where there are multiple one
del letters[0:3]
# letters.clear():removes everything from the list
print(letters)
