def is_palindrome(n):
    inp = str(int(n))
    rev = inp[::-1]
    return inp == rev


def factors_of_number(x):
    factors = []
    for i in range(1, x + 1):
        if x % i == 0:
            factors.append(i)
    return(factors)

def largest_palindrome(upper_bound):
    n = int(upper_bound)
    x = ((n-1)//11)*11  #All six digit palindromes divisible by 11.
    three_digit_factors = False
    while x > 0 and three_digit_factors:
        if is_palindrome(x):
            factors = factors_of_number(x)
            factors_100 = [i for i in factors if i >= 100 and i < 1000]
            for j in range (0,len(factors_100)):
                if x//factors_100[j] >= 100 and x//factors_100[j] < 1000: 
                    three_digit_factors = True
                    break
        x -= 11
    return x

answer = largest_palindrome