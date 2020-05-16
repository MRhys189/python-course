numbers = [1, 2, 3, 4, 4, 4, 4, 9]
first, *other, last = numbers
print(first, last)
print(other)
print(numbers[-1])

# below is the less clean version of the above code
# first = numbers[0]
# second = numbers[1]
# third = numbers[2]....etc
