# fizz_buzz algorithm


def fizz_buzz(input):
    if (input*3) % 5 == 0:
        return "FizzBuzz"
    if input % 3 == 0:
        return "Fizz"
    if input % 5 == 0:
        return "Buzz"
    else:
        return input


# no need for "else"; just put "return input"
print(fizz_buzz(555555))
