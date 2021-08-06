#!usr/bin/python
# Author:   @AgbaD || @agba_dr3


class Node:
    def __init__(self, data=None):
        self.data = data
        self.prev = None
        self.next = None


class CLinkedList:
    def __init__(self):
        self.root = None
        self.tail = None

    # insert start
    def prepend(self, value):
        if not self.root:
            self.root = Node(value)
        else:
            if not self.root.next:
                temp = self.root
                self.tail = temp
                self.root = Node(value)
                self.root.next = self.tail
                self.root.prev = self.tail
                self.tail.prev = self.root
                self.tail.next = self.root
            else:
                q = self.root
                self.root = Node(value)
                self.root.next = q
                q.prev = self.root
                self.root.prev = self.tail
                self.tail.next = self.root

    # insert end
    def append(self, value):
        if not self.root:
            self.root = Node(value)
        else:
            if self.tail:
                p = self.tail.prev
                q = self.tail
                p.next = q
                q.prev = p
                self.tail = Node(value)
                q.next = self.tail
                self.tail.prev = q
                self.tail.next = self.root
            else:
                self.tail = Node(value)
                self.tail.next = self.root
                self.tail.prev = self.root
                self.root.next = self.tail
                self.root.prev = self.tail

    # remove start
    def pop(self):
        if not self.root:
            print("Circular linked list is empty!")
            return
        else:
            if not self.root.next:
                self.root = None
            else:
                n = self.root.next
                if n == self.tail:
                    self.root = self.tail
                    self.root.next = None
                    self.root.prev = None
                    self.tail = None
                else:
                    self.root = n
                    self.root.prev = self.tail
                    self.tail.next = self.root

    # remove end
    def push(self):
        if not self.root:
            print("Circular linked list is empty!")
            return
        else:
            if not self.root.next:
                self.root = None
            else:
                p = self.tail.prev
                if p == self.root:
                    self.tail = None
                    self.root.next = None
                    self.root.prev = None
                else:
                    self.tail = p
                    self.tail.next = self.root
                    self.root.prev = self.tail

    # remove value
    def remove_value(self, value):
        lst = self.traverse()
        if not lst:
            print("Circular linked list is empty")
            return
        elif value not in lst:
            print("Value isn't present in circular linked list")
            return
        else:
            ind = lst.index(value)
            if lst[ind] == lst[-1]:
                p = self.tail.prev
                self.tail = p
                self.tail.next = self.root
                self.root.prev = self.tail
            elif ind == 0:
                if self.root.next:
                    n = self.root.next
                    if n == self.tail:
                        self.root = n
                        self.root.next = None
                        self.root.prev = None
                        self.tail = None
                    else:
                        self.root = n
                        self.root.prev = self.tail
                        self.tail.next = self.root
                else:
                    self.root = None
            else:
                cur = self.root
                for i in range(ind):
                    cur = cur.next
                p = cur.prev
                n = cur.next
                p.next = n
                n.prev = p

    # traverse
    def traverse(self):
        if not self.root:
            print("Circular linked list is empty")
            return None
        else:
            lst = [self.root.data]
            if self.root.next:
                cur = self.root
                while cur.next != self.tail:
                    cur = cur.next
                    lst.append(cur.data)
                lst.append(self.tail.data)
            print(lst)
            return lst


if __name__ == "__main__":
    lst = CLinkedList()

    lst.traverse()

    lst.append(17)
    lst.prepend(16)
    lst.prepend(15)
    lst.prepend(14)
    lst.prepend(13)
    lst.prepend(12)

    lst.traverse()

    lst.append(18)
    lst.append(19)

    lst.traverse()

    lst.pop()
    lst.push()
    lst.push()

    lst.traverse()

    lst.remove_value(15)
    lst.traverse()
