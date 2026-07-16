def findMin(nums):
    s = 0
    e = len(nums) - 1
    
    while s < e:
        m = s + (e - s) // 2
        if nums[m] > nums[e]:
            s = m + 1
        else:
            e = m 
            
    # When s == e, they both point exactly to the minimum element
    return nums[s]

print(findMin(nums=[3,0,1,2]))