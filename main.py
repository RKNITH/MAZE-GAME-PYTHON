from ursina import *
from ursina.prefabs.first_person_controller import FirstPersonController

app = Ursina()

ground = Entity(model='plane', scale=(50,1,50), color=color.white.tint(-.2), texture='white_cube', texture_scale=(50,50), collider='box')
player = FirstPersonController(model='cube',collider = 'box', position=(0,0,-2))

locations = set()
for i in range(0,300):
    x = random.randrange(-24,24,2)
    y = 0
    z = random.randrange(-24,24,2)
    locations.add((x,y,z))
finish_location = random.choice(list(locations))
locations.remove(finish_location)
finish = Entity(model = 'cube', scale=(2,2,1), color=color.green, collider = 'box', position = finish_location)

for loc in locations:
    cube_width = 2
    cube_height = random.randrange(2,8,1)
    cube_depth = 1
    obstacle = Entity(model='cube', 
                    scale=(cube_width,cube_height,cube_depth),
                    position= loc,
                    texture='brick',
                    color=color.yellow.tint(.4),
                    collider='box')

def update(): 
    hit_info = player.intersects()
    if hit_info.hit:
        if hit_info.entity == finish:    
            message = Text(text = 'You WON', scale=2, origin=(0,0), background=True, color=color.blue)
            application.pause()
            mouse.locked = False 
countdown=30
def timedown():
    global countdown
    count = Text(text = 'Countdown: '+str(countdown), origin=(-2,-6),color=color.white)
    count.fade_out(0,0.5)
    countdown-=1
    seq = invoke(timedown, delay=1)
    if countdown == -1:
        end = Text(text = 'You LOST', scale=2, origin=(0,0), background=True, color=color.blue)
        application.pause()
        mouse.locked = False
        seq.kill()
    
timedown()

app.run()