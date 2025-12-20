import pygame
import signal
from model import Exoskeleton


def joint1_rotate_ccw(obj: Exoskeleton, angle: float):
    obj.update(joint1=obj.theta1 + angle)

def joint2_rotate_ccw(obj: Exoskeleton, angle: float):
    obj.update(joint2=obj.theta2 + angle)

def joint1_rotate_cw(obj: Exoskeleton, angle: float):
    obj.update(joint1=obj.theta1 - angle)

def joint2_rotate_cw(obj: Exoskeleton, angle: float):
    obj.update(joint2=obj.theta2 - angle)

def detect_collisions(obj: Exoskeleton, scene: list):
    for obstacle in scene:
        if obstacle.contains(obj.get_position()):
            return True
    return False

def mainloop(obj: Exoskeleton, objects: list):
    if detect_collisions(obj, objects):
        return
    joint1_rotate_cw(obj, 1)
    joint2_rotate_cw(obj, 2)
