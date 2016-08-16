# Find factors of num
# Is it prime?

num = 13195
x = num
factor = 0

while factor is 0 and x > 2:
    x -= 1
    if num % x == 0: # Determines factor
        y = x
        isPrime = True
        while y > 2:
            y -= 1
            if x % y == 0:
                isPrime = False
        if isPrime:
            factor = y
            print(y)

answer = 29

print(factor)
print(answer == sum)
