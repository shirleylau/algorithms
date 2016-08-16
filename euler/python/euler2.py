x = 1
y = 1
sum = 0

while x < 4000000:
    new = x + y
    x = y
    y = new
    if x % 2 == 0:
        sum = sum + x

answer = 4613732

print(sum)
print(answer == sum)
