def greet(name):
    print(f"Hi {name}")
#this can't be reused


# 1- Perform a task e.g greet(),print()
# 2- Return a value e.g round(1.9)

def get_greeting(name):  # this is better than the first part
    return f"Hi {name}"
#returns a value which can be assigned to a variable

message = get_greeting("Mosh")
print(message)
