from email.mime import base
import Images as img
import pygame as pyg

sub_path = "Abilities/"

def start(display, evento):

    base_x = 120
    base_y = 10

    aumento_x = 210
    aumento_y = 360
    
    bakground_coor = [0,0]
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
    
def cargarElementos(display, image_name, coor ):
    elemento = img.setImage(coor, img.root_path + sub_path + image_name +'.png')
    pyg.display.set_caption("Estacion Espacial")
    display.blit( elemento[0], elemento[1] )