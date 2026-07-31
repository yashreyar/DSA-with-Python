'''
LeetCode: https://leetcode.com/problems/odd-even-linked-list/description/

Input: head = [2,1,3,5,6,4,7]
Output: [2,3,6,7,1,5,4]
'''

def odd_even_linked_list(head):
    result = []
    if not head or not head.next:
        return None

    # Append odd nodes to result
    curr = head
    while curr and curr.next:
        result.append(curr)
        curr = curr.next.next

    # Append even nodes to result
    front = curr.next
    while front and front.next:
        result.append(front)
        front = front.next.next

    return result