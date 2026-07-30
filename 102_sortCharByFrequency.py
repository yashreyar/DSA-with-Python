'''
LeetCode: https://leetcode.com/problems/sort-characters-by-frequency/

Input: s = "tree"
Output: "eert"
Explanation: 'e' appears twice while 'r' and 't' both appear once.
So 'e' must appear before both 'r' and 't'. Therefore "eetr" is also a valid answer.
'''

def sort_by_freq(s):
    result = ""
    hash_map = {}
    
    for ch in s:
        hash_map[ch] = hash_map.get(ch, 0) + 1
        
    sorted_char = sorted(hash_map.items(), key=lambda x:(-x[1], x[0]))
    for ch, freq in sorted_char:
        result += (ch*freq)
        
    return result

print(sort_by_freq(s="tree"))
