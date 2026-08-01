"""
GFG: https://www.geeksforgeeks.org/problems/find-pairs-with-given-sum-in-doubly-linked-list/1

head: 1 <-> 2 <-> 4 <-> 5 <-> 6 <-> 8 <-> 9
target = 7
Output: [[1, 6], [2, 5]]
Explanation: There are two pairs (1, 6) and (2,5) with sum 7.
"""


# Time complexity: O(n+k) = O(n)
# Space complexity: O(1) Auxiliary space
def pair_sum(head, target):
    start = head
    end = head
    result = []

    while end.next is not None:             # time: O(n)
        end = end.next

    while start != None and end != None and start != end and end.next != start:           # time: O(k)
        if start.data + end.data == target:
            result.append([start.data, end.data])
            start = start.next
            end = end.prev
        elif start.data + end.data < target:
            start = start.next
        else:
            end = end.prev

    return result


"""
# Time complexity: O(n+klogk)
# Space complexity: O(n)
def pair_sum(head, target):
    my_set = set()
    curr = head
    result = []
    
    while curr is not None:
        remaining = target - curr.data
        if remaining in my_set:
            result.append([remaining, curr.data]) 
        my_set.add(curr.data)
        curr = curr.next
    result.sort()                               # Time: O(klogk) k -> no of valid pairs found
    return result
    """


# OR

"""
# Time complexity: O(n^2)
# Space complexity: O(1) Auxiliary Space
def pair_sum(head, target):
    result = []
    curr = head
    
    while curr is not None:
        front = curr.next
        while front is not None:
            if curr.data + front.data == target:
                result.append([curr.data, front.data])
            front = front.next
        curr = curr.next
    return result
    """
