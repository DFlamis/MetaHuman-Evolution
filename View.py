import pygame as pyg

display_size = 1280, 720
display = pyg.display.set_mode( display_size )

pyg.display.set_caption('Nasa Space App challenges - MetaHuman Evolution')

run  = True

while run:
    for event in pyg.event.get():
        if event.type == pyg.QUIT:
            run  = False
    
    
    pyg.display.flip()
pyg.quit