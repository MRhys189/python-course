# ctr+home: beginning of the file
# ctr+end: end of the file
# alt+up/down: move line up/down(highlight for multiple lines)
# shift+alt+up/down: duplicate line
# ctr+/: convert into comment and vice versa


def multiply(*numbers):
    total = 1
    for number in numbers:
        total *= number
    return total


print("Start")
print(multiply(1, 2, 3))
