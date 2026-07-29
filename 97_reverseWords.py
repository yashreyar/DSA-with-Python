'''
LeetCode: https://leetcode.com/problems/reverse-words-in-a-string/description/

Input: s = "the sky is blue"
Output: "blue is sky the"
'''

# Time complexity: O(n)
# Space complexity: O(n)
def reverse_words(s):
    words = s.split()               # time: O(n)
    words.reverse()                 # time: O(n)
    result = " ".join(words)        # time: O(n)
    return result

print(reverse_words(s = "the sky is blue"))
