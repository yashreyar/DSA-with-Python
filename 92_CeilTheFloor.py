'''
Que: https://www.naukri.com/code360/problems/ceiling-in-a-sorted-array_1825401

Print the floor and ceiling of the target variable respectively.

Floor: Largest number <= target
Ceiling: Smallest number >= target
'''

def ceil_the_floor(nums, target):
    
    ceil = -1
    floor = -1
    n = len(nums)
    s = 0
    e = n-1
    
    while s <= e:
        m = s+(e-s)//2
        if nums[m] == target:
            return [nums[m], nums[m]]
        elif nums[m] > target:
            ceil = nums[m]
            e = m-1
        else:
            floor = nums[m]
            s = m+1
            
    return [floor, ceil]

print(ceil_the_floor(nums=[3, 4, 7, 8, 8, 10], target=5))