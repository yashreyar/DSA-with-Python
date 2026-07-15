'''
Input: binary_str = "101"
Output: 5
'''


def binary_to_decimal(binary_str):
    num = int(binary_str)
    result = 0
    power = 0
    for n in binary_str:
        remainder = num % 10
        result += remainder * (2**power)
        num = num // 10
        power += 1
    return result

print(binary_to_decimal("1010"))