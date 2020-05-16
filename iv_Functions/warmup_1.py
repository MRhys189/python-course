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

#The parameter weekday is True if it is a weekday, 
# and the parameter vacation is True if we are on vacation. 
# We sleep in if it is not a weekday or we're on vacation. 
# Return True if we sleep in.

def sleep_in(weekday,vacation):
    if weekday and vacation:
        return True
    elif weekday and not vacation:
        return False
    else:
        return True

#solution
def sleep_in2(weekday, vacation):
  if not weekday or vacation:
    return True
  else:
    return False
  # This can be shortened to: return(not weekday or vacation)


#We have two monkeys, a and b, and the parameters a_smile and b_smile
#  indicate if each is smiling. 
# We are in trouble if they are both 
# smiling or if neither of them is smiling. 
# Return True if we are in trouble.

def monkey_trouble(a_smile,b_smile):
    if a_smile and b_smile or not (a_smile and b_smile):
        return True
    else:
        return False

# solution
def monkey_trouble2(a_smile, b_smile):
  if a_smile and b_smile:
    return True
  if not a_smile and not b_smile:
    return True
  return False
  ## The above can be shortened to:
  ##   return ((a_smile and b_smile) or (not a_smile and not b_smile))
  ## Or this very short version (think about how this is the same as the above)
  ##   return (a_smile == b_smile)