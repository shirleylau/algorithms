# Implement an algorithm to determine if a string has all unique characters.
# What if you can not use additional data structures??

string = 'banana'

ordered = ''.join(sorted(string))

prev = ''
redundant = []

for char in ordered:
    if char == prev:
        redundant.append(char)
    prev = char

print len(redundant) == 0
