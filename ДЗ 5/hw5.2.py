class Node:

    def __init__(self, value):
        self.value = value  
        self.left = None    
        self.right = None   

class BinarySearchTree:
    """Простое бинарное дерево поиска"""
    def __init__(self):
        self.root = None  

    def insert(self, value):

        if self.root is None:

            self.root = Node(value)
        else:

            self._insert_recursive(self.root, value)

    def _insert_recursive(self, node, value):

        if value < node.value:
            if node.left is None:
                node.left = Node(value)
            else:
                self._insert_recursive(node.left, value)
        else:
            if node.right is None:
                node.right = Node(value)
            else:
                self._insert_recursive(node.right, value)

    def find(self, value):
        return self._find_recursive(self.root, value)

    def _find_recursive(self, node, value):
        if node is None:
            return False  
        if value == node.value:
            return True  
        elif value < node.value:
            return self._find_recursive(node.left, value)
        else:
            return self._find_recursive(node.right, value)

    def print_tree(self):

        self._print_in_order(self.root)

    def _print_in_order(self, node):
        if node:
            self._print_in_order(node.left)
            print(node.value, end=" ")
            self._print_in_order(node.right)
