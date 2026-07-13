def remove_duplicates(items):
    unique_list = []
    for num in items:
        if num not in unique_list:
            unique_list.append(num)
    unique_list.sort()
    return unique_list

print(remove_duplicates([1,4,3,2,6,7,8,5,3,5,7,8,3,2,9,2,9]))


#OR

'''
def remove_duplicate(items):
    items.sort()
    i = 0
    while i < len(items)-1:
        if items[i] == items[i+1]:
            items.pop(i) # Removes the value at i iitems
        else:
            i+=1
    return items

print(remove_duplicate([1,3,6,2,5,9,1,4,2,8,3,2,6,5,8,9]))
'''