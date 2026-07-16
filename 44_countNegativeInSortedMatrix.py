'''
Count negative numbers in a sorted matrix

Input: grid = [[4, 3, 2, 1], [3, 2, 1, -1], [1, 1, -1, -2], [-1, -1, -2, -3]] 
Output: 7 
'''


def countNegatives(grid):
    count = 0
    for list in grid:
        for elements in list:
            if elements < 0:
                count += 1
    return count

print(countNegatives([[4, 3, 2, 1], [3, 2, 1, -1], [1, 1, -1, -2], [-1, -1, -2, -3]]))