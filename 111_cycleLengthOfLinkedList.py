"""
GFG: https://www.geeksforgeeks.org/problems/find-length-of-loop/1
"""


# Time complexity: O(n)
# Space complexity: O(1)
def cycle_Length(head):
    slow = fast = head

    # Detect cycle
    while fast != None and fast.next != None:
        slow = slow.next
        fast = fast.next.next

        if slow == fast:
            # Direct Cycle Length Count (O(1) extra space)
            count = 1
            temp = slow.next
            while temp != slow:
                count += 1
                temp = temp.next
            return count

    # Reached end of list -> No cycle
    return 0
