# -*-coding:utf-8-*-
__author__ = 'shenshen'

import wx
import random
import copy

class LifeGame(object):
    def __init__(self, dim=10, steps=100, grids=None):
        self.steps = steps
        self.dim = dim #width=height
        if grids is None or not self.check_grids(grids, dim):
            self.initialize()
            self.buffer = copy.deepcopy(self.grids)
        else:
            self.grids = grids
            self.buffer = copy.deepcopy(grids)

    def check_grids(self, grids, dim):
        try:
            if len(grids) != dim:
                return False
            for i in range(dim):
                if len(grids[i]) != dim:
                    return False
        except:
            return False
        return True

    def initialize(self):
        self.random_init()

    def random_init(self):
        self.grids = []
        for i in range(self.dim):
            tmp = []
            for j in range(self.dim):
                tmp.append(random.randint(0,1))
            self.grids.append(tmp)

    def print_grids(self):
        for i in range(self.dim):
            print(''.join([str(self.grids[i][j]) for j in range(self.dim)]))

    def apply_rules(self):
        for i in range(self.dim):
            for j in range(self.dim):
                nbs = self.neighbors(i, j)
                if nbs <= 2: #die
                    self.buffer[i][j] = 0
                elif nbs == 3: #procreation
                    self.buffer[i][j] = 1
                elif nbs >= 5: #die
                    self.buffer[i][j] = 0
                else: #remains
                    self.buffer[i][j] = self.grids[i][j]

    def neighbors(self, i, j):
        top = (i - 1 + self.dim) % self.dim
        bottom = (i + 1) % self.dim
        left = (j - 1 + self.dim) % self.dim
        right = (j + 1) % self.dim
        count = 0
        if self.grids[top][left] == 1:
            count += 1
        if self.grids[top][j] == 1:
            count += 1
        if self.grids[top][right] == 1:
            count += 1
        if self.grids[i][left] == 1:
            count += 1
        if self.grids[i][right] == 1:
            count += 1
        if self.grids[bottom][left] == 1:
            count += 1
        if self.grids[bottom][j] == 1:
            count += 1
        if self.grids[bottom][right] == 1:
            count += 1
        return count


    def run(self):
        for s in range(self.steps):
            print(s)
            self.apply_rules()
            self.grids = copy.deepcopy(self.buffer)
            self.print_grids()


if __name__ == '__main__':
    grids = [[0, 1, 0, 1, 0, 0, 0, 1, 0, 0],
             [1, 0, 1, 1, 1, 0, 0, 1, 0, 1],
             [1, 1, 0, 1, 0, 0, 0, 1, 1, 1],
             [1, 0, 1, 1, 0, 0, 1, 0, 0, 1],
             [0, 0, 0, 1, 1, 1, 0, 0, 1, 0],
             [1, 0, 0, 1, 1, 1, 1, 0, 0, 0],
             [1, 0, 1, 1, 1, 1, 0, 1, 0, 0],
             [0, 0, 0, 1, 1, 1, 1, 0, 1, 1],
             [1, 0, 0, 1, 0, 0, 1, 1, 1, 1],
             [0, 1, 0, 0, 0, 1, 0, 0, 1, 1]]
    lg = LifeGame(10, 100, grids)
    lg.run()
