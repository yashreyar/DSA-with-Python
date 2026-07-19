# Using HashMap
def count_number_freq(lst):
    hash_map = {}
    n = len(lst)
    for i in range(n):
        hash_map[lst[i]] = hash_map.get(lst[i], 0) + 1
    return hash_map

print(count_number_freq(lst = [1,3,2,4,5,3,1,2,4,2]))

# OR

# O(n)
'''
def count_numbers_frequency(lst):         
    result = {}
    for num in lst:                 # O(n)
        if num in result:           # O(1)
            result[num] += 1        # O(1)
        else:                       
            result[num] = 1         # O(1)
    return result

print(count_numbers_frequency(lst=[1,2,5,4,3,2,52,1,4,1,2,5,3]))
'''