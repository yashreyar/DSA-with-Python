'''
Check if a number is palindrome or not

Input = 12321
Output = True
'''

def is_palindrome(num):
    # Negative numbers are not palindromes
    if num < 0:
        return False
    temp_num = num
    reverse_num = 0
    while temp_num > 0:
        last_digit = temp_num % 10
        reverse_num = (reverse_num * 10) + last_digit
        temp_num = temp_num // 10
    return reverse_num == num

print(is_palindrome(num=12321))