# Design  an  algorithm  and  write  code  to  remove  the  duplicate
# characters  in  a  string without using any additional buffer. NOTE: One or
# two additional variables are fine. An extra copy of the array is not.
#
# FOLLOW UP: Write the test cases for this method.

string = 'banana'
newString = ''

i = 0

while i < len(string):
    char = string[i]
    try:
        newString.index(char)
    except:
        newString = newString + char
    i += 1

print newString
