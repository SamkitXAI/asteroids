from circleshape import *
from constants import *
import pygame

class Shot(CircleShape):
    
    def __init__(self, x, y, SHOT_RADIUS, velocity):
        super().__init__(x, y, SHOT_RADIUS)
        self.velocity = velocity
        
    def draw(self, screen):
        pygame.draw.circle(screen, "white", self.position, self.radius, 2)
        
    def update(self, dt):
        self.position = self.position + self.velocity * dt 