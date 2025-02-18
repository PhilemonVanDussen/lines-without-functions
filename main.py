# Pygame game template

import pygame
import sys
import config # Import the config module

def init_game():
    pygame.init()
    screen = pygame.display.set_mode((config.WINDOW_WIDTH, config.WINDOW_HEIGHT)) # Use constants from config
    pygame.display.set_caption(config.TITLE)
    return screen

def handle_events():
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            return False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                return False
    return True

def main():
    screen = init_game()
    clock = pygame.time.Clock() # Initalize the clock here
    # Lines

    # Line 1
    start_pos1 = [150, 200]  
    end_pos1 = [500,400] 
    line_color1 = config.WHITE
    line_thickness1 = 8

    # Line 2
    start_pos2 = [50, 300]
    end_pos2 = [500,400] 
    line_color2 = config.RED
    line_thickness2 = 5
    
    # Line 3
    start_pos3 = [1, 600]
    end_pos3 = [500,400] 
    line_color3 = config.BLUE
    line_thickness3 = 4

    # Line 4
    start_pos4 = [320, 450]
    end_pos4 = [500,400] 
    line_color4 = config.BLACK
    line_thickness4 = 10
    
    # Line 5
    start_pos5 = [800, 250]
    end_pos5 = [500,400] 
    line_color5 = config.RED
    line_thickness5 = 9
    
    # Line 6
    start_pos6 = [670, 430]
    end_pos6 = [500,400] 
    line_color6 = config.WHITE
    line_thickness6 = 7

    running = True
    while running:
        running = handle_events()
        screen.fill(config.GREEN) # Use color from config
        # Draw lines
        pygame.draw.line(screen, line_color1, start_pos1, end_pos1, line_thickness1)
        pygame.draw.line(screen, line_color2, start_pos2, end_pos2, line_thickness2)
        pygame.draw.line(screen, line_color3, start_pos3, end_pos3, line_thickness3)
        pygame.draw.line(screen, line_color4, start_pos4, end_pos4, line_thickness4)
        pygame.draw.line(screen, line_color5, start_pos5, end_pos5, line_thickness5)
        pygame.draw.line(screen, line_color6, start_pos6, end_pos6, line_thickness6)
        pygame.display.flip()

        # Limit the frame rate to the specified frames per second
        clock.tick(config.FPS) # Use the clock to control the frame rate

    pygame.quit()
    sys.exit()

if __name__ == '__main__':
    main()



