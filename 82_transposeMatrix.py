'''
Input:      [[1,2,3],
            [4,5,6]]
            
Output:     [[1,4],
            [2,5],
            [3,6]]
'''

# Only works on n*n matrix(square matrix)
# In place
# Time complexity: O(n**2)
# Space complexity: O(1)
def transpose(nums):
    n = len(nums)
    for i in range(0, n-1):
        for j in range(i+1, n):
            nums[i][j], nums[j][i] = nums[j][i], nums[i][j]

nums=[[1,2,3],[4,5,6],[7,8,9]]
transpose(nums)
print(nums)


# OR

'''
# Its not in place
# Time complexity: O(n*m)
# Space complexity: O(n*m)
def transpose(nums):
    rows = len(nums)
    cols = len(nums[0])
    result = [[0]*rows for _ in range(cols)]
    
    for i in range(rows):
        for j in range(cols):
            result[j][i] = nums[i][j]
    return result

print(transpose(nums=[[1,2,3],[4,5,6]]))
'''