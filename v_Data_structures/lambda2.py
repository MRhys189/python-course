# A REGULAR FUNCTION
def guru(funct, *args):
    funct(*args)


def printer_one(arg):
    return print(arg)


def printer_two(arg):
    print(arg)


# CALL A REGRULAR FUNCTION
guru(printer_one, "printer 1 REGULAR CALL")
guru(printer_one, "printer 1 REGULAR CALL")
# CALL A REGULAR FUNCTION THROUGH A LAMDA
guru(lambda: printer_one('printer 1 LAMBDA CALL'))
guru(lambda: printer_two('printer 2 LAMBDA CALL'))
