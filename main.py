# this allows us to use code from
# the open-source pygame library
# throughout this file
import pygame
from player import *
from constants import *
from asteroid import *
from asteroidfield import *

def main():
    pygame.init()
    print("Starting asteroids!")
    
    clock_fps = pygame.time.Clock()
    dt = 0
    
    updatable = pygame.sprite.Group()  # Group A
    drawable = pygame.sprite.Group()  # Group B
    asteroids = pygame.sprite.Group() # Group for asteroids
    shots = pygame.sprite.Group()     # Group for shots
    
    Player.containers = (updatable, drawable)
    Asteroid.containers = (asteroids, updatable, drawable)
    AsteroidField.containers = (updatable)
    shots.containers = (shots, updatable, drawable)
    
    # Set up the screen with defined width and height
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    
    # Create a Player object at the center of the screen
    x = SCREEN_WIDTH / 2
    y = SCREEN_HEIGHT / 2
    player = Player(x, y)
    game_field = AsteroidField()
    

    while True:
        screen.fill((0, 0, 0))
        for entity in drawable:
            entity.draw(screen)
        for entity in updatable:
            entity.update(dt)
            
            
        
        for asteroid in asteroids:
            if player.is_colliding(asteroid):
                # print("Game over!")
                pygame.quit()
                exit("Game over!")
                
            for shot in shots:
                if shot.is_colliding(asteroid):
                    asteroid.kill()
                    shot.kill()
        
        pygame.display.flip()
        
        
        dt = clock_fps.tick(60)/1000
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
    
    


if __name__ == "__main__":
    main()