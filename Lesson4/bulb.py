#importing library
import pygame
#initilize pygame
pygame.init()
#create screen
screen = pygame.display.set_mode((700,700))
screen.fill((255,255,255))
#Inital image is off
image=pygame.image.load("bulboff.png")
pygame.display.update()
#mouse down to ON(Click on screen)
# mouse up(release)to OFF
while True:
    event = pygame.event.poll()
    if event.type == pygame.MOUSEBUTTONDOWN:
        image=pygame.image.load("bulbon.png")
        screen.blit(image,(0,0))
        pygame.display.update()
    elif event.type == pygame.MOUSEBUTTONUP:
        image=pygame.image.load("bulboff.png")
        screen.blit(image,(0,0))
        pygame.display.update()