# This will be using the queue implementation using the linked list.
# The reason for creating the python file is to import it in the "Applicationis_of_stacks" jupyter notebook

class Empty(Exception):
    pass

class _Node:
    def __init__(self, data):
        self.data = data
        self.next_node = None
        self.prev_node = None


class Queue:
    """A queue implementation using a linked list as the underlying structure"""
    def __init__(self):
        self.head = None
        self.tail = None
        self.length = 0  # Used for len method
    
    def is_empty(self):
        """ check if queue is empty. True if empty, False otherwise """
        return self.head == None and self.tail == None
    
    def enqueue(self, data):
        """ add an item to the back of the queue """
        node = _Node(data)
        if self.is_empty():
            self.head = self.tail = node
            self.length += 1
            return
        node.next_node = self.tail
        self.tail.prev_node = node
        self.tail = node
        self.length += 1

    def dequeue(self):
        """ remove an item from the beginning of the queue """
        if self.is_empty():
            raise Empty('Queue is empty. Cannot remove')
        first_data = self.head.data
        self.head = self.head.prev_node
        if self.head is None:
            self.tail = None
        self.length -= 1
        return first_data
    
    def peek(self):
        """ return the current item at the top of the queue, without removing it """
        return self.head.data
    
    def __len__(self):
        """ return the length of the queue"""
        return self.length
    
    def __repr__(self):
        """ machine readable string representation of the queue """
        data_list = []
        current_node = self.tail
        while current_node:
            current_data = current_node.data
            data_list.append(current_data)
            current_node = current_node.next_node
        return " ".join([str(item) for item in data_list])