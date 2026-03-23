import pygame
from model import Exoskeleton, Obstacle

from apis import *

WIDTH, HEIGHT = 800, 600
ORIGIN = (WIDTH // 2, HEIGHT // 4)


def main():
    pygame.init()
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("Exoskeloten Model")
    
    robot = Exoskeleton(origin=ORIGIN)
    obstacle = Obstacle(origin=ORIGIN, x=200, y=300, r=100)

    prev = None
    keydown, direction = False, None
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.KEYDOWN:
                keydown = True
                if event.key == pygame.K_RIGHT:
                    direction = "R"
                elif event.key == pygame.K_LEFT:
                    direction = "L"
                elif event.key == pygame.K_UP:
                    direction = "U"
                elif event.key == pygame.K_DOWN:
                    direction = "D"
            elif event.type == pygame.KEYUP:
                keydown = False
                direction = None

        prev = get_link1_angle(robot), get_link2_angle(robot)
        if keydown:
            if direction == "R":
                set_link1_angle(robot, -1)
            elif direction == "L":
                set_link1_angle(robot, 1)
            elif direction == "U":
                set_link2_angle(robot, -1)
            elif direction == "D":
                set_link2_angle(robot, 1)

        if detect_collisions(robot, [obstacle]):
            curr = get_link1_angle(robot), get_link2_angle(robot)
            resolve_collision(robot, [obstacle], prev, curr)

        screen.fill((0, 0, 0))
        robot.draw(screen)
        obstacle.draw(screen)
        pygame.display.flip()
        pygame.time.wait(10)

    pygame.quit()


if __name__ == "__main__":
    main()