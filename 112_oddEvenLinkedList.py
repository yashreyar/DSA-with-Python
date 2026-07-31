"""
LeetCode: https://leetcode.com/problems/odd-even-linked-list/description/

Input: head = [2,1,3,5,6,4,7]
Output: [2,3,6,7,1,5,4]
"""


# Time complexity: O(n)
# Space complexity: O(1)
def odd_even_linked_list(head):
    if not head or not head.next:
        return head

    odd = head
    even = head.next

    # Saving value of even_head to link last odd to first even
    even_head = even

    # Because even will reach None before odd (even starts from head.next)
    while even and even.next:
        odd.next = even.next  # Point current odd to the next odd node
        odd = odd.next  # Move odd pointer forward

        even.next = (odd.next)  # Point current even to the next even node (after odd moved!)
        even = even.next  # Move even pointer forward

    odd.next = even_head
    return head


"""
# Time complexity: O(n/2+n/2+n) = O(n)
# Space complexity: O(n)
def odd_even_linked_list(head):
    result = []
    if not head or not head.next:
        return head

    # Append odd nodes to result
    curr = head
    while curr and curr.next:                   # time: O(n/2)
        result.append(curr)
        curr = curr.next.next

    # Append even nodes to result
    front = head.next                           # time: O(n/2)
    while front and front.next:
        result.append(front)
        front = front.next.next

    # Link every Node to next Node
    curr = head
    index = 0
    while curr:                                 # time: O(n)
        curr.val = result[index]
        index+=1
        curr = curr.next
        
    return head
    """
