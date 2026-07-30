'''
Input: nums = [-2,1,-3,4,-1,2,1,-5,4]
Output: 6
Explanation: The subarray [4,-1,2,1] has the largest sum 6.
'''

# Time complexity: O(n)
# Space complexity: O(1)
def max_subarray(nums):
    n = len(nums)
    maxi = float("-inf")
    total = 0
    for num in nums:
        if total < 0:
            total = 0
        total += num
        maxi = max(total, maxi)
    return maxi

print(max_subarray(nums=[-2,1,-3,4,-1,2,1,-5,4]))


# OR

'''
# Time complexity: O(n**2)
# Space complexity: O(1)
def max_subarray(nums):
    n = len(nums)
    maxi = float("-inf")
    
    for i in range(n):
        total = 0
        for j in range(i, n):
            total = total + nums[j]
            maxi = max(total, maxi)
    return maxi

print(max_subarray(nums=[-2,1,-3,4,-1,2,1,-5,4]))
'''
