import pgzrun
from random import randint
TITLE = "Flappy Ball"
WIDTH = 800
HEIGHT = 600


R = randint(0,255)
G = randint(0,255)
B = randint(0,255)
C = R,G,B

Grav = 2000.0

class ball:
    def __init__(self,initx,inity):
        self.x=initx
        self.y=inity
        self.vx = 200
        self.vy = 0
        self.radius = 40
    
    def draw(self):
        pos = (self.x,self.y)
        screen.draw.filled_circle(pos,self.radius,C)
        screen.draw.filled_circle(pos,self.radius,C)

ball1 = ball(50,100)
def draw():
    screen.clear()
    ball1.draw()

def update(dt):
    uy = ball1.vy
    ball1.vy += Grav*dt
    ball1.y += (uy + ball1.vy)*0.5*dt
    #that can handle the bounce.
    if ball1.y > HEIGHT-ball1.radius:
        ball1.y = HEIGHT-ball1.radius
        ball1.vy = -ball1.vy*0.9
    ball1.x += ball1.vx*dt
    if ball1.x > WIDTH-ball1.radius or ball1.x < ball1.radius:
        ball1.vx = -ball1.vx

def on_key_down(key):
    if key == keys.SPACE:
        ball1.vy = -500

pgzrun.go()