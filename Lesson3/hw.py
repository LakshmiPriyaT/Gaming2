import pygame
pygame.init()
#global variables
screen = pygame.display.set_mode([500,500])
red = (255,0,0)
green = (0,255,0)
blue = (0,0,255)
white=(255,255,255)
yellow = (255,255,0)
black=(0,0,0)

screen.fill(white)

class myRect():
    def __init__(self,color, x,y, w,h):
        self.color = color
        self.dimensions = (x,y,w,h)
        self.w = w
        self.h = h
        self.x = x
        self.y = y
        self.scrn = screen
        
    def draw(self):
        pygame.draw.rect(self.scrn, self.color, self.dimensions )

    def grow(self,wid,hgt):
        self.w += wid
        self.h += hgt
        self.dimensions = (self.x,self.y,self.w,self.h)
        pygame.draw.rect(self.scrn, self.color, self.dimensions)
"""        
#how to draw a circle
position = (300,300)
radius = 50
wid = 2
pygame.draw.circle(screen, red, position, radius, wid )
pygame.display.update()
"""

#creating instances
bluerect = myRect(blue,100,20,100,40)




while(1):
    for event in pygame.event.get():
        if (event.type == pygame.MOUSEBUTTONDOWN):
            bluerect.draw()
            
            pygame.display.update()
        elif (event.type == pygame.MOUSEBUTTONUP):
            bluerect.grow(5,5)
            pygame.display.update()
        elif (event.type == pygame.MOUSEMOTION):
            pos = pygame.mouse.get_pos()
            blackrect = myRect(black,pos[0],pos[1],10,15)
            blackrect.draw()
            pygame.display.update()
            