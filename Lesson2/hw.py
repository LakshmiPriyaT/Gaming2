import pgzrun
from random import randint

TITLE = 'Flappy Ball'
WIDTH = 800
HEIGHT = 600

R = randint(0,255)
G = randint(0,255)
B = randint(0,255)
CLR = R,G,B

#BLUE = 0, 128, 255
GRAVITY = 2000.0  # pixels per second per second


class Ball:
    
    def __init__(self, initial_x, initial_y):
        self.x = initial_x
        self.y = initial_y
        self.vx = 200
        self.vy = 0
        self.radius = randint(20,40)
        self.CLR =(randint(0,255),randint(0,255),randint(0,255))
    def draw(self):
        pos = (self.x, self.y)
        screen.draw.filled_circle(pos, self.radius, self.CLR)


ball1 = Ball(50, 100)
ball2 = Ball(500,10)

balls = [ball1,ball2]

def draw():
    screen.clear()
    ball1.draw()
    ball2.draw()


def update(dt):
    index = 1
    for ball in balls:
        
    # Apply constant acceleration formulae
        uy = ball.vy
        ball.vy += GRAVITY * dt
        ball.y += (uy + ball.vy) * 0.5 * dt

    # detect and handle bounce
        if ball.y > HEIGHT - ball.radius:  # we've bounced!
            ball.y = HEIGHT - ball.radius  # fix the position
            ball.vy = -ball.vy * (index * 0.9)  # inelastic collision

    # X component doesn't have acceleration
        ball.x += ball.vx * dt
        if ball.x > WIDTH - ball.radius or ball.x < ball.radius:
            ball.vx = -ball.vx
        index = index+0.5


def on_key_down(key):
    """Pressing a key will kick the ball upwards."""
    for ball in balls:
        if key == keys.SPACE:
            ball.vy = -500

pgzrun.go()