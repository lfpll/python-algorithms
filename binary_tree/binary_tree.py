class Binary_Tree:

    class Node:
        
        def __init__(self, value):
            self.left = None
            self.right = None
            self.value = value

    def __init__(self, root):
        self.size = 0
        self.root = Node(root)

    def add_value(self,value,node=self.root):
        if node is None:
            return Node(value)
        elif node.value < value:
            node.right = add_value(value,node.right)
        else:
            node.left = add_value(value,node.left)
        return node

    def find_biggest_to_right(node,value):
        if node.right:
            return find_biggest_to_right(node.right,value)
        else:
            return node
            
    def remove_value(self,value,node=self.root):
        if node.value == value:
            
        elif node.value < value:
            pass
        else:
        

            