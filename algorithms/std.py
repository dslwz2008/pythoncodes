#-*-coding:utf-8-*-
__author__ = 'shenshen'

import random
import math
import pygame
from math import pi

#
class StdRandom(object):
    """Random"""
    @classmethod
    def initialize(cls, seed):
        """initialize"""
        random.seed(seed)

    @classmethod
    def random(cls):
        """return float number between 0 and 1"""
        return random.random()

    @classmethod
    def uniform(cls, n):
        """return the int between 0 and n"""
        return random.randint(0, n)

    @classmethod
    def uniform(cls, lo, hi):
        """return the number between lo and hi"""
        return random.uniform(lo, hi)

    @classmethod
    def bernoulli(cls, p):
        """return True at the probability of p"""
        return StdRandom.random() < p

    @classmethod
    def gaussian(cls):
        pass

    @classmethod
    def discrete(cls, alist):
        pass

    @classmethod
    def shuffle(cls, alist):
        """随机打乱一个数组"""
        return random.shuffle(alist)


class StdStats(object):
    @classmethod
    def max(cls, alist):
        return max(alist)

    @classmethod
    def min(cls, alist):
        return min(alist)

    @classmethod
    def mean(cls, alist):
        if len(alist) == 0:
            return None
        return float(sum(alist)) / len(alist)

    @classmethod
    def variance(cls, data):
        if len(data) == 0:
            return None
        mu = StdStats.mean(data)
        return StdStats.mean([(x - mu) ** 2 for x in data])

    @classmethod
    def sample_variance(cls, data):
        if len(data) == 0:
            return None
        sum = 0.0
        avg = StdStats.mean(data)
        for n in data:
            sum = sum + (n - avg) * (n - avg)
        return sum / (len(data) - 1)

    @classmethod
    def stddev(cls, data):
        return math.sqrt(float(StdStats.variance(data)))

    @classmethod
    def median(cls, data):
        data.sort()
        result = 0
        if len(data) % 2 == 0:
            result = (data[len(data)/2] + data[len(data)/2-1]) / 2
        else:
            result = data[len(data)/2]
        return result

    @classmethod
    def mode(cls, data):
        maxcount = 0
        maxelem = data[0]
        for item in data:
            icount = data.count(item)
            if icount > maxcount:
                maxcount = icount
                maxelem = item
        return maxelem



# Define the colors we will use in RGB format
BLACK = (  0,   0,   0)
WHITE = (255, 255, 255)
BLUE =  (  0,   0, 255)
GREEN = (  0, 255,   0)
RED =   (255,   0,   0)

class ElementType(object):
    POINT,LINE,CIRCLE,ELLIPSE,\
        RECTANGLE,POLYGON = range(6)

class Point(object):
    def __init__(self, x, y, color, width):
        self.x = x
        self.y = y
        self.color = color
        self.width = width

class Line(object):
    def __init__(self, start, end, color, width):
        self.start = start
        self.end = end
        self.color = color
        self.width = width

class Circle(object):
    def __init__(self, pos, radius, color, width):
        self.pos = pos
        self.radius = radius
        self.color = color
        self.width = width

class StdDraw(object):
    def __init__(self):
        self.screen_color = WHITE
        self.screen_size = [400, 300]
        self.caption = "Example code for the draw module"
        self.render_list = []

    def point(self, x, y, color=WHITE):
        point = []
        point.append(ElementType.POINT)
        point.append(x)
        point.append(y)

    def draw(self):
        # Initialize the game engine
        pygame.init()

        # Set the height and width of the screen
        size = self.screen_size
        screen = pygame.display.set_mode(size)

        pygame.display.set_caption(self.caption)

        #Loop until the user clicks the close button.
        done = False
        clock = pygame.time.Clock()

        while not done:

            # This limits the while loop to a max of 10 times per second.
            # Leave this out and we will use all CPU we can.
            clock.tick(10)

            for event in pygame.event.get(): # User did something
                if event.type == pygame.QUIT: # If user clicked close
                    done=True # Flag that we are done so we exit this loop

            # All drawing code happens after the for loop and but
            # inside the main while done==False loop.

            # Clear the screen and set the screen background
            screen.fill(self.screen_color)

            # # Draw on the screen a GREEN line from (0,0) to (50.75)
            # # 5 pixels wide.
            # pygame.draw.line(screen, GREEN, [0, 0], [50,30], 5)
            #
            # # Draw on the screen a GREEN line from (0,0) to (50.75)
            # # 5 pixels wide.
            # pygame.draw.lines(screen, BLACK, False, [[0, 80], [50, 90], [200, 80], [220, 30]], 5)
            #
            # # Draw on the screen a GREEN line from (0,0) to (50.75)
            # # 5 pixels wide.
            # pygame.draw.aaline(screen, GREEN, [0, 50],[50, 80], True)
            #
            # # Draw a rectangle outline
            # pygame.draw.rect(screen, BLACK, [75, 10, 50, 20], 2)
            #
            # # Draw a solid rectangle
            # pygame.draw.rect(screen, BLACK, [150, 10, 50, 20])
            #
            # # Draw an ellipse outline, using a rectangle as the outside boundaries
            # pygame.draw.ellipse(screen, RED, [225, 10, 50, 20], 2)
            #
            # # Draw an solid ellipse, using a rectangle as the outside boundaries
            # pygame.draw.ellipse(screen, RED, [300, 10, 50, 20])
            #
            # # This draws a triangle using the polygon command
            # pygame.draw.polygon(screen, BLACK, [[100, 100], [0, 200], [200, 200]], 5)
            #
            # # Draw an arc as part of an ellipse.
            # # Use radians to determine what angle to draw.
            # pygame.draw.arc(screen, BLACK,[210, 75, 150, 125], 0, pi/2, 2)
            # pygame.draw.arc(screen, GREEN,[210, 75, 150, 125], pi/2, pi, 2)
            # pygame.draw.arc(screen, BLUE, [210, 75, 150, 125], pi,3*pi/2, 2)
            # pygame.draw.arc(screen, RED,  [210, 75, 150, 125], 3*pi/2, 2*pi, 2)
            #
            # # Draw a circle
            # pygame.draw.circle(screen, BLUE, [60, 250], 40)

            # Go ahead and update the screen with what we've drawn.
            # This MUST happen after all the other drawing commands.
            pygame.display.flip()

        # Be IDLE friendly
        pygame.quit()


if __name__ == '__main__':
    # draw = StdDraw()
    # draw.color = RED
    # draw.draw()
    a = [9,18,9,9]
    print StdStats.mean(a)
    print StdStats.variance(a)
    print StdStats.mode(a)

