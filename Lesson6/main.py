import pygame
import os

WIDTH = 900
HEIGHT = 500
#screen
WIN = pygame.display.set_mode((WIDTH,HEIGHT))
#caption header
pygame.display.set_caption("SATELLITE GAME")

WHITE = (255,255,255)
BLACK = (0,0,0)
BORDER = pygame.Rect(WIDTH//2 - 5, 0, 10, HEIGHT)

FPS = 60
VEL = 5
SPACE_WIDTH = 55
SPACE_HEIGHT = 40

yellow_space_img = pygame.image.load(os.path.join("Assets","spaceship_yellow.png"))
yellow_space = pygame.transform.rotate(pygame.transform.scale(yellow_space_img,(SPACE_WIDTH,SPACE_HEIGHT)),90)
red_space_img = pygame.image.load(os.path.join("Assets","spaceship_red.png"))
red_space = pygame.transform.rotate(pygame.transform.scale(red_space_img,(SPACE_WIDTH,SPACE_HEIGHT)),270)

def draw(red,yellow):
    #bg color
    WIN.fill(WHITE)
    #draw border
    pygame.draw.rect(WIN,BLACK,BORDER)
    #draw the image on the window
    WIN.blit(yellow_space,(yellow.x,yellow.y))
    WIN.blit(red_space,(red.x,red.y))
    #update things
    pygame.display.update()

def yellow_movement(keys_pressed,yellow):
    if keys_pressed[pygame.K_a] and yellow.x - VEL > 0: #left
        yellow.x -= VEL
    if keys_pressed[pygame.K_d] and yellow.x + VEL + yellow.width < BORDER.x : #right
        yellow.x += VEL
    if keys_pressed[pygame.K_w] and yellow.y - VEL > 0: #up
        yellow.y -= VEL
    if keys_pressed[pygame.K_s] and yellow.y + VEL + yellow.height < HEIGHT - 15 : #down
        yellow.y += VEL
def red_movement(keys_pressed,red):
    if keys_pressed[pygame.K_LEFT] and red.x - VEL > BORDER.x + BORDER.width:  # LEFT
        red.x -= VEL
    if keys_pressed[pygame.K_RIGHT] and red.x + VEL + red.width < WIDTH:  # RIGHT
        red.x += VEL
    if keys_pressed[pygame.K_UP] and red.y - VEL > 0:  # UP
        red.y -= VEL
    if keys_pressed[pygame.K_DOWN] and red.y + VEL + red.height < HEIGHT - 15:  # DOWN
        red.y += VEL
def main():
    red = pygame.Rect(700,300,SPACE_WIDTH,SPACE_HEIGHT)
    yellow = pygame.Rect(100,300,SPACE_WIDTH,SPACE_HEIGHT)

    clock = pygame.time.Clock()
    run = True
    while run:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
        keys_pressed = pygame.key.get_pressed()
        yellow_movement(keys_pressed, yellow)
        red_movement(keys_pressed, red)
        draw(red,yellow)
    pygame.quit()


if __name__ == "__main__":
    main()
