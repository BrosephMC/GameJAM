import pygame
import random

# Initialize Pygame
pygame.init()

# Set the screen dimensions
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Shaking PNG Example")

# Load the PNG image
image = pygame.image.load("images/player1.png")
image_rect = image.get_rect()

# Define colors
WHITE = (255, 255, 255)

# Define a function to shake the camera
def shake_camera(duration):
    start_time = pygame.time.get_ticks()
    shake_offset = (0, 0)
    while pygame.time.get_ticks() - start_time < duration:
        shake_offset = (random.randint(-5, 5), random.randint(-5, 5))
        yield shake_offset
    yield (0, 0)  # Return to original position after shake is over

# Main game loop
running = True
shake_generator = shake_camera(1000)  # Shake for 1000 milliseconds (1 second)
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Clear the screen
    screen.fill(WHITE)

    # Get the camera shake offset
    shake_offset = next(shake_generator)

    # Draw the image with the shake offset
    screen.blit(image, (200 + shake_offset[0], 200 + shake_offset[1]))

    # Update the display
    pygame.display.flip()

    # Cap the frame rate
    pygame.time.Clock().tick(60)

# Quit Pygame
pygame.quit()

