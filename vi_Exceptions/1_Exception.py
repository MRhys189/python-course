try:
    file = open("1_Exception.py")
    age = int(input("Age:"))
    xfactor = 10/age
except (ValueError, ZeroDivisionError):
    print("You didn't enter a valid age")
else:
    print("No exception were thrown")
finally:
    file.close()
