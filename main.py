# this allows us to use code from
# the open-source pygame library
# throughout this file
import pygame
from player import *
from constants import *

def main():
    pygame.init()
    print("Starting asteroids!")
    
    clock_fps = pygame.time.Clock()
    dt = 0
    
    updatable = pygame.sprite.Group()  # Group A
    drawable = pygame.sprite.Group()  # Group B
    
    Player.containers = (updatable, drawable)

    # Set up the screen with defined width and height
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    
    # Create a Player object at the center of the screen
    x = SCREEN_WIDTH / 2
    y = SCREEN_HEIGHT / 2
    player = Player(x, y)
    
    

    while True:
        screen.fill((0, 0, 0))
        for entity in drawable:
            entity.draw(screen)
        for entity in updatable:
            entity.update(dt)
            
        pygame.display.flip()
        
        
        dt = clock_fps.tick(60)/1000
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
    
    
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")


if __name__ == "__main__":
    main()