class TreeNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

def create_binary_tree(input_list=[]):
    if input_list is None or len(input_list) == 0:
        return None
    
    data = input_list.pop(0)
    if data is None:
        return None
    
    node = TreeNode(data)
    node.left = create_binary_tree(input_list)
    node.right = create_binary_tree(input_list)
    return node

def pre_order_traversal(node):
    if node is None:
        return
    
    print(node.data, end = ' ')
    pre_order_traversal(node.left)
    pre_order_traversal(node.right)
    return node

def pre_order_traversal_with_stack(node):
    stack = []
    while node is not None or len(stack) > 0:
        while node is not None:
            print(node.data, end = ' ')
            stack.append(node)
            node = node.left
            
        if len(stack) > 0:
            node = stack.pop()
            node = node.right

def in_order_traversal(node):
    if node is None:
        return
    
    in_order_traversal(node.left)
    print(node.data, end = ' ')
    in_order_traversal(node.right)
    return node

def in_order_traversal_with_stack(node):
    stack = []
    while node is not None or len(stack) > 0:
        while node is not None:
            stack.append(node)
            node = node.left

        if len(stack) > 0:
            node = stack.pop()
            print(node.data, end = ' ')
            node = node.right

def post_order_traversal(node):
    if node is None:
        return

    post_order_traversal(node.left)
    post_order_traversal(node.right)
    print(node.data, end = ' ')

def post_order_traversal_with_stack(node):
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

def level_order_traversal(node):
    queue = Queue()
    queue.put(node)
    while not queue.empty():
        node = queue.get()
        print(node.data, end = ' ')
        if node.left is not None:
            queue.put(node.left)
        if node.right is not None:
            queue.put(node.right)

my_input_list = list([3, 2, 9, None, None, 10, None, None, 8, None, 4])
root = create_binary_tree(my_input_list)
print("Pre-order traversal:")
pre_order_traversal(root)
print("\nPre-order traversal with stack:")
pre_order_traversal_with_stack(root)
print("\nIn-order traversal:")
in_order_traversal(root)
print("\nIn-order traversal with stack:")
in_order_traversal_with_stack(root)
print("\nPost-order traversal:")
post_order_traversal(root)
print("\nPost-order traversal with stack:")
post_order_traversal_with_stack(root)
print("\nLevel-order traversal:")
#level_order_traversal(root)

