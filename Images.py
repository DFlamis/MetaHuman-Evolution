import pygame as pyg
root_path = 'Resources/'

def setImage(coord,path):
    imgA = pyg.image.load(path).convert_alpha()
    imgB = imgA.get_rect()
    imgB.move_ip(coord[0],coord[1])
    return imgA,imgB