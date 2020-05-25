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

def in_order_traversal(node):
    if node is None:
        return
    
    in_order_traversal(node.left)
    print(node.data, end = ' ')
    in_order_traversal(node.right)
    return node

def post_order_traversal(node):
    if node is None:
        return

    post_order_traversal(node.left)
    post_order_traversal(node.right)
    print(node.data, end = ' ')
    return node

my_input_list = list([3, 2, 9, None, None, 10, None, None, 8, None, 4])
root = create_binary_tree(my_input_list)
print("Pre-order traversal:")
pre_order_traversal(root)
print("\nIn-order traversal:")
in_order_traversal(root)
print("\nPost-order traversal:")
post_order_traversal(root)

