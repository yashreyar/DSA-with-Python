'''
Upper Bound: Smallest index such that nums[i] > target
'''

# Time complexity: O(logn)
# Space complexity: O(1)
def upper_bound(nums, target):
    n = len(nums)
    s = 0
    e = n-1
    ub = n
    while s <= e:
        m = s + (e - s) // 2
        if nums[m] > target:
            ub = m
            e = m-1
        else:
            s = m+1
    
    return ub

print(upper_bound(nums=[1,1,1,2,3,3,4,5,5,6,6,6,6,7,8,8], target=3))
