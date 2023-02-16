import os
import sys
import pygame
from settings import Settings
from UFO import Projectile
from UFO import UFO 
pygame.init()
pygame.font.init()
pygame.mixer.init()

"""Project about a UFO shooter where you are the U.F.O. , remember this is just for fun!"""
BULLET = Projectile()
BULLET_VEL = BULLET.BULLET_VEL
red_bullets = BULLET.red_bullets
yellow_bullets = BULLET.yellow_bullets
SPACESHIP = UFO()
gameset = Settings()
YELLOW_SPACESHIP = SPACESHIP.YELLOW_SPACESHIP
RED_SPACESHIP = SPACESHIP.RED_SPACESHIP
YELLOW_HIT = SPACESHIP.YELLOW_HIT
RED_HIT = SPACESHIP.RED_HIT
HEALTH_FONT = gameset.HF
WINNER_FONT = gameset.WF
RH = SPACESHIP.RED_HEALTH
YH = SPACESHIP.YELLOW_HEALTH
WIN = pygame.display.set_mode((gameset.screen_width,
     gameset.screen_height))
pygame.display.set_caption("UFO Shooter")

def draw_window(red, yellow, red_bullets, yellow_bullets, RH, YH):
    WIN.blit(gameset.bg_screen, (0, 0)) # Fills backround color or pattern
    pygame.draw.rect(WIN, gameset.bg_color_blk, gameset.BORDER)
    
    red_health_text = HEALTH_FONT.render("HEALTH: " + str(SPACESHIP.RED_HEALTH), 1, gameset.bg_color)
    yellow_health_text = HEALTH_FONT.render("HEALTH " + str(SPACESHIP.YELLOW_HEALTH), 1, gameset.bg_color)
    WIN.blit(red_health_text, (gameset.screen_width - red_health_text.get_width() - 10, 10))
    WIN.blit(yellow_health_text, (10, 10))
    WIN.blit(YELLOW_SPACESHIP, (yellow.x, yellow.y))
    WIN.blit(RED_SPACESHIP, (red.x, red.y ))
    pygame.display.update() # updates the screen


    for bullet in red_bullets:
        pygame.draw.rect(WIN, gameset.color_red, bullet)
    
    for bullet in yellow_bullets:
        pygame.draw.rect(WIN, gameset.color_ylw, bullet)

    pygame.display.update() # updates screen

def yellow_handle_movement(keys_pressed, yellow):
    if keys_pressed[pygame.K_a] and yellow.x - gameset.VEL > 0: # LEFT and checks for border of screen, disallows access
        yellow.x -= gameset.VEL
    if keys_pressed[pygame.K_d] and yellow.x + gameset.VEL + SPACESHIP.WIDTH < gameset.BORDER.x: # RIGHT
        yellow.x += gameset.VEL
    if keys_pressed[pygame.K_w] and yellow.y - gameset.VEL > 0: # UP
        yellow.y -= gameset.VEL
    if keys_pressed[pygame.K_s] and yellow.y + gameset.VEL + SPACESHIP.HEIGHT < gameset.screen_height - 15: # DOWN
        yellow.y += gameset.VEL

def red_handle_movement(keys_pressed, red):
    if keys_pressed[pygame.K_LEFT] and red.x - gameset.VEL > gameset.BORDER.x + gameset.BORDER.width: # LEFT
        red.x -= gameset.VEL
    if keys_pressed[pygame.K_RIGHT] and red.x + gameset.VEL + SPACESHIP.WIDTH < gameset.screen_width: # RIGHT
        red.x += gameset.VEL
    if keys_pressed[pygame.K_UP] and red.y - gameset.VEL > 0: # UP
        red.y -= gameset.VEL
    if keys_pressed[pygame.K_DOWN] and red.y + gameset.VEL + SPACESHIP.HEIGHT < gameset.screen_height - 15: # DOWN
        red.y += gameset.VEL

def handle_bullets(yellow_bullets, red_bullets, yellow, red):
    for bullet in yellow_bullets:
        bullet.x += BULLET_VEL
        if red.colliderect(bullet): # Checking if yellow bullets hit red
            pygame.event.post(pygame.event.Event(RED_HIT))
            yellow_bullets.remove(bullet)
            print (len(yellow_bullets))
        elif bullet.x > gameset.screen_width:
            yellow_bullets.remove(bullet)
            print (len(yellow_bullets))
       

    
    for bullet in red_bullets:
        bullet.x -= BULLET_VEL
        if yellow.colliderect(bullet): # Checking if yellow bullets hit red
            pygame.event.post(pygame.event.Event(YELLOW_HIT))
            red_bullets.remove(bullet)
        elif bullet.x < 0:
            red_bullets.remove(bullet)
        
def draw_winner(text):
    draw_text = WINNER_FONT.render(text, 1, gameset.bg_color, None )
    WIN.blit(draw_text, (gameset.screen_width/2 - draw_text.get_width() / 2, gameset.screen_height/2 - draw_text.get_height()/2))
    pygame.display.update()
    pygame.time.delay(5000)


def start_engine():
    red = pygame.Rect(700, 300, SPACESHIP.WIDTH, SPACESHIP.HEIGHT)
    yellow = pygame.Rect(100, 300, SPACESHIP.WIDTH, SPACESHIP.HEIGHT)
    clock = pygame.time.Clock()
    run = True
    while run:
        clock.tick(gameset.FPS) # Calls FPS to set the tick to control frame rate
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                pygame.quit()
            
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE and len(yellow_bullets) < BULLET.max_payload:
                    bullet = pygame.Rect(
                        yellow.x + SPACESHIP.WIDTH, yellow.y + SPACESHIP.HEIGHT//2 - 2, 10, 5)
                    yellow_bullets.append(bullet)
                    BULLET.BULLET_FIRE_SOUND.play()


                if event.key == pygame.K_RCTRL and len(red_bullets) < BULLET.max_payload:
                    bullet = pygame.Rect(red.x ,red.y + SPACESHIP.HEIGHT//2 - 2, 10, 5)
                    red_bullets.append(bullet)
                    BULLET.BULLET_FIRE_SOUND.play()

            if event.type == RED_HIT:
                SPACESHIP.RED_HEALTH -= 1
                BULLET.BULLET_HIT_SOUND.play()


            if event.type == YELLOW_HIT:
                SPACESHIP.YELLOW_HEALTH -= 1
                BULLET.BULLET_HIT_SOUND.play()

        winner_text = ""
        if SPACESHIP.RED_HEALTH <= 0:
            winner_text = "Yellow Wins!"

        if SPACESHIP.YELLOW_HEALTH <= 0:
            winner_text = "Red Wins!"

        if winner_text != "":
            draw_winner(winner_text)
            break

        keys_pressed = pygame.key.get_pressed() 
        yellow_handle_movement(keys_pressed, yellow)
        red_handle_movement(keys_pressed, red)

        handle_bullets(yellow_bullets, red_bullets, yellow, red)

        draw_window(red, yellow, red_bullets, yellow_bullets,RH, YH)  


    



if __name__ == '__main__':
    start_engine()
 