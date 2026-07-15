'''
Reverse a string:

Input: "Python"
Output: "nohtyP"
'''


def reverse_string(s):
    result = ""
    for char in s:
        result = char + result
    return result
print(reverse_string("Hello"))