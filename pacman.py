import pygame

pygame.init()

window_x_size = 800
window_y_size = 800
window = pygame.display.set_mode((window_x_size, window_y_size), 0, 0)

# Color used in the game
YELLOW = (255,255,0)
BLACK = (0,0,0)
BLUE = (13,56,143)
WHITE = (255, 255, 255)

class Scenery:
    def __init__(self, size):
        self.size = size // 30

        self.matrix = [ 
            [2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2],
            [2, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 2, 2, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 2],
            [2, 1, 2, 2, 2, 2, 1, 2, 2, 2, 2, 2, 1, 2, 2, 1, 2, 2, 2, 2, 2, 1, 2, 2, 2, 2, 1, 2],
            [2, 1, 2, 2, 2, 2, 1, 2, 2, 2, 2, 2, 1, 1, 1, 1, 2, 2, 2, 2, 2, 1, 2, 2, 2, 2, 1, 2],
            [2, 1, 2, 2, 2, 2, 1, 2, 2, 2, 2, 2, 1, 2, 2, 1, 2, 2, 2, 2, 2, 1, 2, 2, 2, 2, 1, 2],
            [2, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 2, 2, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 2],
            [2, 1, 2, 2, 2, 2, 1, 2, 2, 1, 2, 2, 2, 2, 2, 2, 2, 2, 1, 2, 2, 1, 2, 2, 2, 2, 1, 2],
            [2, 1, 2, 2, 2, 2, 1, 2, 2, 1, 2, 2, 2, 2, 2, 2, 2, 2, 1, 2, 2, 1, 2, 2, 2, 2, 1, 2],
            [2, 1, 1, 1, 1, 1, 1, 2, 2, 1, 1, 1, 1, 2, 2, 1, 1, 1, 1, 2, 2, 1, 1, 1, 1, 1, 1, 2],
            [2, 2, 2, 1, 2, 2, 1, 2, 2, 2, 2, 2, 1, 2, 2, 1, 2, 2, 2, 2, 2, 1, 2, 2, 1, 2, 2, 2],
            [2, 2, 2, 1, 2, 2, 1, 2, 2, 2, 2, 2, 1, 2, 2, 1, 2, 2, 2, 2, 2, 1, 2, 2, 1, 2, 2, 2],
            [2, 1, 1, 1, 2, 2, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 2, 2, 1, 1, 1, 2],
            [2, 1, 2, 2, 2, 2, 1, 2, 2, 1, 2, 2, 0, 0, 0, 0, 2, 2, 1, 2, 2, 1, 2, 2, 2, 2, 1, 2],
            [2, 1, 2, 2, 2, 2, 1, 2, 2, 1, 2, 0, 0, 0, 0, 0, 0, 2, 1, 2, 2, 1, 2, 2, 2, 2, 1, 2],
            [2, 1, 1, 1, 1, 1, 1, 2, 2, 1, 2, 0, 0, 0, 0, 0, 0, 2, 1, 2, 2, 1, 1, 1, 1, 1, 1, 2],
            [2, 1, 2, 2, 2, 2, 1, 2, 2, 1, 2, 0, 0, 0, 0, 0, 0, 2, 1, 2, 2, 1, 2, 2, 2, 2, 1, 2],
            [2, 1, 2, 2, 2, 2, 1, 2, 2, 1, 2, 2, 2, 2, 2, 2, 2, 2, 1, 2, 2, 1, 2, 2, 2, 2, 1, 2],
            [2, 1, 1, 1, 2, 2, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 2, 2, 1, 1, 1, 2],
            [2, 2, 2, 1, 2, 2, 1, 2, 2, 2, 2, 2, 1, 2, 2, 1, 2, 2, 2, 2, 2, 1, 2, 2, 1, 2, 2, 2],
            [2, 2, 2, 1, 2, 2, 1, 2, 2, 2, 2, 2, 1, 2, 2, 1, 2, 2, 2, 2, 2, 1, 2, 2, 1, 2, 2, 2],
            [2, 1, 1, 1, 1, 1, 1, 2, 2, 1, 1, 1, 1, 2, 2, 1, 1, 1, 1, 2, 2, 1, 1, 1, 1, 1, 1, 2],
            [2, 1, 2, 2, 2, 2, 1, 2, 2, 1, 2, 2, 2, 2, 2, 2, 2, 2, 1, 2, 2, 1, 2, 2, 2, 2, 1, 2],
            [2, 1, 2, 2, 2, 2, 1, 2, 2, 1, 2, 2, 2, 2, 2, 2, 2, 2, 1, 2, 2, 1, 2, 2, 2, 2, 1, 2],
            [2, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 2, 2, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 2],
            [2, 1, 2, 2, 2, 2, 1, 2, 2, 2, 2, 2, 1, 2, 2, 1, 2, 2, 2, 2, 2, 1, 2, 2, 2, 2, 1, 2],
            [2, 1, 2, 2, 2, 2, 1, 2, 2, 2, 2, 2, 1, 1, 1, 1, 2, 2, 2, 2, 2, 1, 2, 2, 2, 2, 1, 2],
            [2, 1, 2, 2, 2, 2, 1, 2, 2, 2, 2, 2, 1, 2, 2, 1, 2, 2, 2, 2, 2, 1, 2, 2, 2, 2, 1, 2],
            [2, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 2, 2, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 2],
            [2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2]
        ]


    def paint_line(self, surface, line_index, line):
        for column_index, column in enumerate(line):
            x_box = column_index * self.size
            y_box = line_index * self.size
            half_size = self.size //2

            if column == 2:
                pygame.draw.rect(surface, BLUE, (x_box, y_box, self.size, self.size), 0)
            elif column == 1:
                pygame.draw.circle(surface, YELLOW, (x_box + half_size, y_box + half_size), self.size//10, 0)
            else:
                pygame.draw.rect(surface, BLACK, (x_box, y_box, self.size, self.size), 0)

    def paint_scenery(self, surface): # , matrixcolumn, matrix_liner
        for line_index, line in enumerate(self.matrix):
            self.paint_line(surface, line_index, line)
        


class Pacman:
    def __init__(self):
        self.line = 1
        self.column = 1
        self.size = int(window_x_size//30) # 2x radius and size/number of the cells
        self.radius = int((self.size//2))
        self.x_center = int((window_x_size//2))
        self.y_center = int((window_y_size//2))
        self.speed_x = 0
        self.speed_y = 0
    
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
    
    def calculate_rules(self):
        self.column += self.speed_x
        self.line += self.speed_y
        self.x_center = int( (self.column * self.size) + self.radius ) 
        self.y_center = int( (self.line * self.size) + self.radius )

       
        
    
if __name__ == '__main__':
    pacman = Pacman()
    scenary = Scenery(window_x_size)


   

    while True:

        # Game Rules
        pacman.calculate_rules()

        scenary.paint_scenery(window)

        
        # Figures

        pacman.draw_pacman(window)
        pygame.display.update()
        window.fill(BLACK)
        pygame.time.delay(100)

        eventos = pygame.event.get()
        for e in eventos:
            if e.type == pygame.QUIT: # check if the user have clicked on the X box to quit
                exit()
            elif e.type == pygame.KEYDOWN:
                if e.key == pygame.K_RIGHT or e.key == pygame.K_d:
                    pacman.speed_x = 1
                elif e.key == pygame.K_LEFT or e.key == pygame.K_a:
                    pacman.speed_x = -1
                elif e.key == pygame.K_UP or e.key == pygame.K_w:
                    pacman.speed_y = -1
                elif e.key == pygame.K_DOWN or e.key == pygame.K_s:
                    pacman.speed_y = 1
            elif e.type == pygame.KEYUP:
                pacman.speed_x = 0
                pacman.speed_y = 0
            

