import pygame as pyg
import Station as st
import Missions as msn

display_size = 1280, 720
display = pyg.display.set_mode( display_size )

pyg.display.set_caption('Nasa Space App challenges - MetaHuman Evolution')

fps = 60

the_number = 0

run  = True
clock = pyg.time.Clock()

while run:
    for event in pyg.event.get():
        if event.type == pyg.QUIT:
            run  = False
        elif event.type == pyg.MOUSEBUTTONDOWN:
            st.buttons_click(display, event, pyg.mouse.get_pos())

    #carga la estacion espacial
    if the_number == 0:
        the_number = st.start( display, event )
    #Carga la pantalla de misiones
    elif the_number == 1:
        msn.start( display, event )
    
    pyg.display.flip()
    clock.tick( fps )
pyg.quit