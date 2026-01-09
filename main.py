import pygame
from pixels import Pixel
from pixels import*

pygame.init()
pygame.display.set_caption("Conway's Game of Life")
screen_size = 800
tile_size = 16
screen = pygame.display.set_mode((screen_size, screen_size))
clock = pygame.time.Clock()
running = True

#draw grid
def draw_grid(tile_size):

    for x in range(tile_size, screen_size, tile_size):
        pygame.draw.line(screen, "GREY", (x, 0), (x,screen_size))

    for y in range(tile_size, screen_size, tile_size):
        pygame.draw.line(screen, "GREY", (0, y), (screen_size, y))

title_screen = pygame.image.load("title_screen.png")

#create array of pixels
pix_array = create_pixel_array()
pix_array = populate_array(pix_array)

#create default alive pixels
pix_array[24][25].alive = True
pix_array[24][26].alive = True
pix_array[25][25].alive = True
pix_array[25][24].alive = True
pix_array[26][24].alive = True
pix_array[26][23].alive = True 

start_screen = True

game_start = False

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        
        if pygame.mouse.get_pressed()[0] == True:
            x_index = pygame.mouse.get_pos()[0] // 16
            y_index = pygame.mouse.get_pos()[1] // 16
            pix_array[y_index][x_index].alive = not pix_array[y_index][x_index].alive

        keys = pygame.key.get_pressed()

        if keys[pygame.K_SPACE]:
            start_screen = False
        
        if keys[pygame.K_s]:
            game_start = True

    if game_start == False and start_screen == True:
        screen.fill("WHITE")
        screen.blit(title_screen, (0, 60))

    if start_screen == False:
        screen.fill("BLACK")

        #draw array of pixels
        for arr in pix_array:
            for pix in arr:
                pix.draw(screen)

        draw_grid(tile_size)
    
    if game_start == True:

        count_alive_neighbors(pix_array)

        for arr in pix_array:
            for pix in arr:
                pix.rules()

    pygame.display.flip()
    
    dt = clock.tick(15) / 1000
    
pygame.quit()