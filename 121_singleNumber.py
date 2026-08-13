'''
LeetCode: https://leetcode.com/problems/single-number/description/

Input: nums = [4,1,2,1,2]
Output: 4
'''

# Time complexity: O()
# Space complexity: O()
def single_number(nums):
    ans = 0
    for num in nums:
        ans = ans ^ num
    return ans

print(single_number(nums=[4,1,2,1,2]))


# OR

'''
# Time complexity: O(n) + O((n/2)+1)
# Space complexity: O((n/2)+1)
def single_number(nums):
    hash_map = {}
    for num in nums:
        hash_map[num] = hash_map.get(num, 0) + 1
    for num, count in hash_map.items():
        if count == 1:
            return num

print(single_number(nums=[4,1,2,1,2]))
'''
