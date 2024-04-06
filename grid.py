import pygame
import sys

# Initialize Pygame
pygame.init()

# Set up the window
WIDTH, HEIGHT = 640, 480
GRID_SIZE = 40
GRID_WIDTH, GRID_HEIGHT = WIDTH // GRID_SIZE, HEIGHT // GRID_SIZE
WINDOW = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Grid Movement Game")

# Colors
WHITE = (255, 255, 255)
RED = (255, 0, 0)
BLACK = (0, 0, 0)

# Player
player_x = 0
player_y = 0
move_speed = 1  # Number of squares the player moves at a time

# Main game loop
def main():
    global player_x, player_y

    running = True

    while running:
        # Handle events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                # Move player one square at a time when arrow keys are pressed
                if event.key == pygame.K_LEFT and player_x > 0:
                    player_x -= move_speed
                elif event.key == pygame.K_RIGHT and player_x < GRID_WIDTH - 1:
                    player_x += move_speed
                elif event.key == pygame.K_UP and player_y > 0:
                    player_y -= move_speed
                elif event.key == pygame.K_DOWN and player_y < GRID_HEIGHT - 1:
                    player_y += move_speed

        # Draw grid
        WINDOW.fill(WHITE)
        for x in range(0, WIDTH, GRID_SIZE):
            pygame.draw.line(WINDOW, BLACK, (x, 0), (x, HEIGHT))
        for y in range(0, HEIGHT, GRID_SIZE):
            pygame.draw.line(WINDOW, BLACK, (0, y), (WIDTH, y))

        # Draw player
        pygame.draw.rect(WINDOW, RED, (player_x * GRID_SIZE, player_y * GRID_SIZE, GRID_SIZE, GRID_SIZE))

        pygame.display.update()

# Run the game
if __name__ == "__main__":
    main()
