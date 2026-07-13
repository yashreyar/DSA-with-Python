# Merge 2 List into Dictionary

def merge_lists_to_dictionary(keys, values):
    
    if len(keys) != len(values):
        return False
    
    result = {}
    for i in range(len(keys)):
        result[keys[i]] =values[i]
        
    return result

print(merge_lists_to_dictionary(keys=['a', 'b', 'c'], values=[1, 2, 3]))