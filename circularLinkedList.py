"""
Class for implementing a Python circular linked list data structure. 
Head value contains the 1st value in the list. 
Last node is connected to head node
Uses 'node' class to add nodes to 'CircularLinkedList' class.
Author : Blake Livermore 2022
"""

class Node():
    """
    Creates nodes to store data in CircularLinkedList class
    """
    def __init__(self, data):
        self.data = data
        self.next = None

class CircularLinkedList():
    """
    Creates a circular linked list which data can be appended to and removed from. 
    
    Contains the following functions:
        append() \n
        prepend() \n
        pop() \n
        length() \n
        show_list() \n
    """

    def __init__(self):
        self.head = None
    
    def append(self, data):
        """
        Append input data to the end of the linked list. 

        input:  (Any) data
                Data of any type to be appended to the linked list
        output: None
        """
        new_node = Node(data)

        # special cases
        if self.head == None:
            self.head = new_node
            self.head.next = self.head
            return
        
        cur_node = self.head
        while cur_node.next != self.head:
            cur_node = cur_node.next
        new_node.next = self.head
        cur_node.next = new_node


    def prepend(self, data):
        """
        Appends input data to the beginning of the linked list. 

        input:  (Any) data
                Data of any type to be appended to the linked list
        output: None
        """
        new_node = Node(data)

        # special cases
        if self.head == None:
            self.head = new_node
            return

        # find last node to attach to new head
        cur_node = self.head
        while cur_node.next != self.head:
            cur_node = cur_node.next
        
        # reorder nodes to have new_node as head
        cur_node.next = new_node
        old_head = self.head
        self.head = new_node
        new_node.next = old_head
        return
        
    
    def pop(self):
        """
        Removes last node from linked list. 

        input:  None
        output: None
        """
        # special cases
        if self.head == None:
            print("Error: Linked List is empty. Unable to pop()")
            return 

        cur_node = self.head
        prev_node = None

        while cur_node.next != self.head:
            prev_node = cur_node
            cur_node = cur_node.next
        prev_node.next = self.head


    def show_list(self):
        """
        Displays the contents of the linked list.

        input:  None
        output: None
        """

        # special cases
        if self.head == None:
            return

        nodes = []
        cur_node = self.head
        nodes.append(cur_node.data)
        while cur_node.next != self.head:
            cur_node = cur_node.next
            nodes.append(cur_node.data)
        print(nodes)


    def length(self):
        """
        Returns length of linked list.

        input:  None
        output: None
        """

        # special cases
        if not self.head:
            return 0
        
        cur_node = self.head
        count = 1
        while cur_node.next != self.head:
            cur_node = cur_node.next
            count += 1
        return count
