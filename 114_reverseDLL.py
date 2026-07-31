"""
LeetCode: https://www.geeksforgeeks.org/problems/reverse-a-doubly-linked-list/1
"""

# Time complexity: O(n)
# Space complexity: O(1)
def reverse_DLL(head):
    curr = head
    prev = None

    while curr != None:
        front = curr.next
        curr.next = prev
        curr.prev = front
        prev = curr
        curr = front

    return prev
