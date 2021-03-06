#-*-coding:utf-8-*-
__author__ = 'shenshen'

from node import Node, DoublyLinkedNode
import copy


class DoublyLinkedList(object):
    def __init__(self):
        self.first = None
        self.last = None

    def isEmpty(self):
        return self.first is None

    def pushHead(self, data):
        node = DoublyLinkedNode(data)
        if self.isEmpty():
            self.first = node
            self.last = node
        else:
            oldfirst = self.first
            node.next = oldfirst
            oldfirst.prev = node
            self.first = node

    def pushTail(self, data):
        node = DoublyLinkedNode(data)
        if self.isEmpty():
            self.first = node
            self.last = node
        else:
            oldlast = self.last
            oldlast.next = node
            node.prev = oldlast
            self.last = node

    def popHead(self):
        if self.isEmpty():
            return None
        poped = self.first
        self.first = self.first.next
        self.first.prev = None
        return poped

    def popTail(self):
        if self.isEmpty():
            return None
        poped = self.last
        self.last = self.last.prev
        self.last.next = None
        return poped

    def insertBefore(self, data, before):
        current = self.first
        found = False
        while current is not None and not found:
            if current.getData() == before:
                found = True
            else:
                current = current.next
        if found:
            if current == self.first:
                self.pushHead(data)
            else:
                node = DoublyLinkedNode(data)
                prev = current.prev
                prev.next = node
                current.prev = node
                node.prev = prev
                node.next = current
        return found

    def insertAfter(self, data, after):
        current = self.first
        found = False
        while current is not None and not found:
            if current.getData() == after:
                found = True
            else:
                current = current.next
        if found:
            if current == self.last:
                self.pushTail(data)
            else:
                node = DoublyLinkedNode(data)
                nextnode = current.next
                current.next = node
                nextnode.prev = node
                node.prev = current
                node.next = nextnode
        return found

    def delete(self, data):
        current = self.first
        found = False
        while current is not None and not found:
            if current.getData() == data:
                found = True
            else:
                current = current.getNext()
        if found:
            prevnode = current.prev
            nextnode = current.next
            prevnode.next = nextnode
            nextnode.prev = prevnode

    def toList(self):
        result = []
        current = self.first
        while current is not None:
            result.append(current.getData())
            current = current.getNext()
        return result


class UnorderedList(object):
    def __init__(self):
        """creates a new list that is empty.
        It needs no parameters and returns an empty list"""
        self.head = None

    def add(self, item):
        """add(item) adds a new item to the list.
        It needs the item and returns nothing. """
        temp = Node(item)
        temp.setNext(self.head)
        self.head = temp

    def append(self, item):
        """adds a new item to the end of the list making it the last item in the collection.
        It needs the item and returns nothing. """
        if self.isEmpty():
            self.add(Node(item))

        current = self.head
        stop = False
        while current is not None and not stop:
            if current.getNext() is None:
                stop = True
            else:
                current = current.getNext()
        temp = Node(item)
        if current is None:
            self.head.setNext(temp)
        else:
            current.setNext(temp)

    def remove(self, item):
        """removes the item from the list.
        It needs the item and modifies the list. """
        current = self.head
        previous = None
        found = False
        while current is not None and not found:
            if item == current.getData():
                found = True
            else:
                previous = current
                current = current.getNext()
        if current is None:
            return
        if previous is None:
            self.head = current.getNext()
        else:
            previous.setNext(current.getNext())


    def search(self, item):
        """searches for the item in the list.
        It needs the item and returns a boolean value."""
        current = self.head
        found = False
        while current != None and not found:
            if item == current.getData():
                found = True
            else:
                current = current.getNext()
        return found

    def isEmpty(self):
        """tests to see whether the list is empty.
         It needs no parameters and returns a boolean value."""
        return self.head == None

    def length(self):
        """returns the number of items in the list.
        It needs no parameters and returns an integer."""
        current = self.head
        count = 0
        while current != None:
            count = count + 1
            current = current.getNext()
        return count

    def index(self, item):
        """returns the position of item in the list.
        It needs the item and returns the index. """
        pos = 0
        found = False
        current = self.head
        while current is not None and not found:
            if item == current.getData():
                found = True
            else:
                pos = pos + 1
                current = current.getNext()
        if found:
            return pos
        else:
            return -1

    def insert(self, pos, item):
        """adds a new item to the list at position pos.
        It needs the item and returns nothing. """
        if pos == 0:
            self.add(item)

        if pos >= self.length():
            self.append(item)
            return

        current = self.head
        previous = None
        count = 0
        while count < pos:
            count = count + 1
            previous = current
            current = current.getNext()

        temp = Node(item)
        temp.setNext(current)
        previous.setNext(temp)

    def pop(self, pos = 0):
        """ removes and returns the last item in the list.
        It needs nothing and returns an item. """
        if self.length() == 0:
            return None

        if pos >= self.length():
            return None

        current = self.head
        previous = None
        count = 0
        while count < pos:
            count = count + 1
            previous = current
            current = current.getNext()

        if previous is None:
            temp = current.getNext()
            self.head = temp
        else:
            temp = current.getNext()
            previous.setNext(temp)
        return current

    def toList(self):
        """convert the linked data to a list, and return it"""
        current = self.head
        result = []
        while current is not None:
            result.append(current.getData())
            current = current.getNext()
        return result


class OrderedList(object):
    def __init__(self):
        """creates a new ordered list that is empty"""
        self.head = None

    def add(self, item):
        """adds a new item to the list making sure that the order is preserved.
        It needs the item and returns nothing.
        """
        current = self.head
        previous = None
        stop = False
        while current is not None and not stop:
            if current.getData() > item:
                stop = True
            else:
                previous = current
                current = current.getNext()

        temp = Node(item)
        if previous is None:
            temp.setNext(self.head)
            self.head = temp
        else:
            temp.setNext(current)
            previous.setNext(temp)

    def remove(self, item):
        """removes the item from the list.
        It needs the item and modifies the list."""
        current = self.head
        previous = None
        found = False
        while current is not None and not found:
            if item == current.getData():
                found = True
            else:
                previous = current
                current = current.getNext()
        if current is None:
            return
        if previous is None:
            self.head = current.getNext()
        else:
            previous.setNext(current.getNext())

    def search(self, item):
        """searches for the item in the list.
        It needs the item and returns a boolean value."""
        current = self.head
        found = False
        stop = False
        while current is not None \
            and found is False \
            and stop is False:
            if item == current.getData():
                found = True
                stop = True
            elif item < current.getData():
                stop = True
            else:
                current = current.getNext()
        return found

    def index(self, item):
        """returns the position of item in the list.
        It needs the item and returns the index. """
        if self.length() == 0:
            return -1
        current = self.head
        count = 0
        while current is not None:
            if item == current.getData():
                return count
            else:
                current = current.getNext()
                count = count + 1
        return -1

    def length(self):
        """returns the number of items in the list.
        It needs no parameters and returns an integer."""
        current = self.head
        count = 0
        while current is not None:
            count = count + 1
            current = current.getNext()
        return count

    def pop(self, pos):
        """removes and returns item in the list.
        It needs nothing and returns an item. """
        if pos < 0 or pos > self.length() - 1:
            return None
        previous = None
        current = self.head
        count = 0
        while count < pos:
            previous = current
            current = current.getNext()
            count = count + 1
        temp = current.getNext()
        previous.setNext(temp)
        return current

    def isEmpty(self):
        """tests to see whether the list is empty.
        It needs no parameters and returns a boolean value."""
        return self.head is None

    def toList(self):
        """convert the linked data to a list, and return it"""
        current = self.head
        result = []
        while current is not None:
            result.append(current.getData())
            current = current.getNext()
        return result


def moveToFront(num):
    data = []
    for _ in range(num):
        data.append(raw_input())

    ul = UnorderedList()
    for d in data:
        if ul.search(d):
            ul.remove(d)
        ul.add(d)

    print(ul.toList())


def test():
    # moveToFront(5)
    #temp = Node(11)
    #print temp.getData()
    #print temp.getNext()
    testlist = DoublyLinkedList()
    testlist.pushHead(34)
    testlist.pushHead(78)
    testlist.insertAfter(25, 78)
    testlist.insertBefore(36, 78)
    testlist.pushTail(1)
    testlist.pushTail(56)
    testlist.delete(78)
    # print(testlist.popHead().getData())
    # print(testlist.popTail().getData())
    print(testlist.toList())
    # another = copy.copy(testlist)
    another = copy.deepcopy(testlist)
    testlist.popTail()
    print(testlist.toList())
    print(another.toList())


    #print(testlist.length())
    #print(testlist.search(1))
    #print(testlist.search(99))
    # testlist.remove(1)
    # testlist.append(12)
    # testlist.add(21)
    #print(testlist.length())

if __name__ == '__main__':
    test()