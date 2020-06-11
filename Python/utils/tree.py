import sys
import os
sys.path.append(os.environ['WORKSPACE'])
from utils.queue import MyQueue

class TreeNode:

    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

class MyTree:
    
    def __init__(self, input_list):
        self.list = input_list
        self.root = self.__create_binary_tree()

    def __create_binary_tree(self):
        if self.list is None or len(self.list) == 0:
            return None
    
        data = self.list.pop(0)
        if data is None:
            return None
    
        node = TreeNode(data)
        node.left = self.__create_binary_tree()
        node.right = self.__create_binary_tree()
        return node

    def __pre_order_traversal_core(self, node):
        if node is None:
            return
    
        print(node.data, end = ' ')
        self.__pre_order_traversal_core(node.left)
        self.__pre_order_traversal_core(node.right)

    def __pre_order_traversal_with_stack_core(self, node):
        stack = []
        while node is not None or len(stack) > 0:
            while node is not None:
                print(node.data, end = ' ')
                stack.append(node)
                node = node.left
            
            if len(stack) > 0:
                node = stack.pop()
                node = node.right

    def __in_order_traversal_core(self, node):
        if node is None:
            return
    
        self.__in_order_traversal_core(node.left)
        print(node.data, end = ' ')
        self.__in_order_traversal_core(node.right)

    def __in_order_traversal_with_stack_core(self, node):
        stack = []
        while node is not None or len(stack) > 0:
            while node is not None:
                stack.append(node)
                node = node.left

            if len(stack) > 0:
                node = stack.pop()
                print(node.data, end = ' ')
                node = node.right

    def __post_order_traversal_core(self, node):
        if node is None:
            return

        self.__post_order_traversal_core(node.left)
        self.__post_order_traversal_core(node.right)
        print(node.data, end = ' ')

    def __post_order_traversal_with_stack_core(self, node):
        stack = [node]
        stack_assit = []
        while len(stack) > 0:
            node = stack.pop()
            stack_assit.append(node)

            if node.left is not None:
                stack.append(node.left)
            if node.right is not None:
                stack.append(node.right)

        while len(stack_assit) > 0:
            print(stack_assit.pop().data, end = ' ')

    def __level_order_traversal_core(self, node):
        q = MyQueue(10000)
        q.enqueue(node)
        while not q.empty():
            node = q.dequeue()
            print(node.data, end = ' ')
            if node.left is not None:
                q.enqueue(node.left)
            if node.right is not None:
                q.enqueue(node.right)

    def pre_order_traversal(self):
        self.__pre_order_traversal_core(self.root)

    def pre_order_traversal_with_stack(self):
        self.__pre_order_traversal_with_stack_core(self.root)

    def in_order_traversal(self):
        self.__in_order_traversal_core(self.root)

    def in_order_traversal_with_stack(self):
        self.__in_order_traversal_with_stack_core(self.root)

    def post_order_traversal(self):
        self.__post_order_traversal_core(self.root)

    def post_order_traversal_with_stack(self):
        self.__post_order_traversal_with_stack_core(self.root)

    def level_order_traversal(self):
        self.__level_order_traversal_core(self.root)

my_input_list = list([3, 2, 9, None, None, 10, None, None, 8, None, 4])
myTree = MyTree(my_input_list)
print("Pre-order traversal:")
myTree.pre_order_traversal()
print("\nPre-order traversal with stack:")
myTree.pre_order_traversal_with_stack()
print("\nIn-order traversal:")
myTree.in_order_traversal()
print("\nIn-order traversal with stack:")
myTree.in_order_traversal_with_stack()
print("\nPost-order traversal:")
myTree.post_order_traversal()
print("\nPost-order traversal with stack:")
myTree.post_order_traversal_with_stack()
print("\nLevel-order traversal:")
myTree.level_order_traversal()

