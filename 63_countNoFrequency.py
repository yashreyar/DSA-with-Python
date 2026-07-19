# O(n)
def count_numbers_frequency(lst):         
    result = {}
    for num in lst:                 # O(n)
        if num in result:           # O(1)
            result[num] += 1        # O(1)
        else:                       
            result[num] = 1         # O(1)
    return result

print(count_numbers_frequency(lst=[1,2,5,4,3,2,52,1,4,1,2,5,3]))