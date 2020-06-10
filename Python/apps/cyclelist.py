import sys
sys.path.append('../')
from utils.linkedlist import Node

class MyCycleList:

    def __init__(self, node):
        self.head = node
        self.is_cycle = False
        self.cycle_length = 0
        self.cycle_start = self.head        
        self.slow = self.head
        self.fast = self.head

    def check_cycle(self):
        while self.fast is not None and self.fast.next is not None:
            self.slow = self.slow.next
            self.fast = self.fast.next.next

            if self.slow == self.fast:
                self.is_cycle = True
                return

    def check_cycle_length(self):
        if self.is_cycle:
            p1 = self.slow
            p2 = self.fast
                            
            while 1:
                p1 = p1.next
                p2 = p2.next.next
                self.cycle_length += 1                    
                    
                if p1 == p2:
                    return

    def check_cycle_start(self):
        if self.is_cycle:
            p1 = self.slow
            p2 = self.fast

            while 1:
                p1 = p1.next
                p2 = p2.next

                if p1 == p2:
                    self.cycle_start = p1
                    return

    def output(self):
        print("Cycle length:", end = ' ')
        print(self.cycle_length)
        print("Cycle start point:", end = ' ')
        print(self.cycle_start.data)

node1 = Node(5)
node2 = Node(3)
node3 = Node(7)
node4 = Node(2)
node5 = Node(6)
node1.next = node2
node2.next = node3
node3.next = node4
node4.next = node5
node5.next = node2

cycle = MyCycleList(node1)
cycle.check_cycle()
cycle.check_cycle_length()
cycle.check_cycle_start()
cycle.output()

