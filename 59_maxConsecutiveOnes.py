'''
Input: nums = [1, 0, 1, 1, 0, 1, 1, 1, 1]
Output: 4
'''

# Time complexity: O(n)
# Space complexity: O(1)
def find_max_consecutive_ones(nums):
    count = 0
    max_count = 0
    for num in nums:                                # time: O(n)
        if num == 1:
            count += 1
            max_count = max(count, max_count)       # time: O(1)
        else:
            count = 0
    return max_count

print(find_max_consecutive_ones(nums=[1, 0, 1, 1, 0, 1, 1, 1, 1]))