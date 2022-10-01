import Images as img

sub_path = 'Missions/'

def start( display ):
    mission_background( display, 'Background' )
    mission_background( display, 'Screen' )

def mission_background( display, image_name ):
    Background_path = img.root_path + sub_path + image_name +'.png'
    Background_coor = [0,0]
    image_setter = img.setImage( Background_coor ,Background_path )
    display.blit( image_setter[0], image_setter[1] )
