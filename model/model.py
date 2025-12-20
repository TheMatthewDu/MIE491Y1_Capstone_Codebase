import pygame
import math


class Exoskeleton:
    def __init__(self, origin, l1=200, l2=200):
        self.origin = origin

        # Lengths
        self.l1 = l1
        self.l2 = l2

        # Angles
        self.theta1 = 0
        self.theta2 = 0

    def update(self, joint1: float=None, joint2: float=None):
        if joint1 is not None:
            self.theta1 = joint1

        if joint2 is not None:
            self.theta2 = joint2

    def get_position(self):
        ox, oy = self.origin
        x1 = ox + self.l1 * math.sin(math.radians(self.theta1)) + self.l2 * math.sin(math.radians(self.theta2))
        y1 = oy + self.l1 * math.cos(math.radians(self.theta1)) + self.l2 * math.cos(math.radians(self.theta2))

        return x1, y1

    def draw(self, screen):
        ox, oy = self.origin

        x1 = ox + self.l1 * math.sin(math.radians(self.theta1))
        y1 = oy + self.l1 * math.cos(math.radians(self.theta1))

        x2 = x1 + self.l2 * math.sin(math.radians(self.theta2))
        y2 = y1 + self.l2 * math.cos(math.radians(self.theta2))

        # Draw pendulum arms
        pygame.draw.line(screen, (255, 255, 255), (ox, oy), (x1, y1), 5)
        pygame.draw.line(screen, (255, 255, 255), (x1, y1), (x2, y2), 5)


class Obstacle:
    def __init__(self, origin, x, y, r):
        self.origin = origin

        self.x = self.origin[0] + x
        self.y = self.origin[1] + y
        self.radius = r

    def contains(self, pt: (float, float)) -> bool:
        return (pt[0] - self.x) ** 2 + (pt[1] - self.y) ** 2 <= self.radius ** 2

    def draw(self, screen):
        pygame.draw.circle(screen, (0, 255, 0), (self.x, self.y), self.radius, 0)

