#-*-coding:utf-8-*-
__author__ = 'shenshen'

class BinaryTree(object):
    def __init__(self, rootObj):
        self.key = rootObj
        self.leftChild = None
        self.rightChild = None

    def insertLeft(self, newObj):
        if self.leftChild is None:
            self.leftChild = BinaryTree(newObj)
        else:
            t = BinaryTree(newObj)
            t.leftChild = self.leftChild
            self.leftChild = t

    def insertRight(self, newObj):
        if self.rightChild is None:
            self.rightChild = BinaryTree(newObj)
        else:
            t = BinaryTree(newObj)
            t.rightChild = self.rightChild
            self.rightChild = t

    def getRightChild(self):
        return self.rightChild

    def getLeftChild(self):
        return self.leftChild

    def setRootVal(self,obj):
        self.key = obj

    def getRootVal(self):
        return self.key

def ListsTree(r):
    return [r, [], []]

def insertLeft(root, newBranch):
    t = root.pop(1)
    if len(t) > 1:
        root.insert(1, [newBranch, t, []])
    else:
        root.insert(1, [newBranch, [], []])
    return root

def insertRight(root,newBranch):
    t = root.pop(2)
    if len(t) > 1:
        root.insert(2,[newBranch,[],t])
    else:
        root.insert(2,[newBranch,[],[]])
    return root

def getRootVal(root):
    return root[0]

def setRootVal(root,newVal):
    root[0] = newVal

def getLeftChild(root):
    return root[1]

def getRightChild(root):
    return root[2]

def buildListsTree():
    tree = ListsTree('a')
    insertLeft(tree, 'b')
    insertRight(tree, 'c')
    insertRight(getLeftChild(tree), 'd')
    insertLeft(getRightChild(tree), 'e')
    insertRight(getRightChild(tree), 'f')
    return tree

def buildBinaryTree():
    root = BinaryTree('a')
    root.insertLeft('b')
    root.insertRight('c')
    root.getLeftChild().insertRight('d')
    root.getRightChild().insertLeft('e')
    root.getRightChild().insertRight('f')
    return root

if __name__ == '__main__':
    # r = BinaryTree(3)
    # insertLeft(r,4)
    # insertLeft(r,5)
    # insertRight(r,6)
    # insertRight(r,7)
    # l = getLeftChild(r)
    # print(l)
    #
    # setRootVal(l,9)
    # print(r)
    # insertLeft(l,11)
    # print(r)
    # print(getRightChild(getRightChild(r)))
    # t = buildListsTree()
    # print(getRootVal(getRightChild(t)))
    # print(getRootVal(getRightChild(getLeftChild(t))))
    # print(getRootVal(getRightChild(getRightChild(t))))

    ttree = buildBinaryTree()

    print(ttree.getRightChild().getRootVal())
    print(ttree.getLeftChild().getRightChild().getRootVal())
    print(ttree.getRightChild().getLeftChild().getRootVal())
