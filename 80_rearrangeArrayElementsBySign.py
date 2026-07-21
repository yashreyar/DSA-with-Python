'''
LeetCode: https://leetcode.com/problems/rearrange-array-elements-by-sign/description/ 

You should return the array of nums such that the array follows the given conditions:
1.Every consecutive pair of integers have opposite signs.
2.For all integers with the same sign, the order in which they were present in nums is preserved.
3.The rearranged array begins with a positive integer.

Input: nums = [3,1,-2,-5,2,-4]
Output: [3,-2,1,-5,2,-4]
Explanation:
The positive integers in nums are [3,1,2]. The negative integers are [-2,-5,-4].
'''

# Time complexity: O(n)
# Space complexity: O(n)
# Pass count: 1 Iteration
def rearrange_array(nums):
    n = len(nums)
    result = [0] * n
    pos_index = 0
    neg_index = 1
    
    for num in nums:
        if num > 0:
            result[pos_index] = num
            pos_index+=2
        else:
            result[neg_index] = num
            neg_index+=2
    return result

print(rearrange_array(nums=[3,1,-2,-5,2,-4]))


# OR

'''
# Time complexity: O(n)
# Space complxity: O(n)
# Pass count: 2 iterations
def rearrange_array(nums):
    pos = []
    neg = []
    result = []
    for num in nums:                        # iteration 1
        if num < 0:
            neg.append(num)
        else:
            pos.append(num)
    for i in range(len(pos)):               # iteration 2
        result.append(pos[i])
        result.append(neg[i])
    return result

print(rearrange_array(nums=[3,1,-2,-5,2,-4]))
'''