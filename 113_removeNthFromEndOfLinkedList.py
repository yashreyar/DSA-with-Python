'''
LeetCode: https://leetcode.com/problems/remove-nth-node-from-end-of-list/description/

Input: head = [1,2,3,4,5], n = 2
Output: [1,2,3,5]
'''

# Time complexity: O(n)
# Space complexity: O(1)
def remove_nth(head, n):
    slow = fast = head
    
    for i in range(n):
        fast = fast.next
    
    if fast == None:
        return head.next
    
    while fast.next:
        slow = slow.next
        fast = fast.next
    
    slow.next = slow.next.next
    return head


# OR

'''
# Time complexity: O(2n)
# Space complexity: O(1)
def remove_nth(head, n):
    slow = head
    length = 0
    
    while slow:
        length += 1
        slow = slow.next
    
    if n == length:
        new_head = head.next
        return new_head
    
    pos_to_stop = length-n
    count = 1
    slow = head
    
    while count < pos_to_stop:
        slow = slow.next
        count+=1
    
    slow.next = slow.next.next
    
    return head
    '''