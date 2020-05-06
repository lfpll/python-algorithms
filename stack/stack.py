from linked_list.linked_list import Double_Side_Linked_List

class Stack(Double_Side_Linked_List):


    def push(self,value):
        self.addFirst(value)
    
    def pop(self):
        return self.getFirst()

    def peek(self):
        self.check_if_empty()
        return self.head.value

    def isEmpty(self):
        return self.size == 0