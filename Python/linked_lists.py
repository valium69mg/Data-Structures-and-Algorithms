class Node:
    data = None
    next_node = None 

    def __init__(self,data):
        self.data = data

    def __repr__(self):
        return "<Node data: %s>" % self.data

class LinkedList:
    
    def __init__(self):
        self.head = None
    
    def __repr__(self):
        nodes = []
        current = self.head

        while current:
            if current is self.head:
                nodes.append("[Head: %s]" % current.data)
            elif current.next_node is None:
                nodes.append("[Tail: %s]" % current.data)
            else:
                nodes.append("[%s]" % current.data)
            current = current.next_node
        return '-> '.join(nodes)
    
    def node_at_index(self,index):
        if index == 0:
            return self.head
        else:
            current = self.head 
            position = 0

            while position < index:
                current = current.next_node
                position += 1

            return current

    def is_empty(self):
        return self.head == None
    
    def insert(self,data,index):
        if index == 0:
            self.add(data)
        if index > 0:
            new = Node(data)

            position = index
            current = self.head

            while position > 1:
                current = current.next_node
                position -= 1

            prev = current 
            next_node = current.next_node

            prev.next_node = new
            new.next_node = next_node
    
    def remove(self,key):
        current = self.head 
        previous = None
        found = False
        while current and not found:
            if current.data == key and current == self.head:
                found = True 
                self.head = current.next_node
            elif current.data == key:
                found = True 
                previous.next_node = current.next_node
            else:
                previous = current 
                current = current.next_node
        return current
    
        
    def size(self):
        """
        Counts the elements and returns the size of the list
        Takes linear time
        """
        current = self.head
        count = 0
        while current:
            count += 1
            current = current.next_node
        return count
    
    def add(self,data):
        """
        Adds new Node containing data at the head of the list
        Takes O(1) time
        """
        new_node = Node(data)
        new_node.next_node = self.head
        self.head = new_node
    

    def search(self,key):
        current = self.head

        while current:
            if current.data == key:
                return current
            else: 
                current = current.next_node
        
        return None
        



list = LinkedList()
