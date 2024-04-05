import pygame
import sys

# Initialize Pygame
pygame.init()

# Set screen dimensions
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Simple Platformer")

# Set colors
WHITE = (255, 255, 255)
BLUE = (0, 0, 255)

# Set player attributes
player_width = 50
player_height = 50
player_x = 50
player_y = SCREEN_HEIGHT - player_height - 50
player_vel = 5

# Set gravity
gravity = 0.5
player_jump = False
jump_velocity = 10

# Set floor attributes
floor_y = SCREEN_HEIGHT - 50

# Main game loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE and not player_jump:
                player_jump = True

    # Player movement
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        player_x -= player_vel
    if keys[pygame.K_RIGHT]:
        player_x += player_vel

    # Jumping mechanic
    if player_jump:
        player_y -= jump_velocity
        jump_velocity -= gravity
        if jump_velocity < -10:
            player_jump = False
            jump_velocity = 10

    # Collision detection with the floor
    if player_y >= floor_y - player_height:
        player_y = floor_y - player_height
        player_jump = False
        jump_velocity = 10

    # Apply gravity
    player_y += gravity

    # Draw everything
    screen.fill(WHITE)
    pygame.draw.rect(screen, BLUE, (player_x, player_y, player_width, player_height))
    pygame.display.flip()

    # FPS
    pygame.time.Clock().tick(60)

pygame.quit()
sys.exit()
