# Maximum difference between two consecutive elements in a list.

def max_diff(nums):
    
    if len(nums) < 2:
        return 0
    
    max_difference = 0
    for i in range(1, len(nums)):
        
        current_difference = abs(nums[i] - nums[i-1])
        
        if current_difference > max_difference:
            max_difference = current_difference
            
        i+=1
    return max_difference

print(max_diff([1,7,3,10,5]))