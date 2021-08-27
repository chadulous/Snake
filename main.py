from ursina import *
from time import sleep as wait
from random import randint
from sys import argv
highscore = int(open('score.dat', 'r').read())
class Player(Entity):
    def __init__(self, pfield):
        super().__init__()
        self.parent = pfield
        self.model = 'cube'
        self.color = rgb(100, 186, 74)
        self.scale = .05
        self.position = (0,0,-.03)
        self.collider = 'box'
        self.dx = 0
        self.dy = 0
        self.eaten = 0
    def update(self):
        global body
        global highscore
        self.x+=time.dt * self.dx
        self.y+=time.dt * self.dy
        hit_info=self.intersects()
        print_on_screen(f'Score: {self.eaten}\nHigh Score: {highscore}', duration=.01)
        if hit_info.hit:
            apple.x = randint(-4,4)*.1
            apple.y = randint(-4,4)*.1
            new_body = Entity(parent=self.parent, model='cube', z=-.029, color=self.color, scale=.05)
            body.append(new_body)
            self.eaten += 1
        if self.eaten >  highscore:
            highscore = self.eaten
            open('score.dat', 'w').write(f'{highscore}')
        for i in range(len(body)-1,0,-1):
            body[i].position = body[i-1].position
        if len(body)>0:
            body[0].x=self.x
            body[0].y=self.y
        if abs(self.x)>.47 or abs(self.y)>.47:
            for segment in body:
                segment.position=(10,10)
            body=[]
            print_on_screen('You Died', position=(0,0), origin=(0,0), scale=2, duration=2)
            self.position = (0,0)
            self.dx=0
            self.dy=0
            self.eaten = 0
            apple.x = randint(-4,4)*.1
            apple.y = randint(-4,4)*.1
    def input(self,key):
        if key=='right arrow' or key=='d':
            self.dx=.3
            self.dy=0
        if key=='left arrow' or key=='a':
            self.dx=-.3
            self.dy=0
        if key=='up arrow' or key=='w':
            self.dx=0
            self.dy=.3
        if key=='down arrow' or key=='s':
            self.dx=0
            self.dy=-.3
app=Ursina()
Entity(model='quad', scale=60, texture='sky_sunset')
field_size=25
camera.position=(field_size//2, -18, -18)
camera.rotation_x = -56
field=Entity(model='quad', color=color.green, scale=(12,12), position=(field_size//2, field_size//2, -.01), texture='grass')
apple=Entity(parent=field, model='sphere', color=color.red, scale=.05, position=(.1,.1,-.03), collider='box')
player=Player(field)
body=[]
try:
    import pyi_splash
    for i in range(0,5):
        pyi_splash.update_text(f'Loading Stuff, {i}s..')
        wait(1)
    pyi_splash.close()
except:
    print('running on .py, splash screen not allowed')
app.run()