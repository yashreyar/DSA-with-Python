'''
LeetCode: https://leetcode.com/problems/remove-outermost-parentheses/description/

Input: s = "(()())(())(()(()))"
Output: "()()()()(())"
'''

def remove_outermost_parenthesis(s):
    result = ""
    count = 0
    for ch in s:
        if ch == "(":
            count+=1
            if count > 1:
                result += ch
        else:
            count-=1
            if count > 0:
                result += ch
                
    return result

print(remove_outermost_parenthesis(s="(()())(())(()(()))"))