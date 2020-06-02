
#Implement Erathosthenes' Sieve - O(sqrt(n))

def erathosthenes_max_prime(n):

    max_prime = -1

    # Get rid of all even factors
    while n%2 == 0:
        max_prime = 2
        n //= 2
    
    for i in range(3, int(n**0.5) + 1, 2):
        while n % i == 0:
            max_prime = i
            n //= i
    
    return n if n > 2 else max_prime

answer = erathosthenes_max_prime
print(answer(n))
