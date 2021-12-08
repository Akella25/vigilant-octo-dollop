
class ListItem:

    prev = None
    data = None
    next = None

    def __init__(self, data):
        self.data = data

    def __str__(self):
        return str(self.data)


class LinkedList:

    head = None

    def __init__(self, data):
        self.head = ListItem(data=data)

    def __iter__(self):
        self._current = self.head
        return self

    def __next__(self):
        tmp = self._current
        if tmp is not None:
            self._current = self._current.next
            return tmp
        else:
            raise StopIteration()

    def add_element(self, data):
        new_element = ListItem(data=data)
        tail = self.head
        while tail.next is not None:
            tail = tail.next
        tail.next = new_element
        new_element.prev = tail

    def my_find(self, data):
        head = self.head
        while head.next is not None:
            if head.data == data:
                return head.data
            head = head.next

    def my_insert(self, index, data):
        head = self.head
        count = 0
        item = ListItem(data=data)

        if index == 0:
            next_head = self.head
            self.head = item
            self.head.next = next_head
            return

        while head.next is not None:
            if count == index - 1:
                next_head = head.next
                head.next = item
                head.next.next = next_head
            count += 1
            head = head.next

    def my_extend(self, data_list):
        for item in data_list:
            self.add_element(item)

    def print_list(self):
        current = self.head
        while current is not None:
            print(current.data)
            current = current.next

    def delete_element(self, data):
        if self.head.data == data:
            tmp = self.head
            self.head = self.head.next
            del tmp
            return

        current = self.head
        while current.next is not None:
            if current.next.data == data:
                tmp = current.next
                current.next = current.next.next
                del tmp
                return
            else:
                currnet = currnet.next


class Dequeue:

    def __init__(self):
        self._items = []

    def add_to_tail(self, element):
        self._items.append(element)

    def add_to_head(self, element):
        self._items.insert(0, element)

    def pop_from_tail(self):
        return self._items.pop(-1)

    def pop_from_head(self):
        return self._items.pop(0)

    @property
    def empty(self):
        return not bool(self._items)