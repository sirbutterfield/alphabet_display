import pygame
import sys

pygame.init()

screen_width = 800
screen_height = 600

screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Wyświetlacz alfabetu")

clock = pygame.time.Clock()
black = (0, 0, 0)
white = (255, 255, 255)
green = (0, 255, 0)
red = (255, 0, 0)
font = pygame.font.Font(None, 40)
run = False
start = pygame.Rect(50, 50, 100, 50)
stop = pygame.Rect(200, 50, 100, 50)
alfabet = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'R', 'S', 'T', 'U', 'W', 'X', 'Y', 'Z']
index = 0

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if start.collidepoint(event.pos):
                run = True
            elif stop.collidepoint(event.pos):
                run = False

    if run:
        screen.fill(black)
        text = font.render(alfabet[index], True, white)
        screen.blit(text, (screen_width // 2 - text.get_width() // 2, screen_height // 2 - text.get_height() // 2))
        
        index = (index + 1) % len(alfabet)
    
    pygame.draw.rect(screen, green, start)
    pygame.draw.rect(screen, red, stop)

    start_text = font.render("Start", True, black)
    stop_text = font.render("Stop", True, black)

    screen.blit(start_text, (start.centerx - start_text.get_width() // 2, start.centery - start_text.get_height() // 2))
    screen.blit(stop_text, (stop.centerx - stop_text.get_width() // 2, stop.centery - stop_text.get_height() // 2))

    pygame.display.flip()
    clock.tick(1)
