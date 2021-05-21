import pygame

pygame.init()


window_x_size = 1000
window_y_size = 800
window = pygame.display.set_mode((window_x_size, window_y_size), 0, 0)

window_center = ((window_x_size/2), (window_y_size/2))

# Colors section
RED_204 = (204,37,18)
BLACK = (0,0,0)


x=0
while True:
    # Regras  
    
    # grafics
    window.fill(BLACK)
    pygame.draw.circle(window, RED_204, (500 + x, 400), 10, 0)
    pygame.display.update()

    # events
    x += 1

    for e in pygame.event.get():
        if e.type == pygame.QUIT: # check if the user have clicked on the X box to quit
            exit()
