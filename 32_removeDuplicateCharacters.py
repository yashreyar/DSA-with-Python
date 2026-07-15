'''
Remove Duplicates in a string

Input: "Hello, World!"
Output: "Helo, Wrd!"
'''

def remove_duplicates(s):
    result = ""
    
    for char in s:
        if char in result:
            result = result
        else:
            result = result + char
    return result

print(remove_duplicates("Hello, World!"))