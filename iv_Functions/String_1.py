# Basic python string problems -- no loops.
#  Use + to combine strings, len(str) is the number of chars in a String, 
# str[i:j] extracts the substring starting at index i and running up 
# to but not including index j.

#1)Hello_name
#Given a string name, e.g. "Bob", return a greeting of the form "Hello Bob!" 
# output is:
# hello_name('Bob') → 'Hello Bob!'
# hello_name('Alice') → 'Hello Alice!'
# hello_name('X') → 'Hello X!'

def hello_name(name):
    return 'Hello'+' '+ name + '!'

print(hello_name('Rhys'))

#Solution
def hello_name2(name):
  return "Hello " + name + "!"


#Q2 make_abba
#Given two strings, a and b, return the result of 
# putting them together in the order abba, e.g. 
# "Hi" and "Bye" returns "HiByeByeHi"
#Output is:
#make_abba('Hi', 'Bye') → 'HiByeByeHi'
# make_abba('Yo', 'Alice') → 'YoAliceAliceYo'
# make_abba('What', 'Up') → 'WhatUpUpWhat'

def make_abba(a,b):
    return a+b+b+a

print(make_abba("Hi","you"))
#solution was the same

#Q3) make_tags
# The web is built with HTML strings like "<i>Yay</i>" 
# which draws Yay as italic text. 
# In this example, the "i" tag makes <i> and </i> 
# which surround the word "Yay". 
# Given tag and word strings, create the HTML string with tags around the word,
# e.g. "<i>Yay</i>
#output is:
# make_tags('i', 'Yay') → '<i>Yay</i>'
# make_tags('i', 'Hello') → '<i>Hello</i>'
# make_tags('cite', 'Yay') → '<cite>Yay</cite>'

