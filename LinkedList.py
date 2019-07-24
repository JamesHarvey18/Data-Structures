class Node(object):

    def __init__(self, data=None, next_node=None):
        self.data = data
        self.next_node = next_node

    def get_data(self):
        return self.data

    def get_next(self):
        return self.next_node

    def set_next(self, new_next):
        self.next_node = new_next


class LinkedList(object):

    def __init__(self, head=None):
        self.head = head

    def insert(self, data):
        new_node = Node(data)
        new_node.set_next(self.head)
        self.head = new_node

    def size(self):
        current = self.head
        count = 0
        while current:
            count = count + 1
            current = current.get_next()
        return count

    def search(self, data):
        current = self.head
        found = False

        while current and not found:
            if current.get_data() == data:
                found = True
            else:
                current = current.get_next()
        if current is None:
            raise ValueError('Data not found')
        return current

    def delete(self, data):
        current = self.head
        previous = None
        found = False

        while current and not found:
            if current.get_data == data:
                found = True
            else:
                previous = current
                current = current.get_next()
        if current is None:
            raise ValueError('Data not found')
        if previous is None:
            self.head = current.get_next()
        else:
            previous.set_next(current.get_next())

    def halfway(self):
        slow = self.head
        fast = self.head

        while fast is not None and fast.get_next() is not None:
            slow = slow.get_next()
            fast = fast.get_next().get_next()

        print('Middle element:', slow.data)


a = LinkedList()
a.insert(1)
a.insert(2)
a.insert(3)
a.insert(4)
a.insert(5)
a.insert(6)
a.insert(7)
a.insert(8)
a.insert(9)
a.insert(10)
a.insert(11)

a.halfway()
print(a.head.get_data())
