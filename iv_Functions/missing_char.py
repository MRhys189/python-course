def missing_char(str: str, n: int):
    unpacked = [*str]
    unpacked[n] = ''
    new_str = ''
    return new_str.join(unpacked)


print(missing_char('code', 2))

# solution


def missing_char2(str: str, n: int):
    front = str[:n]
    back = str[n+1:]
    return front + back


print(missing_char2('howaboutthat', 5))

# Given a string, return a new string 
# where the first and last chars have been exchanged.


def front_back(str: str):
    unpacked = [*str]
    first, *others, last = unpacked
    new_list = [last, *others, first]
    new_str = ''
    return new_str.join(new_list)


print(front_back('prevalent'))


def front_back2(str):
    if len(str) > 1:
        front = str[0]
        back = str[-1]
        middle = str[1:-1]
        return back + middle + front
    else:
        return str


print(front_back2('a'))

# solution


def front_back3(str):
    if len(str) <= 1:
        return str

    mid = str[1:len(str)-1]
    # last + mid + first
    return str[len(str)-1] + mid + str[0]  # can be written as str[1:-1]

# Given a string, we'll say that the front is the first 
# 3 chars of the string. If the string length is less than 3, 
# the front is whatever is there. 
# Return a new string which is 3 copies of the front.


def front3(str):
    if len(str) <= 3:
        return str*3
    else:
        return str[:3] * 3

print(front3("rhys"))

#solution
def front3_2(str):
  # Figure the end of the front
  front_end = 3
  if len(str) < front_end:
    front_end = len(str)
  front = str[:front_end]
  return front + front + front 

# Could omit the if logic, and write simply front = str[:3]
  # since the slice is silent about out-of-bounds conditions.
