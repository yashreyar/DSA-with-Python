# Check if all elements in a list are Unique

def unique_items(items):
    items.sort()
    i = 0
    while i < len(items)-1:
        if(items[i] == items[i+1]):
            return False
        i += 1    
    return True
print(unique_items([9,1,2,3,4,5,6,7]))