# -*-coding:utf-8-*-
# Author: Shen Shen
# Email: dslwz2002@163.com
import pygame
import random
import math

background_colour = (255, 255, 255)
(width, height) = (800, 600)


class Particle:
    def __init__(self, (x, y), size):
        self.x = x
        self.y = y
        self.size = size
        self.colour = (0, 0, 255)
        self.thickness = 1
        self.speed = 0
        self.angle = 0

    def display(self):
        pygame.draw.circle(screen, self.colour, (int(self.x), int(self.y)), self.size, self.thickness)

    def move(self):
        self.x += math.sin(self.angle) * self.speed
        self.y -= math.cos(self.angle) * self.speed


screen = pygame.display.set_mode((width, height))
pygame.display.set_caption('Tutorial 4')

number_of_particles = 10
my_particles = []

for n in range(number_of_particles):
    size = random.randint(10, 20)
    px = random.randint(size, width - size)
    py = random.randint(size, height - size)

    particle = Particle((px, py), size)
    particle.speed = random.random()
    particle.angle = random.uniform(0, math.pi * 2)

    my_particles.append(particle)

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill(background_colour)

    for particle in my_particles:
        particle.move()
        particle.display()
    pygame.display.flip()

pygame.quit()
