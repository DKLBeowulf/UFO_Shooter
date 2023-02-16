import os
import pygame
pygame.init()
pygame.font.init()
pygame.mixer.init()
class UFO():
    def __init__(self):
        self.WIDTH = 55
        self.HEIGHT = 47
        self.YELLOW_SPACESHIP_IMAGE = pygame.image.load(os.path.join
            ('Assets', 'spaceship_yellow.png'))
        self.RED_SPACESHIP_IMAGE = pygame.image.load(os.path.join
            ('Assets', 'spaceship_red.png'))
        self.YELLOW_SPACESHIP = pygame.transform.rotate(pygame.transform.scale(self.YELLOW_SPACESHIP_IMAGE, (self.WIDTH, self.HEIGHT)), 90)
        self.RED_SPACESHIP = pygame.transform.rotate(pygame.transform.scale(self.RED_SPACESHIP_IMAGE, (self.WIDTH, self.HEIGHT)), 270)
        self.YELLOW_HIT = pygame.USEREVENT + 1 # Create an event an assign it 1
        self.RED_HIT =  pygame.USEREVENT + 2 # Create an event and assign it 2
        self.RED_HEALTH = 10
        self.YELLOW_HEALTH = 10

class Projectile():
    def __init__(self):
        self.red_bullets = []
        self.yellow_bullets = []
        self.BULLET_VEL = 7
        self.max_payload = 3
        self.BULLET_HIT_SOUND = pygame.mixer.Sound(os.path.join('Assets', 'Assets_Grenade+1.mp3'))
        self.BULLET_FIRE_SOUND = pygame.mixer.Sound(
            os.path.join('Assets', 'Assets_Gun+Silencer.mp3'))

    
