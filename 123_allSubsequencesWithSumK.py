'''
Ques: https://www.geeksforgeeks.org/dsa/find-all-subsequences-with-sum-equals-to-k/

Input: arr[] = [1, 2, 3], k = 3 
Output: [[1, 2], [3]]
'''

# Time complexity: O(n * 2^n)
# Space complexity: O(n) Auxiliary stack space
def subsets(arr, k):
    result = []
    def solve(index, total, subset):
        if total == k:
            result.append(subset.copy())
            return
        elif total > k:
            return
        if index == len(arr):
            return
        subset.append(arr[index])
        sum = total + arr[index]
        solve(index+1, sum, subset)
        e = subset.pop()
        sum -= e
        solve(index+1, sum, subset)
    solve(0, 0, [])
    return result

print(subsets(arr=[1, 2, 3], k=3))


# OR

'''
# Time complexity: O(n * 2^n)
# Space complexity: O(n) Auxiliary stack space
def subsets(arr, k):
    result = []
    
    def func(index, subset):
        if index == len(arr):
            if sum(subset) == k:
                result.append(subset.copy())        # time: O(n)
            return
        subset.append(arr[index])
        func(index+1, subset)
        subset.pop()
        func(index+1, subset)
    func(0, [])
    return result

print(subsets(arr=[1, 2, 3], k=3))
'''