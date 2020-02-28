class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

    def add(self, value):
        self.next = Node(value)

    def middle(self):
        while self.next is not None:
            current_value = self.value
            self.next.next
        return current_value


