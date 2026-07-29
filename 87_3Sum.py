'''
LeetCode: https://leetcode.com/problems/3sum/description/

Input: nums = [-1,0,1,2,-1,-4]
Output: [[-1,-1,2],[-1,0,1]]
'''

# Time complexity: O(nlogn) + O(n^2) = O(n^2)
# Space complexity: O(1) / O(no. of triplets)
def three_sum(nums):
    nums.sort()                           # time: O(nlogn)
    n = len(nums)
    ans = []
    
    for i in range(n-2):                  # time: O(n)
        # Optimization: positive numbers can't sum to 0
        if nums[i] > 0:
            break
        # If previous value of i was equal to the current value,
        # Increse i until it reaches a new value
        if i != 0 and nums[i] == nums[i-1]:
            continue
        
        # Initializing j and k
        j = i+1
        k = n-1
        
        # Moving two pointers
        while j < k:                    # time: O(n)
            total_sum = nums[i]+nums[j]+nums[k]
            
            if total_sum < 0:
                j+=1
                
            elif total_sum > 0:
                k-=1
                
            else:
                temp = [nums[i], nums[j], nums[k]]
                ans.append(temp)
                j+=1
                k-=1
                
                # Skip the duplicates if occured
                while j < k and nums[j] == nums[j-1]:
                    j+=1
                    
                while k > j and nums[k] == nums[k+1]:
                    k-=1
                    
    return ans

print(three_sum(nums=[-1,0,1,2,-1,-4]))


# OR

'''
# Time complexity: O(n^3)
# Space complexity: O(1) / O(no. of triplets)
def three_sum(nums):
    my_set = set()
    n = len(nums)
    for i in range(n-2):
        for j in range(i+1, n-1):
            for k in range(j+1, n):
                if nums[i] + nums[j] + nums[k] == 0:
                    temp = [nums[i], nums[j], nums[k]]
                    temp.sort()
                    my_set.add(tuple(temp))
                    
    return [list(ans) for ans in my_set]

print(three_sum(nums=[-1,0,1,2,-1,-4]))
'''