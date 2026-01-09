import pygame

pygame.font.init()
text_font = pygame.font.SysFont("Arial", 30)

def draw_text(text, font, x, y, text_col = "BLACK"):
    img = font.render(text, True, text_col)
    screen.blit(img, (x,y))