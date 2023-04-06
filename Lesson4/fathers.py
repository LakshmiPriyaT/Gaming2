#importing the pygame and time libraries 
import pygame
import time

#initalize the pygame module 
pygame.init()
#display.set_mode((600,600)) is used to create a display window with 600px height and 600px width
screen=pygame.display.set_mode((600,600))
# Below code upto tim.sleep(2) for image 1 and nickname 1......
#loading the local image 1 to screen
image=pygame.image.load("FD.jpg")
screen.fill((255,255,255))
#place the image at (0,0) 
screen.blit(image,(0,0))
pygame.display.update()
time.sleep(2)
#image 2
image=pygame.image.load("fathers_day.jpg")
#load the font and write text with that font...
font=pygame.font.SysFont("sans script",50)
text=font.render("To My Hero",True,(0,0,0))
#fill the screen with color
screen.fill((255,255,255))
#place the image at (0,0) 
screen.blit(image,(0,0))
#place the text at (250,550)
screen.blit(text,(250,550))
#pygame.display.update() is to refelct the changes to be appear on screen 
pygame.display.update()
#sleep for 2 milli seconds 
time.sleep(2)
#you can use different fonts with different sizes
font=pygame.font.SysFont("Times New Roman",36)
text=font.render("Some people don't believe in heroes..",True,(0, 0, 255))
text1=font.render("but they haven't met my dad...",True,(0, 0, 255))
screen.fill((255,255,255))
screen.blit(text,(0,10))
screen.blit(text1,(150,50))
pygame.display.update()
time.sleep(2)
#Below code for image 3 with nickname 3...........
image=pygame.image.load("fathers_day2.png")
font=pygame.font.SysFont("Times New Roman",36)
text=font.render("Love U Dad",True,(0,225,0))
screen.fill((255,255,255))
screen.blit(image,(0,0))
screen.blit(text,(250,0))
pygame.display.update()
time.sleep(2)
#Below code for image 4 with nickname 4...........
image=pygame.image.load("fathers_day3.jpg")
font=pygame.font.SysFont("Times New Roman",36)
text=font.render("Infinity Times..",True,(0,0,0))
screen.fill((255,255,255))
screen.blit(image,(0,0))
screen.blit(text,(250,550))
pygame.display.update()
time.sleep(2)

#like you can create any number of images............