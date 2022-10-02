import pygame as pyg

import Images as img

sub_path = 'Exploration/'
location = [50,50]
movement_speed = 6
map_name = 'Map'

def start( display, key ):
    fake_move( movement_speed, key, display )
    # display.blit( image_setter[0], image_setter[1] )

def generate_map( display, image_name, coor_x, coor_y ):
    Background_path = img.root_path + sub_path + image_name +'.jpg'
    Background_coor = [ coor_x ,coor_y]
    image_setter = img.setImage( Background_coor ,Background_path )
    display.blit( image_setter[0], image_setter[1] )

def fake_move( speed, key, display ):
    
    if key[pyg.K_UP]:
        print('UP')
        location[1] += speed
        # sprite = sprite.update( location[0], location[1])
        
    elif key[pyg.K_DOWN]:
        print('DOWN')
        location[1] -= speed
        # sprite = sprite.update( location[0], location[1])
    
    elif key[pyg.K_LEFT]:
        print('LEFT')
        location[0] += speed
        # sprite = sprite.update( location[0], location[1] )
        
    elif key[pyg.K_RIGHT]:
        print('RIGHT')
        location[0] -= speed  
        # sprite = sprite.update( location[0], location[1] )
    
    generate_map( display, map_name,location[0], location[1] )