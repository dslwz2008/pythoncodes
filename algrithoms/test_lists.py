#-*-coding:utf-8-*-
__author__ = 'shenshen'

from lists import Node
from lists import UnorderedList
from lists import OrderedList
import unittest

class TestNode(unittest.TestCase):
    def setUp(self):
        pass

    def test_setData(self):
        node = Node(36)
        node.setData(25)
        self.assertEqual(node.getData(), 25)

    def test_setNext(self):
        node = Node(36)
        node1 = Node(25)
        node.setNext(node1)
        self.assertEqual(node.getNext(), node1)

class TestOrderedList(unittest.TestCase):
    def setUp(self):
        pass

    def test_add(self):
        l = OrderedList()
        l.add('test')
        l.add(1)
        l.add('ABC')
        self.assertEqual(l.toList(), ['ABC', 1, 'test'])

    def test_remove(self):
        l = OrderedList()
        l.add('test')
        l.add(1)
        l.add('ABC')
        l.remove(1)
        self.assertEqual(l.toList(), ['ABC', 'test'])

    def test_search(self):
        l = OrderedList()
        l.add('test')
        l.add(1)
        l.add('ABC')
        self.assertEqual(l.search('ABC'), True)
        self.assertEqual(l.search(2), False)

    def test_index(self):
        l = OrderedList()
        l.add('test')
        l.add(100)
        l.add('ABC')
        self.assertEqual(l.index(100), 1)
        self.assertEqual(l.index(2), -1)

    def test_length(self):
        l = OrderedList()
        l.add('test')
        l.add(100)
        l.add('ABC')
        self.assertEqual(l.length(), 3)

    def test_pop(self):
        l = OrderedList()
        l.add('test')
        l.add(100)
        l.add('ABC')
        self.assertEqual(l.pop(-1), None)
        self.assertEqual(l.pop(5), None)
        self.assertEqual(l.pop(0), 'test')

    def test_isEmpty(self):
        l = OrderedList()
        l.add('test')
        l.add(100)
        l.add('ABC')
        self.assertEqual(l.isEmpty(), False)
        l.remove('test')
        l.remove(100)
        l.remove('ABC')
        self.assertEqual(l.isEmpty(), True)

class TestUnorderedList(unittest.TestCase):
    def setUp(self):
        pass

    def test_add(self):
        l = UnorderedList()
        l.add(34)
        l.add('test')
        self.assertEqual(l.length(), 2)
        self.assertEqual(l.toList(), ['test', 34])

    def test_append(self):
        l = UnorderedList()
        l.append(34)
        l.append('test')
        self.assertEqual(l.length(), 2)
        self.assertEqual(l.toList(), [34, 'test'])

    def test_index(self):
        l = UnorderedList()
        l.add('test')
        l.add(34)
        l.add(0)
        l.append(78)
        self.assertEqual(l.length(), 4)
        self.assertEqual(l.toList(), [0, 34, 'test', 78])
        pos = l.index(34)
        self.assertEqual(pos, 1)

    def test_remove(self):
        l = UnorderedList()
        l.add('test')
        l.add(34)
        l.add(0)
        l.append(78)
        self.assertEqual(l.length(), 4)
        self.assertEqual(l.toList(), [0, 34, 'test', 78])
        l.remove(34)
        self.assertEqual(l.toList(), [0, 'test', 78])
        l.remove(45)
        self.assertEqual(l.toList(), [0, 'test', 78])

    def test_index(self):
        l = UnorderedList()
        l.add('test')
        l.add(34)
        l.add(0)
        l.append(78)
        self.assertEqual(l.index(78), 3)
        self.assertEqual(l.index(0), 0)
        self.assertEqual(l.index('test'), 2)

    def test_insert(self):
        l = UnorderedList()
        l.add('test')
        l.add(34)
        l.add(0)
        l.append(78)
        l.insert(2, 'inserted')
        self.assertEqual(l.toList(), [0, 34, 'inserted', 'test', 78])
        l.insert(4, 'out')
        self.assertEqual(l.toList(), [0, 34, 'inserted', 'test', 'out', 78])
        l.insert(0, 12)
        self.assertEqual(l.toList(), [12, 0, 34, 'inserted', 'test', 'out', 78])
        l.insert(10, 100)
        self.assertEqual(l.toList(), [12, 0, 34, 'inserted', 'test', 'out', 78])

    def test_pop(self):
        l = UnorderedList()
        l.add('test')
        l.add(34)
        l.add(0)
        l.append(78)
        l.pop(2)
        self.assertEqual(l.toList(), [0, 34, 78])
        l.pop(0)
        self.assertEqual(l.toList(), [34, 78])
        l.pop(5)
        self.assertEqual(l.toList(), [34, 78])
        l.pop()
        self.assertEqual(l.toList(), [78])


if __name__ == '__main__':
    unittest.main()
