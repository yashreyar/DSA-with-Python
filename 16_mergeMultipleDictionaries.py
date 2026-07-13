def merge_three_dictionaries(dict1, dict2, dict3):
    
    merged_dict = dict1.copy()
    
    for key, value in dict2.items():
        merged_dict[key] = value
        
    for key, value in dict3.items():
        merged_dict[key] = value
        
    return merged_dict

print(merge_three_dictionaries(dict1={'a': 1, 'b': 2}, dict2={'c': 3, 'd': 4}, dict3={'e': 5, 'f': 6}))