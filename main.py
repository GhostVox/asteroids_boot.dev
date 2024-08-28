import pygame
import sys

from asteroidfield import AsteroidField
from constants import *    
from player import Player
from asteroid import Asteroid
from shot import Shot
def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH,SCREEN_HEIGHT  ))
    clock= pygame.time.Clock()
    
    asteroids = pygame.sprite.Group()
    updateable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    shots = pygame.sprite.Group()
    Player._containers = (updateable,drawable)
    Asteroid._containers = (updateable,drawable , asteroids)
    AsteroidField._containers = (updateable,)
    Shot._containers = (updateable , drawable ,shots) 

    player = Player(SCREEN_WIDTH/2 , SCREEN_HEIGHT/2)
    AsteroidField()
    dt = 0
    
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        for member in updateable:
            member.update(dt)

        for member in asteroids:
            if player.collides_with(member):
                print('Game over!')
                sys.exit()
            else:
                      pass  
        for asteroid in asteroids:
             for shot in shots:
                  if shot.collides_with(asteroid):
                        shot.kill()
                        asteroid.split()
            
        screen.fill(color="black" , rect=None)

        for member in drawable:
            member.draw(screen) 
             
        pygame.display.flip()

        # The line below limits the framerate to 60 Fps
        dt = clock.tick(60) /1000
if __name__ == "__main__":


     main()
