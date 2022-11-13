class MyQueue:
    def __init__(self):
        self.items = []

    def is_empty(self):
        return len(self.items) == 0

    def enqueue(self, item):
        self.items.append(item)

    def dequeue(self):
        return self.items.pop(0)

    def size(self):
        return len(self.items)

    def peek(self):
        if self.is_empty():
            raise Exception("Empty list")
        return self.items[0]

    def list(self):
        for item in self.items:
            print(item)


class Node:
    def __init__(self, data):
        self.left = None
        self.right = None

        self.data = data

    def get_left_child(self):
        return self.left

    def set_left_child(self, left):
        self.left = left

    def get_right_child(self):
        return self.right

    def set_right_child(self, right):
        self.right = right

    def get_value(self):
        return self.data

    def set_value(self, data):
        self.data = data

    def print_tree(self):
        if self.left:
            self.left.print_tree()
        print(self.data)
        if self.right:
            self.right.print_tree()


def insert(head, node):
    if head is None:
        return node

    if node.get_value() <= head.get_value():
        head.set_left_child(insert(head.get_left_child(), node))
    else:
        head.set_right_child(insert(head.get_right_child(), node))
    return head


def lookup(head, data):
    if head is None:
        return print("Value not found")
    if head.get_value() == data:
        return head
    if data <= head.get_value():
        return lookup(head.get_left_child(), data)
    else:
        return lookup(head.get_right_child(), data)


def print_node(node):
    try:
        print(node.get_value())
    except:
        pass


def min_value(head):
    current = head

    while current.left is not None:
        current = current.left
    return current.data


def max_value(head):
    current = head

    while current.right is not None:
        current = current.right
    return current.data


def breadth_first(node):
    if node is None:
        raise Exception("No root found")
    path = []
    queue = MyQueue()
    queue.enqueue(node)

    while queue.size() > 0:
        current = queue.dequeue()

        path.append(current.data)

        if current.get_left_child() is not None:
            queue.enqueue((current.get_left_child()))

        if current.get_right_child() is not None:
            queue.enqueue((current.get_right_child()))

    return path


def pre_order(node):
    path = []
    if node:
        path.append(node.data)

        path = path + pre_order(node.get_left_child())
        path = path + pre_order(node.get_right_child())
    return path


def in_order(node):
    path = []
    if node:
        path = path + in_order(node.get_left_child())
        path.append(node.data)
        path = path + in_order(node.get_right_child())
    return path

def post_order(node):
    path = []
    if node:
        path = path + in_order(node.get_left_child())
        path = path + in_order(node.get_right_child())
        path.append(node.data)
    return path



A = Node(45)
B = Node(2)
C = Node(33)
D = Node(54)
E = Node(25)
F = Node(68)
G = Node(72)
H = Node(81)
I = Node(23)
J = Node(1)

head = insert(None, E)
head.print_tree()
print('---')
insert(head, B)
head.print_tree()
print('---')
insert(head, C)
head.print_tree()
print('---')
insert(head, I)
insert(head, A)
head.print_tree()
print('---')
insert(head, G)
insert(head, F)
insert(head, D)
insert(head, H)
insert(head, J)
head.print_tree()

print('---')
print_node(lookup(head, 72))
print('min/max:')
print(min_value(head))
print(max_value(head))

print('Breadth first')
print(breadth_first(E))

print('Pre_order')
print(pre_order(E))

print('In_order')
print(in_order(E))

print('Post_order')
print(post_order(E))