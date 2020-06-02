import math
def arithSum(n):
    return n*(n+1)/2

def three_fives(r):
    n = math.floor(int(r))
    if n < 3:
        return 0
    threes = 3 * arithSum(math.floor(n/3))
    fives =  5 * arithSum(math.floor(n/5))
    fifteens = 15 * arithSum(math.floor(n/15))
    return int(threes + fives - fifteens - n)

def ar_nodiv(n):
    return n*(n+1)

def three_fives_bitwise(input):
    n = int(input)
    a = int(n/3)
    b = int(n/5)
    c = int(n/15)
    return (int(int(3*ar_nodiv(a) + 5*ar_nodiv(b) - 15*ar_nodiv(c))>>1))

def bruteForce(n):
    sum = 0
    for i in range(n):
        if (i%3 == 0) or (i%5 == 0):
            sum += i
    return sum

answer = three_fives_bitwise