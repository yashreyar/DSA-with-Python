'''
Input:      [[1,2,3],
            [4,0,6],
            [7,8,0]]
            
Output:     [[1,0,0],
            [0,0,0],
            [0,0,0]]
'''

# Time complexity: O(n*m) 
# Space complexity: O(n+m)
def set_matrix_zeroes(nums):
    rows = len(nums)
    cols = len(nums[0])
    
    row_track = [0 for _ in range(rows)]
    col_track = [0 for _ in range(cols)]
    
    for i in range(rows):
        for j in range(cols):
            if nums[i][j] == 0:
                row_track[i] = -1
                col_track[j] = -1
    
    for i in range(rows):
        for j in range(cols):
            if row_track[i] == -1 or col_track[j] == -1:
                nums[i][j] = 0
                

matrix = [[1, 2, 3], [4, 0, 6], [7, 8, 0]]
set_matrix_zeroes(matrix)
print(matrix) 


# OR

'''
# Time complexity: O((n*m)*(n+m))+O(n*m) 
# Space complexity: O(1)
def set_matrix_zeroes(nums):
    rows = len(nums)
    cols = len(nums[0])
    
    for i in range(rows):                           # time: O(n*m)
        for j in range(cols):
            if nums[i][j] == 0:
                mark_infinity(nums, i, j)           # time: O(n+m)
                
    for i in range(rows):                           # time: O(n*m)
        for j in range(cols):
            if nums[i][j] == float("inf"):
                nums[i][j] = 0
                
def mark_infinity(nums, r, c):                                
    rows = len(nums)
    cols = len(nums[0])
    
    for i in range(rows):
        if nums[i][c] != 0 and nums[i][c] != float("inf"):
            nums[i][c] = float("inf")
            
    for j in range(cols):
        if nums[r][j] != 0 and nums[r][j] != float("inf"):
            nums[r][j] = float("inf")
            
matrix = [[1, 2, 3], [4, 0, 6], [7, 8, 0]]
set_matrix_zeroes(matrix)
print(matrix)  # Prints: [[1, 0, 0], [0, 0, 0], [0, 0, 0]]
'''