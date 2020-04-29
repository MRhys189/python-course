def missing_char(str, n):
    list_name = [*str]
    print(list_name)
    for letter in list_name:
        list_name[n]=letter

    return list_name[0:]


print(missing_char('floor', 0))


# def fizz_buzz(input):
#     if (input % 5) == 0 and (input % 3) == 0:
#         return "FizzBuzz"
#     else:
#         if (input % 5) == 0:
#             return "Buzz"
#         elif (input % 3) == 0:
#             return "Fizz"
#         else:
#             return input


# print(fizz_buzz(input=21))
