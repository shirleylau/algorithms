# A palindromic number reads the same both ways. The largest palindrome made
#
# Find the largest palindrome made from the product of two 3-digit numbers.

palindrome = None
f1 = 999
f2 = 999
rounds = 0

def is_palindrome(num):
    num = str(num)
    return num == ''.join(reversed(num))

# while !is_palindrome(f1 * f2):
while f2 > 99:
    prod = f1 * f2
    palindrome = prod if is_palindrome(prod) and prod > palindrome else palindrome
    if f1 == 100:
        rounds += 1
        f2 -= 1
        f1 = f2
    else:
        f1 -= 1


print(palindrome)
