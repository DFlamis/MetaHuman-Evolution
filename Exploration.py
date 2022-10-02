import pygame as pyg

import Images as img

sub_path = 'Exploration/'
location = [-1600,-1000]
movement_speed = 6
map_name = 'Map'

def start( display, key ):
    idk = generate_map( display, map_name, location[0], location[1] )
    fake_move( movement_speed, key, idk, display, 1 )

def generate_map( display, image_name, coor_x, coor_y ):
    Background_path = img.root_path + sub_path + image_name +'.png'
    Background_coor = [ coor_x ,coor_y]
    image_setter = img.setImage( Background_coor ,Background_path )
    display.blit( image_setter[0], image_setter[1] )
    return image_setter[1]

def generate_astronaut( frontA, backA, leftA, rightA):
    left = img.setImage( [640,360], img.root_path + sub_path + leftA +'.png' )
    right = img.setImage( [640,360], img.root_path + sub_path + rightA +'.png' )
    front = img.setImage( [640,360], img.root_path + sub_path + frontA +'.png' )
    back = img.setImage( [640,360], img.root_path + sub_path + backA +'.png' )
    return left, front, back, right

def fake_move( speed, key, something, display, pointer ):
    
    astronaut = generate_astronaut( 'Front','Back', 'Left', 'Right' )

    if key[pyg.K_UP]:
        print('UP')
        pointer = 2
        location[1] += speed
        
    elif key[pyg.K_DOWN]:
        print('DOWN')
        pointer = 1
        location[1] -= speed
    
    elif key[pyg.K_LEFT]:
        print('LEFT')
        pointer = 0
        location[0] += speed
        
    elif key[pyg.K_RIGHT]:
        print('RIGHT')
        pointer = 3
        location[0] -= speed  

    display.blit( astronaut[pointer][0],astronaut[1][1] )

    
    something.move_ip( location[0], location[1] )