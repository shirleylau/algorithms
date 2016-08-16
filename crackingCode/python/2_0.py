# Write code to remove duplicates from an unsorted linked list

class Node:

    prev: Node
    nex: Node
    first: Node
    last: Node
    val: string

    def __init__(self, val):
        self.val = val
        self.prev = None
        self.nex = None
        self.first = None
        self.last = None

    def insert_after(self, node):
        if self.nex is not None:
            self.nex.prev = node
            node.last = self.last
        else:
            node.last = node
            active = node
            while active.prev is not None:
                active = active.prev
                active.last = node
        node.nex = self.nex
        node.prev = self
        self.nex = node

    def remove_self(self):
        if self.prev is not None:
            self.prev.nex = self.nex
        else:
            self.nex.first = self.nex
            active = self.nex
            while active.nex is not None:
                active = active.nex
                active.nex =

        if self. nex is not None:
            self.nex.prev = self.prev
        self.nex = self.prev = self.last


first_one = Node('wabooo')
first_one.prev = None


 def remove
