'''
With a set: Checking num not in seen takes $O(1)$ time. 
Repeating this for n numbers takes O(n) total time.
With only a list: Checking num not in result requires scanning the result list
from start to finish every single time. 
This takes O(k) time where k is the current length of result.
Over the whole loop, doing this check repeatedly takes O(n^2) total time.
'''

# Time complexity: O(n) -> Because we're using set function to check (if num not in seen:)
# for list function like if num not in list it takes O(n) time
# Space complexity: O(n)
def remove_duplicates_from_unsorted(nums):
    seen = set()
    result = []
    for num in nums:
        if num not in seen:
            seen.add(num)
            result.append(num)
    return result

# Example:
print(remove_duplicates_from_unsorted([4, 2, 1, 4, 2, 3, 1]))  
# Output: [4, 2, 1, 3]