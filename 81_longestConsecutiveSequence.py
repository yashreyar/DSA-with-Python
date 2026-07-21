'''
LeetCode: https://leetcode.com/problems/longest-consecutive-sequence/description/

Input: my_set = [100,3,4,200,1,1,3,2]
Output: 4
Explanation: The longest consecutive elements sequence is [1, 2, 3, 4]. Therefore its length is 4
'''

# Time complexity: O(n)
# Space complexity: O(n)
def longest_consecutive_sequence(nums):
    longest_sequence = 0
    my_set = set(nums)
    for num in my_set:
        # Check if 'num' is starting of sequence
        if (num-1) not in my_set:
            current_num = num
            current_streak=1
            # Increase the streak while there is next greater consecutive element present
            while (current_num+1) in my_set:
                current_streak+=1
                current_num+=1
            longest_sequence = max(longest_sequence, current_streak)
            
    return longest_sequence

print(longest_consecutive_sequence(nums=[100,3,4,200,1,1,3,2]))