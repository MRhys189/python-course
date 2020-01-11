h_letters = []

for letter in 'humans':
    h_letters.append(letter)
print(h_letters)
h_letters = [letter for letter in "human"]
print(h_letters)

# comprehensions with conditionals

number_list = [x for x in range(20) if x % 2 == 0]
print(number_list)

number_list = []
for x in range(20):
    if x % 2 == 0:
        number_list.append(x)
print(number_list)
