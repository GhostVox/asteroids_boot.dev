import pygame
from circleshape import CircleShape
from typing import Optional ,Tuple

class Asteroid (CircleShape):

    _containers:Optional[Tuple[pygame.sprite.Group, pygame.sprite.Group, pygame.sprite.Group]] = None
    def __init__(self , x, y, radius):
        super().__init__(x,y,radius)
        
        
        if Asteroid._containers is not None:
            for group in Asteroid._containers:
                group.add(self)

        return
    
    def draw(self , screen):
        pygame.draw.circle(screen , "white" ,self.position , self.radius , 2)

        return

    def update(self, dt):
        self.position += (self.velocity * dt)
        return
   
    
          
