import pygame as pyg
import station as st
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
        if event.type == pyg.QUIT or the_number == 4:
            run  = False

    #carga la estacion espacial
    if the_number == 0:
        the_number = st.start( display, event )
    #Carga la pantalla de misiones
    elif the_number == 1:
        the_number = msn.start( display, event )
    #Carga la pantalla 
    elif the_number == 2:
        print("boton2")
    elif the_number == 3:
        print("boton3")

    print(the_number)

    pyg.display.flip()
    clock.tick( fps )
pyg.quit