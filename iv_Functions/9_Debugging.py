def multiply(*numbers):
    total = 1
    for number in numbers:
        total *= number
    return total


# Sh+f5: exit debugger
# fn+f9: to insert/remove a breakpoint
# fn+f5: start/stop debugger upto point where there's a breakpoin
# fn+f10: execute line by line
# fn+f11: step into the function that you've defined(here it's line 13 i.e multiply)
print("Start")
print(multiply(1, 2, 3))

# the breakpoint need not be placed at the first line of program
# put it in line 2
