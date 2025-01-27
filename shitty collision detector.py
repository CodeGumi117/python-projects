import os
import pygame
import time
pygame.init()

width, height = 800, 400
screen = pygame.display.set_mode((width, height))

plr = pygame.Rect(400, 200, 40, 40)  
red = (255, 0, 0)
black = (0, 0, 0)
font = pygame.font.Font(None, 40)

col = 0
run = True
while run:
    screen.fill(black)  
    pygame.draw.rect(screen, red, plr)  

    text = font.render(f"Collisions detected: {col}", True, (0, 255, 0))
    key = pygame.key.get_pressed()

    if key[pygame.K_a] and plr.x > 0:
        plr.x -= 1  
    elif key[pygame.K_d] and plr.x < width - plr.width:
        plr.x += 1  


    if plr.x == 0:
        col += 1
       
    elif plr.x == width - plr.width:
        col += 1
        
    screen.blit(text, (400, 10))  

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    pygame.display.update() 

pygame.quit()
