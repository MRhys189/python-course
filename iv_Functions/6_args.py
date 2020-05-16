def multiply(*numbers):
    total = 1
    for number in numbers:
        total *= number
    return total


print(multiply(2, 3, 4, 5))

message = 'you are great'
unpacked = [*message]
print(range(len(message)))

unpacked[0] = ''
print(unpacked)
new_str = ''
print(new_str.join(unpacked))