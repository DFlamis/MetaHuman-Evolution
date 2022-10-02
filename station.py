import pygame 
import Images as img
import Missions as msn

sub_path = "Station/"

bakground_coor = [0,0]
astronut_coor = [100,0]

button_play_coor = [700, 20]
button_habilities_coor = [700, 180 ]
button_garden_coor = [700, 340]
button_exit_coor = [700, 500]

buttons = []

def start( display, event ):
    the_number = 0
    cargarEstacion( display, 'Background' , bakground_coor )
    cargarEstacion( display, 'Astronaut', astronut_coor )
    cargarBotones(display, 'button_play', button_play_coor )
    cargarBotones(display, 'button_abilities', button_habilities_coor )
    cargarBotones(display, 'button_garden', button_garden_coor )
    cargarBotones(display, 'button_exit', button_exit_coor )

    if event.type == pygame.MOUSEBUTTONDOWN:
        x, y = pygame.mouse.get_pos()
        for i in range(len(buttons)):
            if buttons[i][1].collidepoint(x, y):
                if i == 0:
                    the_number = 1
                    print("boton 1")
                elif i == 1:
                    the_number = 2
                    print("boton 2")
                elif i == 2:
                    the_number = 3
                    print("boton 3")
                elif i == 3:
                    the_number = 4
                    print("boton 4")
    
    return the_number
    
def cargarEstacion(display, image_name, coor ):
    fondo = img.setImage(coor, img.root_path + sub_path + image_name +'.png')
    pygame.display.set_caption("Estacion Espacial")
    display.blit( fondo[0], fondo[1] )

def cargarBotones(display, image_name, coor ):
    button = img.setImage(coor, img.root_path + sub_path + image_name +'.png')
    buttons.append(button)
    display.blit( button[0], button[1] )

