# Example file showing a circle moving on screen
import pygame
from pixels import Pixel
from pixels import*

# pygame setup
pygame.init()
pygame.display.set_caption("Conway's Game of Life")
screen_size = 800
tile_size = 16
screen = pygame.display.set_mode((screen_size, screen_size))
clock = pygame.time.Clock()
running = True

#draw grid
def draw_grid(tile_size):
    #screen.fill(pygame.Color(105,105,145))

    for x in range(tile_size, screen_size, tile_size):
        pygame.draw.line(screen, "GREY", (x, 0), (x,screen_size))

    for y in range(tile_size, screen_size, tile_size):
        pygame.draw.line(screen, "GREY", (0, y), (screen_size, y))

title_font = pygame.font.SysFont("Arial", 50)
regular_font = pygame.font.SysFont("Arial", 15)


def draw_text(text, font, x, y, text_col = "BLACK"):
    img = font.render(text, True, text_col)
    screen.blit(img, (x,y))

#create one pixel
#test_pixel = Pixel(784,784)

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

line_1 = "-Conway's Game of Life is a cellular automaton."
line_2 = "-Devised by the British mathematician John Horton Conway in 1970."
line_3 = "-It is a zero-player game, meaning that its evolution is determined by its initial state, requiring no further input."
line_4 = "-One interacts with the Game of Life by creating an initial configuration and"
line_5 = "observing how it evolves in discrete time steps called generations."
line_6 = "-There is no limit to the number of generations or win condition."
line_7 = "-Click the on the pixels to toggle whether they are dead or alive"
line_8 = "-Press s for start when you are ready to start the simulation"
line_9 = "-Press the SPACEBAR to exit the Title Screen!"



start_screen = True

game_start = False

while running:
    # poll for events
    # pygame.QUIT event means the user clicked X to close your window
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
        draw_text("This is Conways Game of life!", title_font, 40, 150)
        draw_text(line_1, regular_font, 80, 112*2)
        draw_text(line_2, regular_font, 80, 128*2)
        draw_text(line_3, regular_font, 80, 144*2)
        draw_text(line_4, regular_font, 80, 160*2)
        draw_text(line_5, regular_font, 80, 176*2)
        draw_text(line_6, regular_font, 80, 192*2)
        draw_text(line_7, regular_font, 80, 208*2)
        draw_text(line_8, regular_font, 80, 224*2)
        draw_text(line_9, regular_font, 80, 240*2)

    
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

    # flip() the display to put your work on screen
    pygame.display.flip()
    
    # limits FPS to 60
    # dt is delta time in seconds since last frame, used for framerate-
    # independent physics.
    dt = clock.tick(15) / 1000
    
pygame.quit()