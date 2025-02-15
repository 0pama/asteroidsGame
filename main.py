import pygame
import sys
from constants import *
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField
from shot import Shot

def main():
    pygame.init()
    

    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()

    # Load background
    
    background = pygame.image.load("assets/background.png").convert()
    background = pygame.transform.scale(background, (SCREEN_WIDTH, SCREEN_HEIGHT))

    # score init
    score = 0 

    updatable = pygame.sprite.Group()
    shots = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()

    Asteroid.containers = (asteroids, updatable, drawable)
    AsteroidField.containers = updatable
    Shot.containers = (shots, updatable, drawable)
    Player.containers = (updatable, drawable)


    asteroid_field = AsteroidField()
    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)

    dt = 0

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

        
        updatable.update(dt)


        for obj in asteroids:
            if obj.colliding(player):
                print("Game over!")
                sys.exit()
            for shot in shots:
                if obj.colliding(shot):
                    obj.split()
                    shot.kill()
                    score+= 10
                    

        screen.blit(background, (0, 0))
        

        for obj in drawable:
            obj.draw(screen)


        # Display the score
        font = pygame.font.Font(None, 40)  
        score_text = font.render(f"Score: {score}", True, "white")
        screen.blit(score_text, (10, 10))  
        pygame.display.flip()

        # limiting the framerate to 60 FPS
        dt = clock.tick(60) / 1000


if __name__ == "__main__":
    main()
