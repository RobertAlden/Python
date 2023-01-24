import time


class Node:
    def __init__(self, x):
        self.val = x
        self.next_n = None

    def get(self):
        return self.val

    def next_node(self):
        return self.next_n


class SimpleLinkedList:
    def __init__(self):
        self.head = None

    def append(self, x):
        if self.head is None:
            self.head = Node(x)
            return
        ref = self.head
        while ref.next_node() is not None:
            ref = ref.next_node()
        ref.next_n = Node(x)

    def print(self):
        if self.head is None:
            return
        ref = self.head
        print(ref.get(), end=" ")
        while ref.next_node() is not None:
            ref = ref.next_node()
            print(ref.get(), end=" ")
        print("")


class FastAppendLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def append(self, x):
        if self.head is None:
            self.head = Node(x)
            self.tail = self.head
            return
        self.tail.next_n = Node(x)
        self.tail = self.tail.next_node()

    def print(self):
        if self.head is None:
            return
        ref = self.head
        print(ref.get(), end=" ")
        while ref.next_node() is not None:
            ref = ref.next_node()
            print(ref.get(), end=" ")
        print("")


def main():
    nodes = 10000
    fall = FastAppendLinkedList()
    tic = time.perf_counter()
    for i in range(nodes*100):
        fall.append(i)
    toc = time.perf_counter()
    print(f"Built Fast Append Linked List with {nodes*100} nodes in {toc - tic:0.4f} seconds")
    #fall.print()

    sll = SimpleLinkedList()
    tic = time.perf_counter()
    for i in range(nodes):
        sll.append(i)
    toc = time.perf_counter()
    print(f"Built Simple Linked List with {nodes} nodes in {toc - tic:0.4f} seconds")


if __name__ == "__main__":
    main()
