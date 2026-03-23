import math

from model import Exoskeleton

def set_link1_angle(obj: Exoskeleton, angle: float):
    obj.update(joint1=obj.theta1 - angle)
    obj.update(joint2=obj.theta2 - angle)

def set_link2_angle(obj: Exoskeleton, angle: float):
    obj.update(joint2=obj.theta2 - angle)

def get_link1_angle(obj: Exoskeleton):
    return obj.theta1

def get_link2_angle(obj: Exoskeleton):
    return obj.theta2

def detect_collisions(obj: Exoskeleton, scene: list):
    for obstacle in scene:
        if obstacle.contains(obj.get_position()):
            return True
    return False

def resolve_collision(obj: Exoskeleton, scene, old_pos, curr_pos):
    p1, p2 = old_pos, curr_pos

    while detect_collisions(obj, scene):
        angle1 = math.ceil((p2[0] - p1[0]) / 2)
        angle2 = math.ceil((p2[1] - p1[1]) / 2)

        set_link1_angle(obj, angle1)
        set_link2_angle(obj, angle2)

        p2 = get_link1_angle(obj), get_link2_angle(obj)

