from email.mime import base
from re import A
import Images as img
import pygame as pyg

sub_path = "Abilities/"

tarjetas = []
retroceder = []

def start(display, event):

    the_number = 2

    base_x = 120
    base_y = 10

    aumento_x = 210
    aumento_y = 360
    
    bakground_coor = [0,0]
    mainmenu_coor = [30,645]

    primera_coor = [base_x, base_y]
    segunda_coor = [base_x + aumento_x, base_y]
    tercera_coor = [base_x + (aumento_x *2), base_y]
    cuarta_coor = [base_x + (aumento_x *3), base_y]
    quinta_coor = [base_x + (aumento_x *4), base_y]

    sexta_coor = [base_x , base_y + (aumento_y)]
    septima_coor = [base_x + aumento_x, base_y + (aumento_y)]
    octava_coor = [base_x + (aumento_x *2), base_y + (aumento_y)]
    novena_coor = [base_x + (aumento_x *3), base_y + (aumento_y)]
    decima_coor = [base_x + (aumento_x *4), base_y + (aumento_y)]

    cargarElementos( display, 'Background' , bakground_coor )
    cargarElementos( display, 'tarjeta1', primera_coor )
    cargarElementos( display, 'tarjeta2', segunda_coor )
    cargarElementos( display, 'tarjeta3', tercera_coor )
    cargarElementos( display, 'locked', cuarta_coor )    
    cargarElementos( display, 'locked', quinta_coor )
    cargarElementos( display, 'locked', sexta_coor )
    cargarElementos( display, 'locked', septima_coor )
    cargarElementos( display, 'locked', octava_coor )
    cargarElementos( display, 'locked', novena_coor )
    cargarElementos( display, 'locked', decima_coor )

    cargarElementos( display, 'MainMenu', mainmenu_coor )

    if event.type == pyg.MOUSEBUTTONDOWN:
        x , y = pyg.mouse.get_pos()
        for j in range(len(tarjetas)):
            if retroceder[0][1].collidepoint(x, y):
                the_number = 0
                return the_number

            if tarjetas[j][1].collidepoint(x, y):
                if j == 0:
                    cargarElementos( display, 'tarjetaInfo1', primera_coor )
                elif j == 1:
                    cargarElementos( display, 'tarjetaInfo2', segunda_coor )
                elif j == 2:
                    cargarElementos( display, 'tarjetaInfo3', tercera_coor )

    return the_number
            
    
def cargarElementos(display, image_name, coor ):
    elemento = img.setImage(coor, img.root_path + sub_path + image_name +'.png')

    if (image_name != "locked") and (image_name != 'Background') and (image_name != 'MainMenu'):
        tarjetas.append(elemento)
    elif(image_name == 'MainMenu'):
        retroceder.append(elemento)
    
    pyg.display.set_caption("Estacion Espacial")
    display.blit( elemento[0], elemento[1] )
