'''
Count Vowels in a string

Input: "Python Programming"
Output: 4
'''

def count_vowels(s):
    vowels_count = 0
    vowels = "aeiou"
    for char in s:
        if char.lower() in vowels:
            vowels_count += 1
    return vowels_count

print(count_vowels("Python Programming"))
