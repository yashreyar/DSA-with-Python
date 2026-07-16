'''
Plus One in the Number. EG:

Input: digits = [4, 3, 2, 1]
Output: [4, 3, 2, 2]

Input: digits = [9, 9, 9]
Output: [1, 0, 0, 0]
'''

def plus_one(digits):
    num = ""
    for i in range(len(digits) - 1, -1, -1):
        if digits[i] < 9:
            digits[i] += 1
            return digits
        
        # If the current digit is 9, it becomes 0 (and carry moves left)
        digits[i] = 0
        
    # If the loop finished, it means ALL digits were 9 (e.g., [9, 9, 9])
    # We need to prepend a 1 at the beginning
    return [1] + digits

print(plus_one(digits=[9,9,9]))

