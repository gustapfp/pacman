import pygame

pygame.init()

YELLOW = (255,255,0)
RED = (255, 0, 0)

window_x_size = 1000
window_y_size = 800
window = pygame.display.set_mode((window_x_size, window_y_size), 0, 0)


while True:
    pygame.draw.rect(window, YELLOW, (350, 300, 300, 200), 0)
    pygame.draw.polygon(window, RED, [(350,300 ), (650, 300), (500, 100)])
    pygame.display.update()

    for e in pygame.event.get():
            if e.type == pygame.QUIT: # check if the user have clicked on the X box to quit
                exit()
