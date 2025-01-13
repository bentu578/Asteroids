
import sys
import pygame
from constants import *
from player import Player
from asteroid import Asteroid
from astroidfield import AsteroidField
from shot import Shot



def main():
    pygame.init()
    clock = pygame.time.Clock()
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    astroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()

    Shot.containers = (shots, updatable, drawable)
    Player.containers = (updatable, drawable)
    Asteroid.containers = (astroids, updatable, drawable)
    AsteroidField.containers = updatable
    astroid_field = AsteroidField()

    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
    


    dt = 0
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    
    

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        
        for obj in updatable:
            obj.update(dt)

        screen.fill("black")
        
        for obj in drawable:
            obj.draw(screen)


        pygame.display.flip()
        
        
        
        dt = clock.tick(60) / 1000
        for astroid in astroids:
            if astroid.collides_with(player):
                print("Game over!")
                sys.exit()
            for shot in shots:
                if astroid.collides_with(shot):
                    shot.kill()
                    astroid.split()


    
if __name__ == "__main__":
    main()