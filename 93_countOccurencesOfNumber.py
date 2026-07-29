'''
Ques: https://www.geeksforgeeks.org/problems/number-of-occurrence2259/1

Input: arr[] = [1, 1, 2, 2, 2, 2, 3], target = 2
Output: 4
Explanation: target = 2 occurs 4 times in the given array so the output is 4.
'''

# Time complexity: O(logn)
# Space complexity: O(1)
def count_occurences(nums, target):
    s = BS(nums, target, start=True)
    if s == -1:
        return 0
    e = BS(nums, target, start=False)
    return (e - s)+1

def BS(nums, target, start):
    ans = -1
    n = len(nums)
    s = 0
    e = n-1
    
    while s <= e:
        m = s+(e-s)//2
        if nums[m] == target:
            ans = m
            if start == True:
                e = m-1
            else:
                s = m+1
        elif nums[m] > target:
            e = m-1
        else:
            s = m+1
            
    return ans

print(count_occurences(nums=[1, 1, 2, 2, 2, 2, 3], target = 0))


'''
# Time complexity: O(n)
# Space complexity: O(n)
def count_occurences(nums, target):
    hash_map = {}
    for num in nums:
        hash_map[num] = hash_map.get(num, 0) + 1
    return hash_map[target]

print(count_occurences(nums=[1, 1, 2, 2, 2, 2, 3], target = 2))
'''