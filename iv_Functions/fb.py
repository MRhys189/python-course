def fizz_buzz(input):
    if (input % 5) == 0 and (input % 3) == 0:
        return "FizzBuzz"
    else:
        if (input % 5) == 0:
            return "Buzz"
        elif (input % 3) == 0:
            return "Fizz"
        else:
            return input


print(fizz_buzz(input=21))
