import pygame as pyg

import Missions as msn

display_size = 1280, 720
display = pyg.display.set_mode( display_size )

pyg.display.set_caption('Nasa Space App challenges - MetaHuman Evolution')

fps = 60

run  = True
clock = pyg.time.Clock()

while run:
    for event in pyg.event.get():
        if event.type == pyg.QUIT:
            run  = False

    missions = msn.start( display )

    pyg.display.flip()
    clock.tick( fps )
pyg.quit