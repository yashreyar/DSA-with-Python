'''
Rotate matrix to right by 90 degrees

Input: [[1,2,3,4],
        [5,6,7,8],
        [9,10,11,12],
        [13,14,15,16]]
        
Output:[[13,9,5,1],
        [14,10,6,2],
        [15,11,7,3],
        [16,12,8,4]]
'''

# Only used for n*n matrix(square matrix)
# In place 
# Time complexity: O(n*n) + O(n*n) = O(n^2)
# Space complexity: O(1)
def rotate_matrix(nums):
    
    # Transpose the matrix
    n = len(nums)
    for i in range(n):
        for j in range(i+1, n):
            nums[i][j], nums[j][i] = nums[j][i], nums[i][j]
            
    # Reverse each row now
    for i in range(n):
        nums[i].reverse()
        
nums = [[1,2,3,4],
        [5,6,7,8],
        [9,10,11,12],
        [13,14,15,16]]
rotate_matrix(nums)
print(nums)


# OR

'''
# Also used for n*m matrix(non-square matrix)
# It's not in place 
# Time complexity: O(n*m)
# Space complexity: O(n*m)
def rotate_matrix_by_90_degrees(nums):
    n = len(nums)
    rows = len(nums)
    cols = len(nums[0])
    result = [[0]*rows for _ in range(cols)]

    for i in range(rows):
        for j in range(cols):
            result[j][(n-1)-i] = nums[i][j]  
    return result

print(rotate_matrix_by_90_degrees(nums=[[1,2,3,4],[5,6,7,8],[9,10,11,12],[13,14,15,16]]))
'''

