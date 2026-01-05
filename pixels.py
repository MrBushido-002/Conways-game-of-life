import pygame

class Pixel:
    def __init__(self, alive = False, alive_neighbor_count = 0):
        self.alive = False
        self.alive_neighbor_count = alive_neighbor_count

    def rules(self):
        if pixel.alive == False and pixel.alive_neighbor_count == 3:
            pixel.alive = True

        if pixel.alive_neighbor_count < 2:
            pixel.alive = False
        
        if pixel.alive_neighbor_count < 3:
            pixel.alive = False

    def draw(self):
        pygame.draw.rect(screen, "BLACK", rect, width=10)
