def greet(name):
    print(f"Hi {name}")


# 1- Perform a task e.g greet(),print()
# 2- Return a value e.g round(1.9)

def get_greeting(name):  # this is better than the first part
    return f"Hi {name}"


message = get_greeting("Mosh")
print(message)
