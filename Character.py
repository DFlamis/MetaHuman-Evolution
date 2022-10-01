import pygame as pyg

class character( pyg.sprite.Sprite ):
    def __init__( self, path, x_position, y_position ):
        super().__init__(  )
        self.resource_path = path

        self.image = pyg.image.load( self.resource_path ).convert_alpha()
        self.rect = self.image.get_rect( center = (x_position, y_position) )

    def update( self ) -> None:
        self.image = pyg.image.load( self.resource_path ).convert_alpha()
