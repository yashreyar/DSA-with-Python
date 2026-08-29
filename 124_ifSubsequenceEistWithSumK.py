'''
GFG: https://www.geeksforgeeks.org/problems/check-if-there-exists-a-subsequence-with-sum-k/1

Input: arr = [10, 1, 2, 7, 6, 1, 5], k = 8.
Output: true
'''

def subsets(arr, k):
    def solve(index, total, subset):
        if total == k:
            return True
        elif total > k:
            return False
        if index == len(arr):
            return False
        subset.append(arr[index])
        sum = total + arr[index]
        pick = solve(index+1, sum, subset)
        if pick == True:
            return True
        subset.pop()
        sum = total
        not_pick = solve(index+1, sum, subset)
        return not_pick
    return solve(0, 0, [])

print(subsets(arr=[1,2,3,4,5], k=15))
