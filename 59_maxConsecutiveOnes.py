'''
Input: nums = [1, 0, 1, 1, 0, 1, 1, 1, 1]
Output: 4
'''

def find_max_consecutive_ones(nums):
    count = 0
    max_count = 0
    for num in nums:
        if num == 1:
            count += 1
            max_count = max(count, max_count)
        else:
            count = 0
    return max_count

print(find_max_consecutive_ones(nums=[1, 0, 1, 1, 0, 1, 1, 1, 1]))