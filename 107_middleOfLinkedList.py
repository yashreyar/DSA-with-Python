'''
LeetCode: http://leetcode.com/problems/middle-of-the-linked-list/description/

Input: head = [1,2,3,4,5]
Output: [3,4,5]
Explanation: The middle node of the list is node 3.
'''

# Time complexity: O(n/2)
# Space complexity: O(1)
def middleNode(head):
    slow, fast = head, head
    
    while fast != None and fast.next != None:
        slow = slow.next
        fast = fast.next.next
    return slow

'''
# Time complexity: O(n+n/2)
# Space complexity: O(1)
def middleNode(head):
    curr = head
    count = 0
    while curr != None:                 # time: O(n)
        count += 1
        curr = curr.next
    middle_index = count//2
    curr = head
    for i in range(middle_index):       # time: O(n/2)
        curr = curr.next
    return curr
'''