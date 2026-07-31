'''
LeetCode: https://leetcode.com/problems/linked-list-cycle/description/

Input: head = [3,2,0,-4], pos = 1
Output: true
Explanation: There is a cycle in the linked list, where the tail connects to the 1st node (0-indexed).
'''

# Time complexity: O(n)
# Space complexity: O(1)
def hasCycle(head):
    slow, fast = head, head 
    while fast != None and fast.next != None:
        slow = slow.next
        fast = fast.next.next
        if fast == slow:
            return True
    return False

# OR

'''
# Time complexity: O(n)
# Space complexity: O(n)
def hasCycle(head):
    curr = head
    my_set = set()

    while curr != None:
        if curr in my_set:
            return True
        my_set.add(curr)
        curr = curr.next
    return False
'''