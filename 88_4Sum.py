'''
LeetCode: https://leetcode.com/problems/4sum/description/

Input: nums = [1,0,-1,0,-2,2], target = 0
Output: [[-2,-1,1,2],[-2,0,0,2],[-1,0,0,1]]
'''

# Time Complexity: O(n log n) + O(n^3) = O(n^3)
# Space complexity: O(1) auxiliary space (excluding output array)
def four_sum(nums, target):
    nums.sort()
    n = len(nums)
    result = []
    
    for i in range(n-3):
        if i > 0 and nums[i] == nums[i-1]:
            continue
        for j in range(i+1, n-2):
            if j > i+1 and nums[j] == nums[j-1]:
                continue
            # Initializing the k and l pointers
            k = j+1
            l = n-1
            
            while k < l:
                total_sum = nums[i]+nums[j]+nums[k]+nums[l]
                if total_sum < target:
                    k+=1
                elif total_sum > target:
                    l-=1
                else:
                    temp = [nums[i],nums[j],nums[k],nums[l]]
                    result.append(temp)
                    k+=1
                    l-=1
                    
                    # Skip the duplicates if occured
                    while k < l and nums[k] == nums[k-1]:
                        k+=1
                    while l > k and nums[l] == nums[l+1]:
                        l-=1
    return result

print(four_sum(nums=[1,0,-1,0,-2,2], target=0))


# OR

'''
# Time complexity: O(n^4)
# Space complexity: O(No. of quadruplets)
def four_sum(nums, target):
    my_set = set()
    n = len(nums)
    for i in range(n-3):
        for j in range(i+1, n-2):
            for k in range(j+1, n-1):
                for l in range(k+1, n):
                    if nums[i]+nums[j]+nums[k]+nums[l] == target:
                        temp = [nums[i],nums[j],nums[k],nums[l]]
                        temp.sort()
                        my_set.add(tuple(temp))
                        
    return [list(ans) for ans in my_set]
    #OR
    result = []
    for ans in my_set:
        result.append(list(ans))
    
    return result

print(four_sum(nums=[1,0,-1,0,-2,2], target=0))
'''
