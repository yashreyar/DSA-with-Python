# Use a dictionary to count the frequecy of elements in a list 

numbers = [1, 1, 1, 1, 1, 2, 2, 2, 3, 3, 4, 4, 4, 4, 4]
dict = {}

for num in numbers:
    if num not in dict:
        dict[num] = 1;
    else:
        dict[num] += 1;
print(dict)