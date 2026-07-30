class Node: 
    def __init__(self, val):
        self.val = val
        self.next = None


class SinglyLinkedList:
    def __init__(self):
        self.head = None

    # Append method
    def append_(self, val):
        new_node = Node(val)
        
        # If current linkedlist is empty
        if self.head is None:
            self.head = new_node
            return
        # If it has some nodes already
        curr = self.head
        while curr.next is not None:
            curr = curr.next
        curr.next = new_node

    # Traversal
    def traverse_(self):
        # If current linkedlist is empty
        if self.head is None:
            print("SLL is empty")
        # If it has some nodes already
        else:
            curr = self.head
            while curr is not None:
                print(curr.val, end=" -> ")
                curr = curr.next
            print("None")

    # Insert value at index
    def insert_(self, val, position):
        new_node = Node(val)
        
        # Inserting at 0th postion
        if position == 0:
            new_node.next = self.head
            self.head = new_node
            
        # Inserting in between
        else:
            curr = self.head
            prev_node = None
            count = 0
            while curr is not None and count < position:
                prev_node = curr
                curr = curr.next
                count+=1
            
            if prev_node is not None:
                prev_node.next = new_node
                new_node.next = curr

    # Delete a node
    def delete_(self, val):
        # Handle empty list
        if self.head is None:
            print("SLL is empty")
            return
        
        # If list has only 1 node
        if self.head.val == val:
            self.head = self.head.next
            return
        
        # Handle deleting any other node
        curr = self.head
        prev = None
        found = False

        while curr is not None:
            if curr.val == val:
                found = True
                break
            prev = curr
            curr = curr.next

        if found:
            prev.next = curr.next
        else:
            print("Node not found")


sll = SinglyLinkedList()
sll.append_(2)
sll.append_(3)
sll.append_(4)
sll.traverse_()
sll.insert_(10, 2)
sll.traverse_()
sll.delete_(4)
sll.delete_(87)
sll.traverse_()