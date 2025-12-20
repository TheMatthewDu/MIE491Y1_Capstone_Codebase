import pygame
from model import Exoskeleton, Obstacle

from apis import mainloop

def main():
    pygame.init()
    WIDTH, HEIGHT = 800, 600
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("Exoskeloten Model")
    ORIGIN = (WIDTH // 2, HEIGHT // 4)
    
    robot = Exoskeleton(origin=ORIGIN)
    obstacle = Obstacle(origin=ORIGIN, x=200, y=300, r=100)

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        mainloop(robot, [obstacle])

        screen.fill((0, 0, 0))
        robot.draw(screen)
        obstacle.draw(screen)
        pygame.display.flip()
        pygame.time.wait(10)

    pygame.quit()


if __name__ == "__main__":
    main()