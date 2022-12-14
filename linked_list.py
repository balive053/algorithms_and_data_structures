"""
Class for implementing a Python linked list data structure. 
Head value contains the 1st value in the list. 
Uses 'node' class to add nodes to 'LinkedList' class.
Author : Blake Livermore 2022
"""

class node:
    """
    Creates nodes to store data in LinkedList class
    """
    
    def __init__(self, data_val):
        # set data to previous Node and next Node to None
        self.data_val = data_val
        self.next = None
    
class LinkedList:
    """
    Creates a linked list which data can be appended to and removed from. 
    
    Contains the following functions:
        append() \n
        append_after() \n
        prepend() \n
        pop() \n
        length() \n
        show_list() \n
        get() \n
        remove() \n
        swap_nodes() \n
        reverse_list() \n
        remove_duplicates() \n
        nth_value() \n
    """

    def __init__(self):
        # create dummy head of linked list
        self.head_node = None


    def append(self, data):
        """
        Append input data to the end of the linked list. 

        input:  (Any) data
                Data of any type to be appended to the linked list
        output: None
        """
        # add new node to linked list
        new_node = node(data)
        # special case of new linked list
        if self.head_node == None:
            self.head_node = new_node
            return 

        current_node = self.head_node
        # traverse linked list till end is found and append new_node
        while current_node.next != None:
            current_node = current_node.next
        current_node.next = new_node
        return


    def append_after_instance(self, data, prior_node):
        """
        Append value to linked list after first instance of specific value.
        If more than one instance is present, the first match in the list from the head will be used.

        input : (Any) data - value to be appended
                (Any) prior_node - value of node that data is to be appended after
        output : None 
        """
        
        current_node = self.head_node
        while current_node.data_val != prior_node and current_node.next != None:
            current_node = current_node.next
        
        # append after value if found, else do not append and display error message
        if current_node.data_val == prior_node:
            new_node = node(data)
            placeholder = current_node.next
            current_node.next = new_node
            current_node = current_node.next
            current_node.next = placeholder
        else:
            print(f'ERROR: value "{prior_node}" not found in linked list. Node was not added. ' +
            'Note: Method is instance, not index based.')
        return None

    
    def prepend(self, data):
        """
        Appends input data to the beginning of the linked list. 

        input:  (Any) data
                Data of any type to be appended to the linked list
        output: None
        """

        # create new node to insert after head_node and placeholder for head_node.next
        new_node = node(data)
        new_node.next = self.head_node
        self.head_node = new_node
        return None
    

    def pop(self):
        """
        Removes last node from linked list. 

        input:  None
        output: None
        """
        # check linked list is not empty
        current_node = self.head_node
        if current_node.next == None:
            print("Error: Linked list is empty")
            return None
        
        # else traverse linked link to end and bypass final node
        while current_node.next != None:
            previous_node = current_node
            current_node = current_node.next
        previous_node.next = current_node.next


    def length(self):
        """
        Returns length of linked list.

        input:  None
        output: None
        """
        count = 1
        current_node = self.head_node
        while current_node.next != None:
            current_node = current_node.next
            count += 1
        return count
        

    def show_list(self):
        """
        Displays the contents of the linked list.

        input:  None
        output: None
        """
        nodes = []
        current_node = self.head_node
        # traverse linked list and append each node to list
        while current_node:
            nodes.append(current_node.data_val)
            current_node = current_node.next
        print(nodes)


    def get(self, requested_index: int):
        """
        Returns data from specified index.

        input:  (int) requested_index
                Index of node to be returned
        output: (int) 
                Data returned
        """
        ## Error handling
        # check to see input is an int and throw exception 
        if not isinstance(requested_index, int):
            print("Error: Invalid input. Index must be of type 'int'")
            return None
        # check to see index requested exists
        elif requested_index >= self.length():
            print("Error: Index is out of bounds.")
            return None
        
        node_index = 0
        current_node = self.head_node
        while current_node.next != 0:
            
            if requested_index == node_index:
                return current_node.data_val
            current_node = current_node.next
            node_index += 1
            

    def remove(self, requested_index: int):
        """
        Removes selected node from linked list. Takes desired index of node to remove.

        input:  (int) requested_index
                Index of node to be removed
        output: None
        """
        ## Error handling
        list_len = self.length()
        # check to see input is an int and throw exception
        if not isinstance(requested_index, int):
            print("Error: Invalid input. Index must be of type 'int'. Index could not be removed.")
            return None

        # check to see index requested exists
        if requested_index > list_len-1:
            print("Error: Index is out of bounds. Index not removed. Note: Uses zero indexing.")
            return None
        
        # special case handling (index [0, len-1])
        if requested_index == list_len-1:
            self.pop()
            return 
        if requested_index == 0:    
            self.head_node = self.head_node.next
            return
            
        node_index = 1
        current_node = self.head_node

        while current_node:
            # if the current node is a match, bypass it by connecting previous node to current_node.next
            previous_node = current_node
            current_node = current_node.next
            
            if node_index == requested_index:
                previous_node.next = current_node.next
                del current_node 
                break
            node_index += 1


    def swap_nodes(self, key1, key2):
        """
        Swap data values of two nodes by index.

        input: (int) key1 
               index of node 1 to swap
               (int) key2 
               index of node 2 to swap
        output: None
        """
        # special case, keys match
        if key1 == key2:
            return
        ## Error handling
        # Out of bounds error
        list_len = self.length()
        if key1 > list_len-1 or key2 > list_len-1:
            print("ERROR: Index out of bounds. Note: Uses zero indexing.")
            return None

        counter = 0
        curr_node1, curr_node2 = None, None
        
        current_node = self.head_node
        while current_node:
            # find the nodes at the index to be switched 
            if counter == key1:
                curr_node1 = current_node
            if counter == key2:
                curr_node2 = current_node
            counter += 1
            current_node = current_node.next

        # error handling
        # if curr_node1.data_val == None or curr_node2.data_val == None:
        #     print("ERROR: Node not found. Nodes unable to be swapped.")
        #     return None

        # switch node data    
        curr_node1.data_val, curr_node2.data_val = curr_node2.data_val, curr_node1.data_val
        return None


    def reverse_list(self):
        """"
        Reverses all values in the linked list.

        input:  None
        output: None
        """

        prev_node = None
        curr_node = self.head_node
        
        while curr_node:
            # store next node
            next_node = curr_node.next
            # reverse curr next to current prev and prev to curr
            curr_node.next = prev_node
            prev_node = curr_node
            # move to next node
            curr_node = next_node
        self.head_node = prev_node
        return None
    
    def remove_duplicates(self):
        """
        Removes all duplicate nodes from linked list.

        input:  None
        output: None
        """
        curr_node = self.head_node
        prev_node = None
        duplicates = dict()

        while curr_node:
            if curr_node.data_val in duplicates:
                # Remove node:
                prev_node.next = curr_node.next
                curr_node = None
            else:
                # Have not encountered element before.
                duplicates[curr_node.data_val] = 1
                prev_node = curr_node
                curr_node = prev_node.next
            curr_node = prev_node.next
    
    
    def nth_value(self, n):
        """
        Returns value in linked list where n is value of index.
        Allows for both positive indexing (from start of list) and negative indexing (from end of list).

        input:  (int) n
                index value to be returned. e.g. n = 1 will return first value.
        output: (node.data_val) value on node at index n
        """
        length = self.length()
        if abs(n) > length or n == 0:
            return "Error: Index out of bounds."
        # account for negative indexing to return from end of list
        if n < 0:
            n = length+n+1

        counter = 1
        curr_node = self.head_node
        
        while counter < n:
            curr_node = curr_node.next
            counter += 1
        return curr_node.data_val
