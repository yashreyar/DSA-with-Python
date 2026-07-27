'''
Input: nums = [2,7,11,15], target = 9
Output: [0,1]
'''

# Time complexity: O(n)
# Space complexity: O(n)
def two_sum(nums, target):
    hash_map = {}
    n = len(nums)
    for i in range(n):
        remaining = target - nums[i]
        if remaining in hash_map:
            return [hash_map[remaining], i]
        
        # Add the value and index in hashmap
        hash_map[nums[i]] = i
    return []

print(two_sum(nums=[3,3], target=6))


# OR

'''
# Time complexity: O(n**2)
# Space complexity: O(1)
def two_sum(nums, target):
    n = len(nums)
    for i in range(n-1):
        for j in range(i+1, n):
            if nums[i]+ nums[j] == target:
                return [i, j]
    return []

print(two_sum(nums=[3,3], target=6))
'''