import pygame
import os
pygame.init()
pygame.font.init()
class Settings():

    def __init__(self):
        # Screen size and backround color
        self.screen_width = 1000
        self.screen_height = 800
        self.bg_color = (255, 255, 255)
        self.bg_color_blk = (0, 0, 0)
        self.color_red =  (255, 0, 0)
        self.color_ylw = (255, 255, 0)
        self.FPS = 60
        self.VEL = 5
        self.BORDER = pygame.Rect(self.screen_width//2 - 5, 0, 10, self.screen_height)
        self.bg_screen = pygame.transform.scale(pygame.image.load(os.path.join('Assets', 'space.png')), (self.screen_width, self.screen_height))
        self.HF = pygame.font.SysFont('comicsans', 40)
        self.WF = pygame.font.SysFont('comicsans', 100) 