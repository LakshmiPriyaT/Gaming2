import pygame,random
pygame.init()
screen= pygame.display.set_mode((600,600))
screen.fill((255,255,255))
pygame.display.update()
poly=pygame.image.load("download.png")
screen.blit(poly,(150,100))
font=pygame.font.SysFont("Times New Roman",36)
text=font.render("click to change color of the Polygon",True,(0,0,0))
screen.blit(text,(30,50))
blue = (0,0,255)
red = (255,0,0)
green = (0,255,0)

pygame.display.update()
class polygon():
    def __init__(self,color,pos):
        self.color = color
        self.pos = pos
        self.surface = screen
        
    def draw(self):
        self.Draw_poly = pygame.draw.polygon(self.surface,self.color,self.pos)

    
 
def drawp(color):
  points = ((100,100),(150,300),(50,300))
  tri = polygon(color,points)
  tri.draw()
  points =((100,350),(300,350),(300,450),(100,450))
  sq = polygon(color,points)
  sq.draw()
  pygame.display.update()
#circle=Circle(blue,(300,300),25,0)

drawp(blue)
pygame.display.update()
while 1:
    event = pygame.event.poll()
    
    
    if event.type == pygame.MOUSEBUTTONUP:
      r = random.randint(0,255)
      g = random.randint(0,255)
      b = random.randint(0,255)
      color=(r,g,b)
      drawp(color)
      pygame. display.update()
    