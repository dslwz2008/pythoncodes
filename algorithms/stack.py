#-*-coding:utf-8-*-
__author__ = 'shenshen'

from node import Node


class Stack(object):
    def __init__(self):
        self.items = []

    def isEmpty(self):
        return self.items == []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        return self.items.pop()

    def peek(self):
        return self.items[len(self.items) - 1]

    def size(self):
        return len(self.items)


class StackL(object):
    def __init__(self):
        self.first = None
        self.number = 0

    def isEmpty(self):
        return self.first is None

    def size(self):
        return self.number

    def push(self, item):
        oldfirst = self.first
        self.first = Node(item)
        self.first.next = oldfirst
        self.number += 1

    def pop(self):
        data = self.first.data
        self.first = self.first.next
        self.number -= 1
        return data

    def peek(self):
        if self.first is not None:
            return self.first.data


class IterableStack(Stack):
    def __init__(self):
        Stack.__init__(self)
        self.index = -1

    def __iter__(self):
        self.index = len(self.items)
        return self

    def next(self):
        self.index -= 1
        if self.index >= 0:
            return self.items[self.index]
        else:
            raise StopIteration


def test():
    # s = StackL()
    s = IterableStack()
    print(s.isEmpty())
    s.push(4)
    s.push('dog')
    print(s.peek())
    s.push(True)
    print(s.size())
    print(s.isEmpty())
    s.push(8.4)
    for i in s:
        print(i)
    # print(s.pop())
    # print(s.pop())
    # print(s.size())

def revstring(mystr):
    s = Stack()
    for i in mystr:
        s.push(i)
    result = []
    while not s.isEmpty():
        result.append(s.pop())
    return ''.join(result)

def testEqual(str1, str2):
    return str1 == str2

def parChecker(symbolString):
    s = Stack()
    balanced = True
    index = 0
    while index < len(symbolString) and balanced:
        symbol = symbolString[index]
        if symbol == "(":
            s.push(symbol)
        else:
            if s.isEmpty():
                balanced = False
            else:
                s.pop()

        index = index + 1

    if balanced and s.isEmpty():
        return True
    else:
        return False

def parChecker2(symbolString):
    s = Stack()
    balanced = True
    index = 0
    while index < len(symbolString) and balanced:
        symbol = symbolString[index]
        if symbol in "([{":
            s.push(symbol)
        else:
            if s.isEmpty():
                balanced = False
            else:
                top = s.pop()
                if not matches(top,symbol):
                       balanced = False
        index = index + 1
    if balanced and s.isEmpty():
        return True
    else:
        return False

def matches(open,close):
    opens = "([{"
    closers = ")]}"
    return opens.index(open) == closers.index(close)

def baseConverter(decNumber,base):
    digits = "0123456789ABCDEF"

    remstack = Stack()

    while decNumber > 0:
        rem = decNumber % base
        remstack.push(rem)
        decNumber = decNumber // base

    newString = ""
    while not remstack.isEmpty():
        newString = newString + digits[remstack.pop()]

    return newString

def infixToPostfix(infixexpr):
    prec = {}
    prec["^"] = 4
    prec["*"] = 3
    prec["/"] = 3
    prec["+"] = 2
    prec["-"] = 2
    prec["("] = 1
    opStack = Stack()
    postfixList = []
    tokenList = infixexpr.split()

    for token in tokenList:
        if token in "ABCDEFGHIJKLMNOPQRSTUVWXYZ" or token in "0123456789":
            postfixList.append(token)
        elif token == '(':
            opStack.push(token)
        elif token == ')':
            topToken = opStack.pop()
            while topToken != '(':
                postfixList.append(topToken)
                topToken = opStack.pop()
        else:
            while (not opStack.isEmpty()) and \
                            prec[opStack.peek()] >= prec[token]:
                    postfixList.append(opStack.pop())
            opStack.push(token)

    while not opStack.isEmpty():
        postfixList.append(opStack.pop())
    return " ".join(postfixList)

def postfixEval(postfixExpr):
    operandStack = Stack()
    tokenList = postfixExpr.split()

    for token in tokenList:
        if token in "0123456789":
            operandStack.push(int(token))
        else:
            operand2 = operandStack.pop()
            operand1 = operandStack.pop()
            result = doMath(token,operand1,operand2)
            operandStack.push(result)
    return operandStack.pop()

def doMath(op, op1, op2):
    if op == "*":
        return op1 * op2
    elif op == "/":
        return op1 / op2
    elif op == "+":
        return op1 + op2
    else:
        return op1 - op2


def matchParenthesis(expr):
    vals = StackL()
    ops = StackL()
    for c in expr:
        if c in '123456789':
            vals.push(c)
        elif c in '+-*':
            ops.push(c)
        elif c in ')':
            right = vals.pop()
            left = vals.pop()
            oper = ops.pop()
            result = '(%s%s%s)' % (left, oper, right)
            vals.push(result)
    return vals.pop()


if __name__ == '__main__':
    test()
    #print testEqual(revstring('apple'),'elppa')
    #print testEqual(revstring('x'),'x')
    #print testEqual(revstring('1234567890'),'0987654321')
    # print(parChecker('((()))'))
    # print(parChecker('(()'))
    # print(baseConverter(25, 8))
    # print(baseConverter(256, 16))
    # print(infixToPostfix("A * B + C * D"))
    # print(infixToPostfix("( A + B ) * C - ( D - E ) * ( F + G )"))
    # print(infixToPostfix("A + B * C / ( D - E )"))
    # print(postfixEval("4 5 6 * +"))
    # print(infixToPostfix("5 * 3 ^ ( 4 - 2 )"))
    # print(matchParenthesis('1+2)*3-4)*5-6)))'))
