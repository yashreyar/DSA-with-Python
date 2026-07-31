'''
LeetCode: https://leetcode.com/problems/linked-list-cycle-ii/
'''

# Time complexity: O(n)
# Space complexity: O(1)
def detectCycle(head):
    slow, fast = head, head
    hasCycle = False
    
    while fast != None and fast.next != None:
        slow = slow.next
        fast = fast.next.next
        if slow == fast:
            hasCycle = True
            break
    
    if hasCycle: 
        slow = head
        while slow != fast:
            slow = slow.next
            fast = fast.next
    else:
        return None
    
    # Both slow and fast points to same node, so we can return slow/fast
    return slow
'''
# Time complexity: O(n)
# Space complexity: O(n)
def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
    curr = head
    my_set = set()

    while curr != None:
        if curr in my_set:
            return curr
        my_set.add(curr)
        curr = curr.next
    return None
    '''
