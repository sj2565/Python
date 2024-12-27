from pygame import *

init()

screen = display.set_mode([300, 200])
pygame.display.set_caption('간단한 파이게임 윈도!')

done = False
while not done:
    for e in event.get():
        if e.type == QUIT:
            done = True

    display.update()
quit()    

    











            
