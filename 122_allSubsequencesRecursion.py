'''
LeetCode: https://leetcode.com/problems/subsets/

Input: nums = [1,2,3]
Output: [[],[1],[2],[1,2],[3],[1,3],[2,3],[1,2,3]]
'''

# Time Complexity: O(n * 2^n) 2^n because these much subsets are there
# Space Complexity: O(n) Auxiliary stack space
def subsets(nums):
    result = []
    
    def func(index, subset):
        if index == len(nums):
            result.append(subset.copy())            # time: O(n)
            return
        subset.append(nums[index])
        func(index+1, subset)
        subset.pop()
        func(index+1, subset)
    func(0, [])
    return result

print(subsets(nums=[1,2,3]))