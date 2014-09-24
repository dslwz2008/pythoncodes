#-*-coding:utf-8-*-
__author__ = 'shenshen'

from stack import Stack

def main():
    groups = []
    m = int(raw_input())
    for i in range(m):
        n = int(raw_input())
        group = []
        for j in range(n):
            group.append(raw_input())
        groups.append(group)

    #print(groups)
    for g in groups:
        stack = Stack()
        for item in g:
            cmds = item.split()
            if cmds[0] == 'push':
                stack.push(int(cmds[1]))
            elif cmds[0] == 'pop':
                if stack.isEmpty():
                    print('error')
                    break
                else:
                    stack.pop()
        if not stack.isEmpty():
            print(' '.join([str(i) for i in stack.items]))



if __name__ == '__main__':
    main()
