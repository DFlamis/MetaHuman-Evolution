import pygame 
import Images as img

sub_path = "Station/"

bakground_coor = [0,0]
astronut_coor = [0,0]

button_play_coor = [700, 20]
button_habilities_coor = [700, 180 ]
button_garden_coor = [700, 340]
button_exit_coor = [700, 500]

buttons = []

def start( display, event ):
    the_number = 0
    cargarEstacion( display, 'Background' , bakground_coor )
    cargarEstacion( display, 'Astronaut-10', astronut_coor )
    cargarBotones(display, 'button_play', button_play_coor )
    cargarBotones(display, 'button_habilities', button_habilities_coor )
    cargarBotones(display, 'garden', button_garden_coor )
    cargarBotones(display, 'button_exit', button_exit_coor )

    if event.type == pygame.MOUSEBUTTONDOWN:
        x, y = pygame.mouse.get_pos()
        for button in buttons:
            if button[1].collidepoint(x, y):
                the_number = 1

    return the_number
    
def cargarEstacion(display, image_name, coor ):
    fondo = img.setImage(coor, img.root_path + sub_path + image_name +'.png')
    pygame.display.set_caption("Estacion Espacial")
    display.blit( fondo[0], fondo[1] )

def cargarBotones(display, image_name, coor ):
    button = img.setImage(coor, img.root_path + sub_path + image_name +'.png')
    buttons.append(button)
    display.blit( button[0], button[1] )
