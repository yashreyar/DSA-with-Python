'''
LeetCode: https://leetcode.com/problems/reverse-linked-list/description/

Input: head = [1,2]
Output: [2,1]
'''

# Time complexity: O(n)
# Space complexity: O(1)
def reverse_linked_list(head):
    curr = head
    prev = None

    while curr != None:
        front = curr.next
        curr.next = prev
        prev = curr
        curr = front
    return prev


# OR

'''
# Time complexity: O(2n)
# Space complexity: O(n)
def reverse_linked_list(head):
    curr = head
    stack = []
    
    while curr != None:
        stack.append(curr.val)
        curr = curr.next
    
    curr = head
    while curr != None:
        e = stack.pop()
        curr.val = e
        curr = curr.next
    
    return head
    '''