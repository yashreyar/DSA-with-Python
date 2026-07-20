'''
Input: lst1=[1,1,2,3,3,4]
       lst2=[1,2,2,3,4,4,5,6]
       
Output: [1,1,1,2,2,2,3,3,3,4,4,4,5,6]
'''

def merge_sorted_arrays(lst1, lst2):
    result = []
    i, j = 0, 0
    while i<len(lst1) and j<len(lst2):
        if lst1[i] <= lst2[j]:
            result.append(lst1[i])
            i+=1
        else:
            result.append(lst2[j])
            j+=1
            
    return result + lst1[i:] + lst2[j:]

print(merge_sorted_arrays(lst1=[1,1,2,3,3,4], lst2=[1,2,2,3,4,4,5,6]))


# OR

'''
def merge_sorted_arrays(lst1, lst2):
    result = []
    i, j = 0, 0
    while i<len(lst1) and j<len(lst2):
        if lst1[i] <= lst2[j]:
            result.append(lst1[i])
            i+=1
        else:
            result.append(lst2[j])
            j+=1
    while i<len(lst1):
        result.append(lst1[i])
        i+=1
    while j<len(lst2):
        result.append(lst2[j])
        j+=1
    return result

print(merge_sorted_arrays(lst1=[1,1,2,3,3,4], lst2=[1,2,2,3,4,4,5,6]))
'''