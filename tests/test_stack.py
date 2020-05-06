
import pytest

# That's horrible I know
from stack.stack import Stack

class Test_Stack:
    
    def test_push_and_pop(self):
        thisStack = Stack()
        thisStack.push(1)
        assert(thisStack.pop() == 1)
        assert(thisStack.size == 0)
    

    def test_empty(self):
        thisStack = Stack()
        thisStack.push(1)
        thisStack.pop()
        assert(thisStack.isEmpty())
    
    def test_error(self):
        with pytest.raises(LookupError):
            thisStack = Stack()
            thisStack.pop()

    def test_peek(self):
        thisStack = Stack()
        thisStack.push(1)
        assert(thisStack.peek == 1) 
        thisStack.push(2)        
        assert(thisStack.peek == 2)