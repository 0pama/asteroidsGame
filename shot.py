import pygame
from circleshape import CircleShape
from constants import *

class Shot(CircleShape):
    def __init__(self, x, y):
        super().__init__(x,y,SHOT_RADIUS)
        self.image = pygame.image.load(f"assets/PNG/Sprites/Missiles/shot.png").convert_alpha()
        self.image = pygame.transform.scale(self.image, (self.radius * 2, self.radius * 2))

    def draw(self, screen):
        screen.blit(self.image,self.position - pygame.Vector2(self.radius, self.radius))

    
    def update(self,dt):
        self.position +=  self.velocity * dt
