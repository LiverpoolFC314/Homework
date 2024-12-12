import pgzrun 
WIDTH = 600
HEIGHT = 600
ash = Actor("ash")
ash.x = 300
ash.y = 300
pickachu = Actor("pickachu")
pickachu.x = 150
pickachu.y = 100
def draw():
    screen.fill("Blue")
    ash.draw()
    pickachu.draw()
def update():
    if keyboard.w:
        ash.y=+3 
    if keyboard.a:
        ash.x=-3 
    if keyboard.d:
        ash.x=+3 
    if keyboard.s:
        ash.y=-3 
pgzrun.go()

    


