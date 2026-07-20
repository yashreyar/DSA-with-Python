'''
Input: nums = [0, 1]
Output: 2

Input: nums = [8, 7, 6, 4, 3, 2, 0, 1]
Output: 5
'''

# Time complexity: O(n)
# Space complexity: O(1)
def find_missing_number(nums):
    n = len(nums)
    expected_sum = n * (n + 1) // 2
    actual_sum = sum(nums)                  # time: O(n)
    
    return expected_sum - actual_sum

print(find_missing_number(nums=[2,3,6,7,1,4,5]))