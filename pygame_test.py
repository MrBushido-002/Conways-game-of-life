# Example file showing a circle moving on screen
import pygame
import Pixel

# pygame setup
pygame.init()
screen_size = 800
tile_size = 15
screen = pygame.display.set_mode((screen_size, screen_size))
clock = pygame.time.Clock()
running = True
dt = 0





#draw grid
def draw_grid(tile_size):
    screen.fill(pygame.Color(105,105,145))

    for x in range(tile_size, screen_size, tile_size):
        pygame.draw.line(screen, "black", (x, 0), (x,screen_size))

    for y in range(tile_size, screen_size, tile_size):
        pygame.draw.line(screen, "black", (0, y), (screen_size, y))

#create one pixel
test_pixel = Pixel()

while running:
    # poll for events
    # pygame.QUIT event means the user clicked X to close your window
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    draw_grid(tile_size)
    test_pixel.draw()
    
    # flip() the display to put your work on screen
    pygame.display.flip()

    # limits FPS to 60
    # dt is delta time in seconds since last frame, used for framerate-
    # independent physics.
    dt = clock.tick(60) / 1000

pygame.quit()


