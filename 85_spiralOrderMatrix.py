'''
LeetCode: https://leetcode.com/problems/spiral-matrix/description/

Input: matrix = [[1,2,3,4],
                [12,13,14,5],
                [11,16,15,6],
                [10,9,8,7]]
Output: [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16]
'''

def spiral_matrix(nums):
    if not nums or not nums[0]:
        return []
    
    rows = len(nums)
    cols = len(nums[0])
    top, left = 0, 0
    bottom = rows-1
    right = cols-1
    result = []
    
    while left <= right and top <= bottom:
        
        # Move left to right across top row
        for i in range(left, right+1):
            result.append(nums[top][i])
        top+=1
        
        # Move right to bottom across right column
        for i in range(top, bottom+1):
            result.append(nums[i][right])
        right-=1
        
        # Move left to right across bottom row(if still valid)
        if top <= bottom:
            for i in range(right, left-1, -1):
                result.append(nums[bottom][i])
            bottom-=1
            
        # Move bottom to top along the left column(if still valid)
        if left <= right:
            for i in range(bottom, top-1, -1):
                result.append(nums[i][left])
            left+=1
            
    return result

print(spiral_matrix(nums=
                [[1,2,3,4],
                [12,13,14,5],
                [11,16,15,6],
                [10,9,8,7]]))
