'''
Input: ARR = [1, 2, 3, 4, 5], D = 2
Output: [3, 4, 5, 1, 2]
'''

def rotate_left(ARR, D):
    D = D % len(ARR)
    
    lst = []
    for i in range(D, len(ARR)):
        lst.append(ARR[i])
    for i in range(D):
        lst.append(ARR[i])
        
    return lst

print(rotate_left(ARR=[1,2,3,4,5], D=2))


# OR (POP and append method: LESS OPTIMIZED THAN ABOVE CODE)
'''
def rotate_left_pop(ARR, D):
    arr = ARR.copy() # Avoid modifying the original list unexpectedly
    D = D % len(arr)
    
    for _ in range(D):
        first_element = arr.pop(0) # Remove from front
        arr.append(first_element)  # Add to back
        
    return arr

print(rotate_left_pop([1, 2, 3, 4, 5], 2))
'''


# OR
'''
def rotate_left(ARR, D):
    D = D % len(ARR)
    # Concatenate the slice from D onward with the slice up to D
    return ARR[D:] + ARR[:D]

print(rotate_left(ARR=[1,2,3,4,5], D=2))
'''
