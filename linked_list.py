

class node:
    """
    Creates nodes to store data in linked_list class
    """
    
    def __init__(self, data_val = None):
        # set data to previous Node and next Node to None
        self.data_val = data_val
        self.next = None
    
class linked_list:
    """
    Creates a linked list which data can be appended to and removed from. 
    
    Contains the following functions:
        append() \n
        pop() \n
        length() \n
        show_list() \n
        get() \n
        remove() \n
    """

    def __init__(self):
        # create head of linked list (should always be empty of data)
        self.head_node = node()


    def append(self, data):
        """
        Appends input data to the end of the linked list. 

        input:  (Any) data
                Data of any type to be appended to the linked list
        output: None
        """
        # add new node to linked list
        new_node = node(data)
        current_node = self.head_node
        # traverse linked list till end is found and append new_node
        while current_node.next != None:
            current_node = current_node.next
        current_node.next = new_node
    
    
    def append_after(self, data, prior_node):
        """
        Append value to linked list after first instance of specific value.
        If more than one instance is present, the first match in the list from the head will be used.

        input : (Any) data - value to be appended
                (Any) prior_node - value of node that data is to be appended after
        output : None 
        """
        
        current_node = self.head_node.next
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
            print(f'ERROR: value "{prior_node}" not found in linked list. Node was not added.')
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
        placeholder = self.head_node.next
        # append to front of linked list
        new_node.next = placeholder
        self.head_node.next = new_node
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
        count = 0
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
        while current_node.next != None:
            current_node = current_node.next
            nodes.append(current_node.data_val)
        print(nodes)


    def get(self, requested_index: int):
        """
        Returns data from specified index.

        input:  (int) requested_index
                Index of node to be returned
        output: (int) 
                Data returned
        """
        # check to see input is an int and throw exception 
        if ~isinstance(requested_index, int):
            print("Error: Invalid input. Index must be of type 'int'")
            return None
        # check to see index requested exists
        elif requested_index >= self.length():
            print("Error: Index is out of bounds.")
            return None
        
        node_index = 0
        current_node = self.head_node
        while current_node.next != 0:
            current_node = current_node.next
            if requested_index == node_index:
                return current_node.data_val
            node_index += 1
            

    def remove(self, requested_index: int):
        """
        Removes selected node from linked list. Takes desired index of node to remove.

        input:  (int) requested_index
                Index of node to be removed
        output: None
        """
        # check to see input is an int and throw exception 
        if ~isinstance(requested_index, int):
            print("Error: Invalid input. Index must be of type 'int'")
            return None
        # check to see index requested exists
        if requested_index >= self.length():
            print("Error: Index is out of bounds.")
            return None
        node_index = 0
        current_node = self.head_node
        while current_node.next != None:
            # if the current node is a match, bypass it by connecting previous node to current_node.next
            previous_node = current_node
            current_node = current_node.next
            if node_index == requested_index:
                previous_node.next = current_node.next
                break
            node_index += 1



tester = linked_list()
tester.append(5)
tester.append('bus station')
tester.append(2)
tester.show_list()
tester.pop()
print(tester.length())
print(tester.get('tree'))
tester.remove(2)
tester.append_after(35, 5)
tester.append_after(57, 999)
tester.show_list()

tester.show_list()
