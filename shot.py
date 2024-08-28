import pygame
from circleshape import CircleShape
from typing import Optional ,Tuple

class Shot (CircleShape):
    _containers :Optional[Tuple[pygame.sprite.Group]]
    def __init__(self,x,y,radius):
        super().__init__(x , y , radius)

        if Shot._containers is not None:
                for group in Shot._containers:
                    group.add(self)
                return

    def draw(self , screen):
        pygame.draw.circle(screen ,'white',self.position,self.radius,)
    
        return

    def update(self,dt):
        self.position += (self.velocity* dt)
        return

