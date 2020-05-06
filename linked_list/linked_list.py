# A node of al i
class Node:

    def __init__(self, value, next=None, previous=None):
        self.next = next
        self.previous = previous
        self.value = value


class Double_Side_Linked_List:
    def __init__(self, head: Node = None, tail: Node = None, size=0):
        self.head = head
        self.tail = tail
        self.size = size

    def __iter__(self):
        return self

    def __next__(self):
        this_node = self.head
        while this_node is not None:
            yield this_node
            this_node = this_node.next
            
    def addFirst(self, value):
        new_head = Node(value)
        new_head.value = value

        # Checking if exists
        if self.size == 0:
            self.head = new_head
            self.tail = new_head
        else:
            old_head = self.head
            new_head.next = old_head
            old_head.previous = new_head
            self.head = new_head

        self.size += 1
        print('New Head is %s' % str(value))

    def addLast(self, value):
        new_tail = Node(value)
        new_tail.value = value

        if self.size == 0:
            self.head = new_tail
            self.tail = self.head
        else:
            old_tail = self.tail
            new_tail.previous = old_tail
            old_tail.next = new_tail
            self.tail = new_tail

        self.size += 1
        print('New Tail is %s' % str(value))

    def check_if_empty(self):
        if self.size == 0:
            raise LookupError("This linked list is empty")

    def getFirst(self):
        self.check_if_empty()
        old_head = self.head
        
        if self.size == 1:
            self.head = None
            self.tail = None
        else:
            self.head = old_head.next
            if self.head is not None:
                self.head.previous = None
        
        self.size -= 1
        return old_head.value

    def getLast(self):
        self.check_if_empty()
        self.size -= 1
        old_tail = self.tail

        if self.size == 1:
            self.head = None
            self.tail = None
        else:
            self.tail = old_tail.previous
            if self.tail is not None:
                self.tail.next = None
        
        self.size -= 1
        return old_tail.value


    def getByIndex(self, index): 
        if index + 1 > self.size:
            raise LookupError("Index bigger then number of values")
        
        # Check to see if it's faster to go backwards
        if index+1 > self.size / 2:
            this_node = self.tail
            for _ in range(self.size - (index+1)):
                this_node = value.previous
        else:
            this_node = self.head
            for _ in range(index):
                this_node = value.next

        next_val = this_node.next
        previous_val = this_node.previous
        
        # In the middle
       
        if next_val is None and previous_val is None:
            self.tail = None
            self.head = None
        elif next_val is None and previous_val is None:
            next_val.previous = previous_val
            previous_val.next = next_val
        elif previous_val is None:
            # Meaning there is a next value
            self.head = next_val
            next_val.previous = None
        else:
            # This should be the tai
            self.tail = previous_val
            previous_val.next = None

        
        self.size -= 1
        return this_node.value
