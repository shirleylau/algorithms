x = 0
sum = 0

for x in range(0, 10):
    print(x)
    if x != 0 and x % 3 == 0 or x % 5 == 0:
        sum = sum + x

print(sum)
