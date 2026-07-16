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