import pygame

pygame.init()


window_x_size = 1000
window_y_size = 800
window = pygame.display.set_mode((window_x_size, window_y_size), 0, 0)

window_center = ((window_x_size/2), (window_y_size/2))

# Colors section
RED_204 = (204,37,18)
BLACK = (0,0,0)


spd_x = 0.1

x_pos = 0
while True:
    # RUles  
    
    # grafics
    window.fill(BLACK)

    x_pos += spd_x
    pygame.draw.circle(window, RED_204, (int(x_pos), 400), 10, 0)
    pygame.display.update()

    # events
    if x_pos > window_x_size: # 10 is the circle radius x2 value
        spd_x = -0.1
    elif x_pos < 0:
        spd_x = 0.1

    for e in pygame.event.get():
        if e.type == pygame.QUIT: # check if the user have clicked on the X box to quit
            exit()
