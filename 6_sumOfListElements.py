# Return sum of all elements in the list

def sum_of_elements(numbers):
    sum = 0
    for num in numbers:
        sum += num
    return sum

print(sum_of_elements([1,2,3,4,5]))