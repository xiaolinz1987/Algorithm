import queue

class TreeNode:

    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

class MyTree:
    
    def __init__(self, input_list):
        self.list = input_list
        self.root = self.__create_binary_tree()
        self.tree = []

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

        self.tree.append(node.data)
        self.__pre_order_traversal_core(node.left)
        self.__pre_order_traversal_core(node.right)

    def __pre_order_traversal_with_stack_core(self, node):
        stack = []
        while node is not None or len(stack) > 0:
            while node is not None:
                self.tree.append(node.data)
                stack.append(node)
                node = node.left
            
            if len(stack) > 0:
                node = stack.pop()
                node = node.right

    def __in_order_traversal_core(self, node):
        if node is None:
            return
    
        self.__in_order_traversal_core(node.left)
        self.tree.append(node.data)
        self.__in_order_traversal_core(node.right)

    def __in_order_traversal_with_stack_core(self, node):
        stack = []
        while node is not None or len(stack) > 0:
            while node is not None:
                stack.append(node)
                node = node.left

            if len(stack) > 0:
                node = stack.pop()
                self.tree.append(node.data)
                node = node.right

    def __post_order_traversal_core(self, node):
        if node is None:
            return

        self.__post_order_traversal_core(node.left)
        self.__post_order_traversal_core(node.right)
        self.tree.append(node.data)

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
            self.tree.append(stack_assit.pop().data)

    def __level_order_traversal_core(self, node):
        q = queue.Queue(10000)
        q.put(node)
        while not q.empty():
            node = q.get()
            self.tree.append(node.data)
            if node.left is not None:
                q.put(node.left)
            if node.right is not None:
                q.put(node.right)

    def pre_order_traversal(self):
        self.tree = []
        self.__pre_order_traversal_core(self.root)

    def pre_order_traversal_with_stack(self):
        self.tree = []
        self.__pre_order_traversal_with_stack_core(self.root)

    def in_order_traversal(self):
        self.tree = []
        self.__in_order_traversal_core(self.root)

    def in_order_traversal_with_stack(self):
        self.tree = []
        self.__in_order_traversal_with_stack_core(self.root)

    def post_order_traversal(self):
        self.tree = []
        self.__post_order_traversal_core(self.root)

    def post_order_traversal_with_stack(self):
        self.tree = []
        self.__post_order_traversal_with_stack_core(self.root)

    def level_order_traversal(self):
        self.tree = []
        self.__level_order_traversal_core(self.root)

    def get_tree(self):
        return self.tree
