
def second_largest_without_sorting(nums):
    largest = float('-inf')
    s_largest = float('-inf')
    n = len(nums)
    
    for i in range(n):
        if nums[i] > largest:
            s_largest = largest
            largest = nums[i]
        elif nums[i] > s_largest and nums[i] != largest:
            s_largest = nums[i]
    return s_largest

print(second_largest_without_sorting(nums=[1,5,3,2,7,9,4]))


'''
# Time complexity: O(n)+O(n) = O(n)
# Space complexity: O(1)
def second_largest_without_sorting(nums):
    largest = float('-inf')
    s_largest = float('-inf')
    n = len(nums)
    
    for i in range(n):                                      # O(n) time
        if largest < nums[i]:
            largest = nums[i]
            
    for i in range(n):                                      # O(n) time
        if nums[i] < largest and nums[i] > s_largest:
            s_largest = nums[i]
            
    return s_largest

print(second_largest_without_sorting(nums=[1,5,3,2,7,9,4]))
'''