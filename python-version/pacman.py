import pygame
from abc import ABCMeta, abstractmethod

pygame.init()

window = pygame.display.set_mode((800, 600), 0)

# Color used in the game
YELLOW = (255,255,0)
BLACK = (0,0,0)
BLUE = (13,56,143)
RED = (255, 0, 0)
speed = 1

class GamesElements(metaclass = ABCMeta):
    

    @abstractmethod
    def calculate_rules(self):
        pass
    @abstractmethod
    def draw(self):
        pass
    @abstractmethod
    def calculate_events(self, events):
        pass


class Scenery(GamesElements):
    def __init__(self, size, character):
        self.character = character
        self.size = size 
        self.points = 0
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
            half_size = self.size // 2
            color = BLACK
            if column == 2:
                color = BLUE
            pygame.draw.rect(surface, color, (x_box, y_box, self.size, self.size), 0)
            if column == 1:
                pygame.draw.circle(surface, YELLOW, (x_box + half_size, y_box + half_size), self.size//10, 0)
                
    def draw(self, surface):
        score_board_x = 30 * self.size # give us a a x ponint far from the maze
        text = f'Score {self.points}'
        score_board_font = pygame.font.SysFont('Arial', 22)
        score_board_text = score_board_font.render(text, True, YELLOW, None)
        window.blit(score_board_text, (score_board_x, 50))

    def paint_scenery(self, surface):
        for line_index, line in enumerate(self.matrix):
            self.paint_line(surface, line_index, line)
        self.draw(window)



    def calculate_rules(self):
        column_character = self.character.intention_column
        line_character = self.character.intention_line

        if 0 <= column_character < 28 and 0 <= line_character < 29: 
            if self.matrix[line_character][column_character] != 2:
                self.character.aprove_movement()
                if self.matrix[line_character][column_character] == 1:
                    self.points += 1
                    self.matrix[line_character][column_character] = 0
    def calculate_events(self, events):
        for e in events:
            if e.type == pygame.QUIT: # check if the user have clicked on the X box to quit
                exit()
        


class Pacman(GamesElements):
    def __init__(self, size):
        self.column = 1
        self.line = 1
        self.x_center = 400
        self.y_center = 300
        self.size = size # 2x radius and size/number of the cells
        self.speed_x = 0
        self.speed_y = 0
        self.radius = self.size // 2
        self.intention_column = self.column
        self.intention_line = self.line

    def calculate_rules(self):
        # calculate the movimentantion
        self.intention_column =  self.column + self.speed_x
        self.intention_line = self.line + self.speed_y
        

    def draw(self, surface):
        # Draw pacman's character
        pacman_body = pygame.draw.circle(surface, YELLOW, (self.x_center, self.y_center), self.radius, 0)
        
        
        # Coordinates
        x_eye_position = ( self.x_center + int( self.radius/4 ) )
        y_eye_position = ( self.y_center - int( (self.radius/2) ) )
        point_a = (self.x_center, self.y_center) # Center
        point_b = ((self.x_center + self.radius), self.y_center) # Right Center
        point_c = ((self.x_center + self.radius), (self.y_center - self.radius)) # Superior Right Center
        points = [point_a, point_b, point_c]
        # Pacman 
        pacman_eye = pygame.draw.circle(surface, BLACK, (x_eye_position, y_eye_position), int(self.radius/10), 0)
        pacman_mouth = pygame.draw.polygon(surface, BLACK, points, 0)
        # Make the draws
        pacman_body 
        pacman_eye
        pacman_mouth

    
    def calculate_events(self, events):
        for e in events:
            if e.type == pygame.KEYDOWN:
                if e.key == pygame.K_RIGHT or e.key == pygame.K_d:
                    self.speed_x = speed
                elif e.key == pygame.K_LEFT or e.key == pygame.K_a:
                    self.speed_x = -speed
                elif e.key == pygame.K_UP or e.key == pygame.K_w:
                    self.speed_y = -speed
                elif e.key == pygame.K_DOWN or e.key == pygame.K_s:
                    self.speed_y = speed
            elif e.type == pygame.KEYUP:
                if e.key == pygame.K_RIGHT or e.key == pygame.K_d:
                    self.speed_x = 0
                elif e.key == pygame.K_LEFT or e.key == pygame.K_a:
                    self.speed_x = 0
                elif e.key == pygame.K_UP or e.key == pygame.K_w:
                    self.speed_y = 0
                elif e.key == pygame.K_DOWN or e.key == pygame.K_s:
                    self.speed_y = 0

    def aprove_movement(self):
        self.column = self.intention_column
        self.line = self.intention_line
        self.x_center = int( self.column * self.size + self.radius ) 
        self.y_center = int( self.line * self.size + self.radius )
class Ghosts(GamesElements):
    def __init__(self, color):
        self.column = 7
        self.line = 8
        self.color = color
    def draw(self):
        ghost
        




    def calculate_events(self, events):
        pass
    def calculate_rules(self):
        pass

if __name__ == '__main__':
    size = 600 // 30
    pacman = Pacman(size)
    scenary = Scenery(size, pacman)  
    

    while True:

        # Game Rules
        pacman.calculate_rules()
        scenary.calculate_rules()

        
        # Figures
        window.fill(BLACK)
        scenary.paint_scenery(window)
        pacman.draw(window)
        pygame.display.update()
        pygame.time.delay(100)
        
        
        event = pygame.event.get()
        pacman.calculate_events(event)
        scenary.calculate_events(event)
        
            

