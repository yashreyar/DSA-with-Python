# Time complexity: O(logn)
# Space complexity: O(1)
def find_min(nums):
    n = len(nums)
    s = 0
    e = n-1
    mini = float("inf")
    
    while s <= e:
        m = s + (e - s) // 2
        
        # If right part is sorted, minimum will be mid element
        if nums[m] <= nums[e]:
            mini = min(mini, nums[m])           # Potential answer found
            # There can be more minimum element to left of it 
            e = m-1
            
        # Otherwise, if left part is sorted
        else:
            mini = min(mini, nums[s])           # Potential answer found
            # There can be more minimum element to left of it 
            s = m+1
            
    return mini

print(find_min(nums=[3,1,2]))