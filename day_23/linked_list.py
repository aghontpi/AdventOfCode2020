#! /usr/bin/python3


class Node():
    def __init__(self, value):
        self.value = value
        self.next = None
        self.last = None


class LinkedList():
    def __init__(self):
        self.head = None
        self.position_map = {}
        self.extracted_elements = {}

    def push(self, value):
        if not self.head:
            self.head = Node(value)
            self.last = self.head
            self.position_map[self.head.value] = self.head
        else:
            # fast - for partTwo
            assert(self.last)
            node = Node(value)
            self.position_map[node.value] = node
            self.last.next = node
            self.last = self.last.next

            # slow
#            node = Node(value)
#            last = self.head
#            while last.next:
#                last = last.next
#            last.next = node
            # print(
            #     f'node inserted after : {last.value}, inserted: {last.next.value}')

#    def deleteAt(self, value):
#        if not self.head:
#            return
#        nodes = self.head
#        if nodes and nodes.value == value:
#            self.head = self.head.next
#            nodes = None
#            # print(f'node deleted at head, new head : {self.head}')
#            return
#
#        prev = self.head
#        while nodes:
#            if nodes.value == value:
#                if nodes.next:
#                    # print(
#                    #     f'node deleted {nodes.value}, after {prev.value}.-> {nodes.next.value}')
#                    prev.next = nodes.next
#                    return
#                else:
#                    # print(f'node deleted at end')
#                    prev.next = None
#                    return
#            prev = nodes
#            nodes = nodes.next

    def extract_elements(self):
        node = self.head
        self.extracted_elements = {}
        i = 0
        while i < 3:
            node = node.next
            self.extracted_elements[node.value] = node.next
            i += 1
        self.head.next = node.next

    def insertExtractedElements(self, value):
        node = self.head
        _next = None
        # fast - for partTwo
        assert(value in self.position_map)
        node = self.position_map[value]
        _next = node.next
        items = self.extracted_elements
        for _x in items:
            newnode = Node(_x)  
            node.next = newnode
            node = node.next
            self.position_map[node.value] = node
        node.next = _next
        if _next == None:
            self.last = node
        self.extracted_elements = {}
        node = node.next
        return

        # slow
#        while node:
#            _next = node.next
#            if node.value == value:
#                items = self.extracted_elements
#                for _x in items:
#                    newnode = Node(_x)  # remove conversion to int
#                    node.next = newnode
#                    node = node.next
#                node.next = _next
#                self.extracted_elements = {}
#            node = node.next

    def moveHead(self):
        # fast - for partTwo
        assert(self.last)
        assert(self.last.next == None)
        newhead = self.head.next
        self.last.next = self.head
        self.last.next.next = None
        self.position_map[self.last.value] = self.last
        self.head = newhead
        self.position_map[self.head.value] = self.head
        self.last = self.last.next
        return
        # slow
#        head = self.head
#        newhead = head.next
#        node = newhead.next
#        while node.next:
#            node = node.next
#        node.next = head
#        node.next.next = None
#        self.position_map[node.next.value] = node.next
#        self.head = newhead
#        self.position_map[self.head.value] = self.head

    def _print(self):
        node = self.head
        while node:
            print(f'{node.value}', end=' -> ')
            node = node.next
        print('None')
        if self.extracted_elements:
            print('extracted : ', end='')
            for x in self.extracted_elements:
                print(x, end=' ')
