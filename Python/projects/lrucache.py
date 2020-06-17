class Node:

    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.pre = None
        self.next = None

class MyLRUCache:

    def __init__(self, limit):
        self.limit = limit
        self.hash = {}
        self.head = None
        self.end = None

    def __add_node(self, node):
        if self.end is not None:
            self.end.next = node
            node.pre = self.end
            node.next = None
        self.end = node
        if self.head is None:
            self.head = node

    def __remove_node(self, node):
        if node == self.head and node == self.end:
            self.head = None
            self.end = None
        elif node == self.end:
            self.end = self.end.pre
            self.end.next = None
        elif node == self.head:
            self.head = self.head.next
            self.head.pre = None
        else:
            node.pre.next = node.pre
            node.next.pre = node.pre
        return node.key

    def __refresh_node(self, node):
        if node == self.end:
            return
        self.__remove_node(node)
        self.__add_node(node)

    def get(self, key):
        node = self.hash.get(key)
        if node is None:
            return None
        
        self.__refresh_node(node)
        return node.value

    def put(self, key, value):
        node = self.hash.get(key)
        if node is None:
            if len(self.hash) >= self.limit:
                old_key = self.__remove_node(self.head)
                self.hash.pop(old_key)
            
            node = Node(key, value)
            self.__add_node(node)
            self.hash[key] = node
        else:
            node.value = value
            self.__refresh_node(node)

    def remove(self, key):
        node = self.hash.get(key)
        self.__remove_node(node)
        self.hash.remove(key)

