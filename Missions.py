import Images as img

import pygame as pyg

pyg.init()

sub_path = 'Missions/'
color_text = (255,255,255)

font_text = 'Consolas'

text_w = 300
text_h = 350

conditions_test = ['High temperatures','Low atmosphere pressure','Low oxigen level']

font = pyg.font.SysFont(font_text,35) #Titulo
font2 = pyg.font.SysFont(font_text,22) #Subtitulo
font3 = pyg.font.SysFont(font_text,20) #Texto

def start( display, event ):
    mission_background( display, 'Background' )
    mission_background( display, 'Screen' )
    # mission_background( display, 'Left' )
    # mission_background( display, 'Right' )

    set_text( display, conditions_test )

    idk = set_buttons( display, 'Left', 'Right' )

    if event.type == pyg.MOUSEBUTTONDOWN:
        x , y = pyg.mouse.get_pos()
        if idk[0].collidepoint(x, y):
            print('IZQUIERDA')
        if idk[1].collidepoint(x, y):
            print('DERECHA')

def mission_background( display, image_name ):
    Background_path = img.root_path + sub_path + image_name +'.png'
    Background_coor = [0,0]
    image_setter = img.setImage( Background_coor ,Background_path )
    display.blit( image_setter[0], image_setter[1] )

def set_text( display, conditions ):
    mission_name = 'First Mission'
    mission_description = 'Search some minerals for improving your equipment'
    planet_name = 'Planet name: ZaiDek'
    planet_description = 'Planet conditions:'

    mission_name_screen = font.render( mission_name, True, color_text )
    mission_description_screen = font3.render( mission_description, True, color_text )
    planet_name_sceen = font2.render( planet_name, True, color_text )
    planet_description_screen = font2.render( planet_description, True, color_text )

    mission_description_rect = mission_description_screen.get_rect( center = (640,220) )
    planet_name_rect = mission_name_screen.get_rect( center = (640,160) )

    display.blit( mission_name_screen, planet_name_rect )
    display.blit( mission_description_screen, (mission_description_rect) )
    display.blit( planet_name_sceen, (text_w,280) )
    display.blit( planet_description_screen, (text_w,320) )

    space = 0
    for condition in conditions:
        temp_condition_screen = font3.render( condition, True, color_text )
        display.blit( temp_condition_screen, (text_w + 50, text_h + space) )
        space += 30

def set_buttons( display, image_name1, image_name2 ):
    left = img.setImage( [220,330], img.root_path + sub_path + image_name1 +'.png' )
    right = img.setImage( [1030,330], img.root_path + sub_path + image_name2 +'.png' )
    
    display.blit( left[0], left[1] )
    display.blit( right[0], right[1] )
    
    return left[1], right[1]