

#none

class Node:
    
    def __init__(self, data):
        self.data = data
        self.next = None
        
class LinkedList:
    
    def __init__(self):
        self.head = None
        
    def append(self, data):
        new_node = Node(data)
        
        if self.head == None:
            self.head = new_node
            return
        
        current_node = self.head
        
        while current_node:
            current_node = current_node.next
        
        current_node.next = new_node
        return
    
    def lenght(self):
        if self.head == None:
            return 0
        current_node = self.head
        total = 0
        
        while current_node:
            total += 1
            current_node = current_node.next
            
        return total
    
    #transformando a lista em um array de Python
    def to_list(self):
        node_data = []
        current_node = self.head
        
        while current_node:
            node_data.append(current_node.data)
            current_node = current_node.next
        return node_data
    
    def display(self):
        contents = self.head
        
        if contents is None:
            print("List has no element")
            
        while contents:
            print(contents.data)
            contents = contents.next
        print("-------------------")
    
    def get(self, index):
        if index >= self.lenght() or index < 0:
            print("Error: Index out of range")
            return None
        current_idx = 0
        current_node = self.head
        
        while current_node != None:
            if current_idx == index:
                return current_node.data
            current_node = current_node.next
            current_idx += 1
         
    def previous_linkedlist(self):
        previous_node = None
        current_node = self.head
        
        while current_node != None:
            next =  current_node.next
            current_node.next = previous_node
            previous_node = current_node
            current_node = next
        self.head = previous_node