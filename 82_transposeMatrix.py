'''
Input:      [[1,2,3],
            [4,5,6]]
            
Output:     [[1,4],
            [2,5],
            [3,6]]
'''

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
