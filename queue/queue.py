
from linked_list.linked_list import Double_Side_Linked_List

class Queue(Double_Side_Linked_List):

    def enqueue(self,value):
        self.addFirst(value)
    
    def dequeue(self):
        return self.getLast()

    def peek(Self):
        return self.tail.value



