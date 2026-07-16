'''
Find First and Last Position of Element in Sorted Array

Input: nums = [5, 7, 7, 8, 8, 10], target = 8 
Output: [3, 4] 
'''

def searchRange(nums, target):
    ans = [-1, -1]
    start = search(nums, target, findStartIndex=True)
    end = search(nums, target, findStartIndex=False)
    ans[0] = start
    ans[1] = end
    return ans

def search(nums, target, findStartIndex):
    s = 0
    e = len(nums) - 1
    ans = -1
    while s <= e:
        m = s + (e - s) // 2
        if target < nums[m]:
            e = m - 1
        elif target > nums[m]:
            s = m + 1
        else:
            ans = m
            # Potential answer found(There may be more target value in left or right)
            if findStartIndex == True:
                e = m - 1
            else:
                s = m + 1
    return ans

print(searchRange(nums=[5, 7, 7, 8, 8, 10], target=8))