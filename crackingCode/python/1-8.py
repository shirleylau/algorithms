
import math

s1 = 'peanutbutter'
s2 = 'terpeanutbut'

halfLen = int(math.floor(len(s1)/2))
head = s1[:halfLen]
tail = s1[-halfLen:]

try:
    index = s2.index(head)
except:
    try:
        index = s2.index(tail) + halfLen
    except:
        print'Nope'

if index:
    print s2[index:] + s2[:index]
