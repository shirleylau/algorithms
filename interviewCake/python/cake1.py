test1 = [3, 4, 3, 5, 53, 7, 5, 8, 11, 9, 1, 23, 61]
test2 = [10, 9, -5, -9]
test3 = [3, 4, 3, 5, 53, 7, 5, 8, 11, 9, 1, 23, 61]

def make_profit(prices):
    # Buy small
    # Sell big
    buy = None
    profit = None
    # for i in range(len(prices)):
    for cur in prices # Elims need for declaring var curr
        # curr = prices[i]
        profit = curr - buy if buy is not None and curr - buy > profit else profit
        # buy = curr if buy is None or buy > curr else buy
        buy = min(curr, buy) if buy is not None else curr

    return 'running with $%s' % profit


print make_profit(test1)
print make_profit(test2)
print make_profit(test3)
