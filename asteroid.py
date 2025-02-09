import pygame
import random
from circleshape import CircleShape
from constants import *

class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)
        self.image = pygame.image.load(f"assets/PNG/Sprites/Meteors/big.png").convert_alpha()
        self.image = pygame.transform.scale(self.image, (radius * 2, radius * 2))
        self.is_exploding = False
        self.explosion_image = pygame.image.load("assets/collision.xcf").convert_alpha()
        self.explosion_image = pygame.transform.scale(self.explosion_image, (self.radius * 4, self.radius * 4))
        self.animation_time = 0.1  # Duration of the explosion animation
        self.explosion_timer = 0.0  

    def draw(self, screen):
        if self.is_exploding:
            screen.blit(self.explosion_image, self.position - pygame.Vector2(self.radius * 2, self.radius * 2))
        else:
            screen.blit(self.image, self.position - pygame.Vector2(self.radius, self.radius))

    def update(self, dt):
        if self.is_exploding:
            self.explosion_timer += dt
            if self.explosion_timer >= self.animation_time:
                self.kill()  # Kill the asteroid after the animation finishes
        else:
            
            self.position += self.velocity * dt

    def split(self):
        self.is_exploding = True
        self.explosion_timer = 0.0

        if self.radius <= ASTEROID_MIN_RADIUS:
            return

        blue_angle = random.uniform(20, 50)
        a = self.velocity.rotate(blue_angle)
        b = self.velocity.rotate(-blue_angle)

        new_radius = self.radius - ASTEROID_MIN_RADIUS
        asteroid1 = Asteroid(self.position.x, self.position.y, new_radius)
        asteroid1.velocity = a * 1.2

        asteroid2 = Asteroid(self.position.x, self.position.y, new_radius)
        asteroid2.velocity = b * 1.2