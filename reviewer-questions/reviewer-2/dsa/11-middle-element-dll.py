class Node:
    def __init__(self, value):
        self.prev = None
        self.value = value
        self.next = None
        
class DoublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        
    def insert_at_begin(self, value):
        new_node = Node(value)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.next = self.head
            self.head.prev = new_node
            self.head = new_node
            
    def insert_at_end(self, value):
        new_node = Node(value)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            new_node.prev = self.tail
            self.tail = new_node
            
    def convert_arr_to_dll(self, arr):
        for i in arr:
            self.insert_at_end(i)
            
    def display(self):
        current = self.head
        while current:
            print(current.value, end = " <-> ")
            current = current.next
        print("None")
        
    def display_reverse(self):
        current = self.tail
        while current:
            print(current.value, end = " <-> ")
            current = current.prev
        print("None")
           
    def delete(self, value):
        if self.head is None:
            return
        
        if self.head.value == value:
            if self.head == self.tail:
                self.head = None
                self.tail = None
            else:
                self.head = self.head.next
                self.head.prev = None
            return
        
        else:
            current = self.head.next
            while current is not None:
                if current.value == value:
                    if current == self.tail:
                        self.tail = current.prev
                        self.tail.next = None
                    else:
                        current.prev.next = current.next
                        current.next.prev = current.prev
                    return
                current = current.next
            
    def insert_before(self, value, data):
        if self.head is None:
            return
        
        if self.head.value == value:
            self.insert_at_begin(data)
            return
        
        current = self.head
        while current.next:
            if current.next.value == value:
                new_node = Node(data)
                new_node.next = current.next
                current.next.prev = new_node
                new_node.prev = current
                current.next = new_node
                return
            current = current.next
            
    def insert_after(self, value, data):
        if self.head is None:
            return
        
        current = self.head
        while current:
            if current.value == value:
                if current == self.tail:
                    self.insert_at_end(data)
                else:
                    new_node = Node(data)
                    new_node.next = current.next
                    current.next.prev = new_node
                    new_node.prev = current
                    current.next = new_node
                return
            current = current.next
            
    def reverse(self):
        if self.head is None:
            return
        
        current = self.head
        while current:
            current.next, current.prev = current.prev, current.next
            current = current.prev
            
        self.head, self.tail = self.tail, self.head
        
    def find_middle(self):
        if self.head is None:
            return
        slow = fast = self.head
        while fast.next and fast.next.next:
            slow = slow.next
            fast = fast.next.next
        return slow.value
        
    def insert_node_at_index(self, index, value):
        if index < 0:
            return 
        
        if index == 0:
            self.insert_at_begin(value)
            return
        
        i = 1
        current = self.head
        while current:
            if index == i:
                if current == self.tail:
                    self.insert_at_end(value)
                else:
                    new_node = Node(value)
                    new_node.next = current.next
                    current.next.prev = new_node
                    new_node.prev = current
                    current.next = new_node
                return
            current = current.next
            i += 1
            
    def remove_duplicates(self):
        if self.head is None:
            return
        
        current = self.head
        seen = {self.head.value}
        while current.next:
            if current.next.value in seen:
                if current.next == self.tail:
                    self.tail = current
                    current.next = None
                else:
                    current.next = current.next.next
                    current.next.prev = current
            else:
                seen.add(current.next.value)
                current = current.next

            
dll = DoublyLinkedList()

dll.convert_arr_to_dll([1, 2, 3, 3, 2, 4, 5, 6])

dll.display()

dll.remove_duplicates()

dll.display()
