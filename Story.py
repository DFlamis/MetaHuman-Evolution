from re import sub
import Images as img
import pygame as pyg

pyg.init()

sub_path = 'Story/'

def start( display, event ):
    the_number = 3
    mission_background( display, 'Background', [0,0] )
    mission_background( display, 'Screen', [0,0] )
    mission_background( display, '1', [290,130])

    idk = set_buttons( display, 'Left', 'Right', 'MainMenu' )

    if event.type == pyg.MOUSEBUTTONDOWN:
        x , y = pyg.mouse.get_pos()
        if idk[0].collidepoint(x, y):
            print('IZQUIERDA')
        if idk[1].collidepoint(x, y):
            print('DERECHA')
        if idk[2].collidepoint(x, y):
            the_number = 0
    
    return the_number

def mission_background( display, image_name, coor ):
    Background_path = img.root_path + sub_path + image_name +'.png'
    image_setter = img.setImage( coor ,Background_path )
    display.blit( image_setter[0], image_setter[1] )
    

def set_buttons( display, image_name1, image_name2, image_name4 ):
    left = img.setImage( [220,330], img.root_path + sub_path + image_name1 +'.png' )
    right = img.setImage( [1030,330], img.root_path + sub_path + image_name2 +'.png' )
    menu = img.setImage( [30,650], img.root_path + sub_path + image_name4 +'.png' ) #280,530
    
    display.blit( left[0], left[1] )
    display.blit( right[0], right[1] )
    display.blit( menu[0], menu[1] )
    
    return left[1], right[1], menu[1]