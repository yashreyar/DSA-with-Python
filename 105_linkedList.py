class Node:
    def __init__(self, val):
        self.val = val
        self.next = None
        
node1 = Node(5)
node2 = Node(2)
node3 = Node(6)
node4 = Node(1)
node5 = Node(4)

node1.next = node2
node2.next = node3
node3.next = node4
node4.next = node5

print(node1.val)
print(node1.next.val)
print(node1.next.next.next.next.val)