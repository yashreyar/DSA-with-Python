# Return the largest element in the list

def largest_element(items):
    largest = 0
    for num in items:
        if num > largest:
            largest = num
    return largest

print(largest_element([11,2,6,5,4,8,3]))