'''
LeetCode: https://leetcode.com/problems/longest-common-prefix/description/

Input: strs = ["flower","flow","flight"]
Output: "fl"
'''

# Time complexity: O(nlogn.m)
# M -> Length of the shortest/first string
# Space complexity: O(1)
def longest_common_prefix(strs):
    if not strs:
        return ""
    
    # Sorting lexicographically
    strs.sort()                                                         # time: O(nlogn)

    # Compare only the first and last strings
    first, last = strs[0], strs[-1]
    i = 0
    while i < len(first) and i < len(last) and first[i] == last[i]:     # time: O(n+m)
        i += 1

    return first[:i]

print(longest_common_prefix(strs = ["flower","flow","flight"]))

'''
# Time complexity: O(n*m) 
# N -> Number of strings in strs, M -> Length of the shortest string
# Space complexity: O(m)
def longest_common_prefix(strs):
    result = ""
    base = strs[0]
    for i in range(len(base)):
        for word in strs[1:]:
            if i == len(word) or base[i] != word[i]:
                return result
        result += base[i]
    return result

print(longest_common_prefix(strs = ["flower","flow","flight"]))
'''