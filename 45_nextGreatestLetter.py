'''
Find smallest letter greater than target

Input:
letters = ['c', 'f', 'j']
target = 'k'
Output: 'c'
'''


def next_greatest_letter(letters, target):
    s = 0
    e = len(letters) - 1
    
    while s <= e:
        m = s + (e - s) // 2
        
        if target < letters[m]:
            e = m - 1
        else:
            s = m + 1
    # If s reaches the length of the array, s % len(letters) wraps it back to 0
    return letters[s % len(letters)]

print(next_greatest_letter(letters=['c','f','j'], target='k'))