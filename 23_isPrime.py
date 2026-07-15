'''
A number n is prime if it is not divisible by any number between 2 and sqrt(n).
'''

import math

def is_prime(n):
    
    if n <= 1:
        return False  # 0 and 1 are not prime numbers
    
    limit = int(math.sqrt(n)) + 1
    for i in range(2, limit):
        if n%i == 0:
            return False
        
    return True # No factor found hence prime number
print(is_prime(2))
