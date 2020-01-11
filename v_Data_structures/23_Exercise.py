sentence = "This is a common interview question"

characters = [*sentence]
# print(characters)

# for char in characters:
#     print(char, characters.count(char))

characters2 = [characters.count(char) for char in characters]
characters3 = [char*1 for char in characters]
print(max(characters3.count(characters)), max(characters2))
