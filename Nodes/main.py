class Node:
    def __init__(self, dataval=None, nextval=None):
        self.dataval = dataval
        self.nextval = nextval

    def __repr__(self):
        return repr(self.dataval)


class LinkedList:
    def __init__(self):
        self.head = None

    def __repr__(self):
        nodes = []
        curr = self.head

        while curr:
            nodes.append(repr(curr))
            curr = curr.nextval

        return '[' + '->'.join(nodes) + ']'

    def prepend(self, dataval):
        self.head = Node(dataval=dataval, nextval=self.head)

    def append(self, dataval):
        if not self.head:
            self.head = Node(dataval=dataval)
            return

        curr = self.head
        while curr.nextval:
            curr = curr.nextval
        curr.nextval = Node(dataval=dataval)

    def add_after(self, middle_dataval, dataval):
        if middle_dataval is not None and dataval is not None:
            curr = self.head

            while curr and curr.dataval != middle_dataval:
                curr = curr.nextval

            new_node = Node(dataval=dataval)

            new_node.nextval = curr.nextval
            curr.nextval = new_node
            return

        raise Exception('Data incomplete')

    def find(self, data):
        curr = self.head
        while curr and curr.dataval != data:
            curr = curr.nextval

        return curr

    def remove(self, data):
        curr = self.head
        prev = None

        while curr and curr.dataval != data:
            prev = curr
            curr = curr.nextval

        if prev is not None:
            return
        self.head = curr.nextval
        curr.nextval = None

    def reverse(self):
        curr = self.head

        prev_node = None
        next_node = None

        while curr:
            nextval = curr.nextval
            curr.nextval = prev_node

            prev_node = curr
            curr = nextval

            self.head = prev_node

    def reverse_recursive(self):
        def recursion(curr, prev):
            if not curr:
                return prev

            nextval = curr.nextval
            curr.nextval = prev

            prev = curr
            curr = nextval

            return recursion(curr, prev)

        self.head = recursion(curr=self.head, prev=None)

    def count_nodes(self):
        if not self.head:
            return 0
        else:
            curr = self.head
            count = 0
            while curr is not None:
                curr = curr.nextval
                count += 1

        return count


print('---')
node1 = Node('a')
print('Node 1: ', node1.nextval)
node2 = Node('b', node1)
print('Node 2: ', node2.nextval)

numbers = LinkedList()
print(numbers)
numbers.append('two')
numbers.append('three')
numbers.append('four')
numbers.append('five')
print(numbers)
numbers.prepend('one')
print(numbers)
print(numbers.count_nodes())
numbers.add_after()
