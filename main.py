import pygame
import sys

# Initialize Pygame
pygame.init()

# Set screen dimensions
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Genshin Impact Lite")

# Set colors
WHITE = (255, 255, 255)
BLUE = (0, 0, 255)

# Set player attributes
player_width = 50
player_height = 50
player_x = SCREEN_WIDTH // 2 - player_width // 2
player_y = SCREEN_HEIGHT // 2 - player_height // 2
player_vel = 5

# Main game loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Player movement
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        player_x -= player_vel
    if keys[pygame.K_RIGHT]:
        player_x += player_vel
    if keys[pygame.K_UP]:
        player_y -= player_vel
    if keys[pygame.K_DOWN]:
        player_y += player_vel

    # Boundary checking
    player_x = max(0, min(SCREEN_WIDTH - player_width, player_x))
    player_y = max(0, min(SCREEN_HEIGHT - player_height, player_y))

    # Draw everything
    screen.fill(WHITE)
    pygame.draw.rect(screen, BLUE, (player_x, player_y, player_width, player_height))
    pygame.display.flip()

    # FPS
    pygame.time.Clock().tick(60)

pygame.quit()
sys.exit()
