'''
Check if a number is armstring or not

Input = 153
Output = True
Explanation = Number of digits = 3, So power will be 3
If (1**3 + 5**3 + 3**3 == 153)
Then its an armstring number
'''
from math import *

def is_armstrong(num):
    if num < 0:
        return False
    if num == 0:
        return True
    n = num
    ans = 0
    no_of_digits = int(log10(n) + 1)
    while n > 0:
        last_digit = n % 10
        ans += (last_digit ** no_of_digits)
        n = n // 10
        
    return ans == num

print(is_armstrong(num=1634))
