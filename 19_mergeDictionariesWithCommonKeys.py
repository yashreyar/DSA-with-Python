def merge_dicts_with_overlapping_keys(dicts):
    result = {}
    
    # loop through every dictionary in dicts
    for d in dicts:
        # loop through key, value pairs in each dictionary
        for key, value in d.items():
            if key in result:
                result[key] += value
            else:
                result[key] = value
    return result
    
print(merge_dicts_with_overlapping_keys([{'a': 1, 'b': 2}, {'b': 3, 'c': 4}, {'c': 5, 'd': 6}]))