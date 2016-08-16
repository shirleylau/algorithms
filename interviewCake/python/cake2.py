test1 = [1, 2, 3, 4]
test2 = [0, 3, 7, 7, 7]
test3 = [0, 3, 7, 7, 7, 0]

def get_exclusive_prods(ints):
    zeroes = len([x for x in ints if x == 0])
    maxProd = 0 if zeroes > 1 else reduce(lambda x, y: x * y, [x for x in ints if x is not 0])
    prods = []
    if zeroes < 2:
        for x in ints:
            prods.append(0 if zeroes > 0 and x != 0 else (maxProd if x == 0 else maxProd / x))
    else:
        prods = [0 for x in ints]

    return prods

print get_exclusive_prods(test2)
