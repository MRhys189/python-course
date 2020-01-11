message = "a"
# avoid global variables because they stay in memory for a long time
# create functions with local variables as best practice
# do not modify global variables in functions


def greet(name):
    global message
    message = "b"


greet("Mosh")
print(message)
