import pygame
import sys

# Initialize Pygame
pygame.init()

# Set up the display
width, height = 800, 600
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Chandrayaan 3")

# Define colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

# Initialize spacecraft properties
spacecraft_position = [0, 0, 0]
directions = ["N", "E", "S", "W"]
current_direction = "N"

# Define movement vectors for each direction
direction_vectors = {
    "N": [0, 1, 0],
    "E": [1, 0, 0],
    "S": [0, -1, 0],
    "W": [-1, 0, 0]
}




# Load images for spacecraft and buttons
spacecraft_image = pygame.image.load("C:/Users/tanvi/Desktop/CHANDARAYAN3/spacecraft.png")  
forward_button = pygame.image.load("C:/Users/tanvi/Desktop/CHANDARAYAN3/forward.png")  
right_button = pygame.image.load("C:/Users/tanvi/Desktop/CHANDARAYAN3/right.png")
left_button = pygame.image.load("C:/Users/tanvi/Desktop/CHANDARAYAN3/left.png")
background_image = pygame.image.load("C:/Users/tanvi/Desktop/CHANDARAYAN3/moon.jpeg")





spacecraft_image = pygame.transform.scale(spacecraft_image, (100, 100)) 
forward_button = pygame.transform.scale(forward_button, (50, 50)) 
right_button = pygame.transform.scale(right_button, (50, 50)) 
left_button = pygame.transform.scale(left_button, (50, 50)) 
# background_image = pygame.transform.scale(background_image, (width, height))



# Position of buttons
button_x = 100
forward_button_y = 400
right_button_y = 500
left_button_y = 500



# Define font for text
font = pygame.font.Font(None, 36)



# Main game loop
spacecraft_x = width // 2 - spacecraft_image.get_width() // 2
spacecraft_y = height // 2 - spacecraft_image.get_height() // 2
running = True
running = True
while running:
    screen.fill(WHITE)
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        
        # Handle keyboard key presses
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:  # Move forward
                movement_vector = direction_vectors[current_direction]
                spacecraft_position = [pos + move for pos, move in zip(spacecraft_position, movement_vector)]
            elif event.key == pygame.K_RIGHT:  # Turn right
                current_direction = directions[(directions.index(current_direction) + 1) % 4]
            elif event.key == pygame.K_LEFT:  # Turn left
                current_direction = directions[(directions.index(current_direction) - 1) % 4]

    # screen.blit(background_image, (0, 0))
    # Draw spacecraft image
    screen.blit(spacecraft_image, (width // 2 - spacecraft_image.get_width() // 2, height // 2 - spacecraft_image.get_height() // 2))
    
    # Draw buttons
    screen.blit(forward_button, (button_x, forward_button_y))
    screen.blit(right_button, (button_x, right_button_y))
    screen.blit(left_button, (button_x, left_button_y))
    
    # Display current position and direction on the screen
    position_text = font.render("Current Position: {}".format(spacecraft_position), True, BLACK)
    direction_text = font.render("Current Direction: {}".format(current_direction), True, BLACK)
    screen.blit(position_text, (20, 20))
    screen.blit(direction_text, (20, 60))
    
    pygame.display.flip()

pygame.quit()
sys.exit()
