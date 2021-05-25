import pygame

pygame.init()

window_x_size = 800
window_y_size = 600
window = pygame.display.set_mode((window_x_size, window_y_size), 0, 0)

# Color used in the pacman draw
YELLOW = (255,255,0)
BLACK = (0,0,0)


class Pacman:
    def __init__(self):
        self.x_center = int((window_x_size/2))
        self.y_center = int((window_y_size/2))
        self.size = 100 # 2x radius
        self.radius = int((self.size/2))
    
    def draw_pacman(self, surface):
        # Draw pacman's character
        
        # Coordinates
        x_eye_position = (self.x_center + int(self.radius/4))
        y_eye_position = ( self.y_center - int( (self.radius/2) ) )
        point_a = (self.x_center, self.y_center) # Center
        point_b = ((self.x_center + self.radius), self.y_center) # Right Center
        point_c = ((self.x_center + self.radius), (self.y_center - self.radius)) # Superior Right Center

        # Pacman 
        pacman_body = pygame.draw.circle(surface, YELLOW, (self.x_center, self.y_center), self.radius, 0)
        pacman_eye = pygame.draw.circle(surface, BLACK, (x_eye_position, y_eye_position), int(self.radius/10), 0)
        pacman_mouth = pygame.draw.polygon(surface, BLACK, [point_a, point_b, point_c], 0)
        return pacman_body, pacman_eye, pacman_mouth
    
    def draw_mirror_pacman(self, surface):
        # Draw pacman's character
        
        # Coordinates
        x_eye_position = (self.x_center - int(self.radius/4))
        y_eye_position = ( self.y_center - int( (self.radius/2) ) )
        point_a = (self.x_center, self.y_center) # Center
        point_b = ((self.x_center - self.radius), self.y_center) # Right Center
        point_c = ((self.x_center - self.radius), (self.y_center - self.radius)) # Superior Right Center

        # Pacman 
        pacman_body = pygame.draw.circle(surface, YELLOW, (self.x_center, self.y_center), self.radius, 0)
        pacman_eye = pygame.draw.circle(surface, BLACK, (x_eye_position, y_eye_position), int(self.radius/10), 0)
        pacman_mouth = pygame.draw.polygon(surface, BLACK, [point_a, point_b, point_c], 0)
        return pacman_body, pacman_eye, pacman_mouth


if __name__ == '__main__':
    pacman = Pacman()

    while True:

        pacman.draw_mirror_pacman(window)
        pygame.display.update()


        for e in pygame.event.get():
            if e.type == pygame.QUIT: # check if the user have clicked on the X box to quit
                exit()