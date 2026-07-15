'''
Count consonants in a string

Input: "Hello, World!"
Output: 7
'''

# consonants = total char - vowels

def count_consonants(s):
    
    s = s.lower()
    consonants_count = 0
    vowels = "aeiou"
    
    for char in s:
        if char.isalpha() and char not in vowels:
            consonants_count += 1
            
    return consonants_count

print(count_consonants(s="Hello, World!"))