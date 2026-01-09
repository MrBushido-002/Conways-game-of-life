import pygame

class Pixel:
    def __init__(self,left_edge, top_edge, width=16, alive = False, alive_neighbor_count = 0):
        self.alive = False
        self.alive_neighbor_count = alive_neighbor_count
        self.width = width
        self.left_edge = left_edge
        self.top_edge = top_edge

    def rules(self):
        if self.alive == True and self.alive_neighbor_count < 2:
            self.alive = False

        if self.alive == True and self.alive_neighbor_count > 3:
            self.alive = False

        if self.alive == True and 1 < self.alive_neighbor_count < 4:
            self.alive = True

        if self.alive == False and self.alive_neighbor_count == 3:
            self.alive = True

        return self

    def draw(self, screen):
        if self.alive == True:
            col = "BLUE"
        elif self.alive == False: 
            col = "WHITE"
        pygame.draw.rect(screen, col, pygame.Rect(self.left_edge, self.top_edge , self.width, self.width))

def create_pixel_array():
    array = []
    for i in range(0, 50):
        array.append([])
    
    return array

def populate_array(array):
    top_edge = 0
    for i in array:
        left_edge = 0
        for j in range(0,50):
            i.append(Pixel(left_edge, top_edge))
            left_edge += 16
        
        top_edge += 16
    return array
        
def count_alive_neighbors(array):
    for i in range(0, 50): #i is the row of pixels
        for j in range(0, 50): #j is the self in row i
            array[i][j].alive_neighbor_count = 0
            try:
                if array[i-1][j-1].alive == True:
                    array[i][j].alive_neighbor_count += 1
            except IndexError:
                continue
            try:
                if array[i-1][j].alive == True:
                    array[i][j].alive_neighbor_count += 1
            except IndexError:
                continue
            try:
                if array[i-1][j+1].alive == True:
                    array[i][j].alive_neighbor_count += 1
            except IndexError:
                continue
            try:
                if array[i][j-1].alive == True:
                    array[i][j].alive_neighbor_count += 1
            except IndexError:
                continue
            try:
                if array[i][j+1].alive == True:
                    array[i][j].alive_neighbor_count += 1
            except IndexError:
                continue
            try:
                if array[i+1][j-1].alive == True:
                    array[i][j].alive_neighbor_count += 1
            except IndexError:
                continue
            try:
                if array[i+1][j].alive == True:
                    array[i][j].alive_neighbor_count += 1
            except IndexError:
                continue
            try:
                if array[i+1][j+1].alive == True:
                    array[i][j].alive_neighbor_count += 1
            except IndexError:
                continue
            
