person = {"name": "Jess", "age": 23, "job": "Programmer"}
person = {"name": "Jess", "age": 23}

# Look before you leap(LBYL) (Non-pythonic)
if "name" in person and "age" in person an "job" in person:
    print("I'm {name}. I'm {age} years old and I am a {job}".format(**person))
else:
    print("Missing some keys")

# #EAFP (Pythonic)
# try:
#     print("I'm {name}. I'm {age} years old and I am a {job}".format(**person))
# except KeyError as e:
#     print("Missing {} key".format(e))
