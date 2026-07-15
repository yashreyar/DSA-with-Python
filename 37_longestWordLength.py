'''
Input: s = "The quick brown fox jumps over the lazy dog"
Output: 5
'''

def longest_word_length(s):
    max_length = 0
    words = s.split()
    for word in words:
        if max_length < len(word):
            max_length = len(word)
    return max_length

print(longest_word_length(s="The quick yellow fox jumps over the lazy dog"))