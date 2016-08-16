test1 = [1, 2, 3, 4]
test2 = [-10, 3, -2, 10, 7]
test3 = [0, 3, 7, 7, 7, 0]

def get_max_prod(arr):
    ints = [abs(x) for x in arr]
    maxProd = reduce(lambda x, y: x * y, sorted(ints)[-3:])
    return maxProd

print get_max_prod(test1)
print get_max_prod(test2)
print get_max_prod(test3)
