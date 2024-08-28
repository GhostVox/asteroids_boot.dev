import pygame
from constants import *
from circleshape import CircleShape
from shot import Shot
from typing import Optional , Tuple
class Player(CircleShape):
    
    _containers:Optional[Tuple[pygame.sprite.Group, pygame.sprite.Group]] = None
   
    def __init__(self , x, y):
        super().__init__(x,y,PLAYER_RADIUS)
        self.rotation = 0
        self.radius = PLAYER_RADIUS
        self.shoot_timer = 0
        if Player._containers is not None:
            for group in Player._containers:
                group.add(self)

     
    # in the player class
    def triangle(self):
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        right = pygame.Vector2(0, 1).rotate(self.rotation + 90) * self.radius / 1.5
        a = self.position + forward * self.radius
        b = self.position - forward * self.radius - right
        c = self.position - forward * self.radius + right
        return [a, b, c]

    def draw(self, screen):
        pygame.draw.polygon(screen,"white",self.triangle(),2)
    
    def rotate (self,dt):
        self.rotation += PLAYER_TURN_SPEED * dt

    def update(self, dt):
        self.shoot_timer -= dt
        keys = pygame.key.get_pressed()

        if keys[pygame.K_a]:
            self.rotate(-dt)
        if keys[pygame.K_d]:
            self.rotate(dt)
        if keys[pygame.K_s]:
            self.move(-dt)
        if keys[pygame.K_w]:
            self.move(dt)
        if keys[pygame.K_SPACE]:
            self.shoot(dt)
        return
  
    def move(self, dt):

        foward = pygame.Vector2(0,1).rotate(self.rotation)
        self.position += foward * PLAYER_SPEED * dt
        return
    
    def shoot(self,dt):
        if self.shoot_timer > 0:
            return
        self.shoot_timer = PLAYER_SHOOT_COOLDOWN
        shot = Shot(self.position.x, self.position.y, 2)
        shot.velocity = pygame.Vector2(0, 1).rotate(self.rotation) * PLAYER_SHOOT_SPEED
    

