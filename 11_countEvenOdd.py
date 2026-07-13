# Count Number of Odd and Even Elements in a List

def even_odd_count(nums):
    odd = 0
    even = 0
    for num in nums:
        if num%2 == 0:
            even += 1
        else:
            odd += 1
    return even, odd

print(even_odd_count([1,2,3,4,5,6,7,8,9]))