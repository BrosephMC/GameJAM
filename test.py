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
BLUE = (0, 0, 255)
BLACK = (0, 0, 0)

# Player
player1_x, player1_y = 0, 0
player2_x, player2_y = GRID_WIDTH - 1, GRID_HEIGHT - 1
move_speed = 1  # Number of squares the player moves at a time

# Main game loop
def main():
    global player1_x, player1_y, player2_x, player2_y

    running = True

    while running:
        # Handle events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                # Player 1 movement with WASD
                if event.key == pygame.K_a and player1_x > 0:
                    player1_x -= move_speed
                elif event.key == pygame.K_d and player1_x < GRID_WIDTH - 1:
                    player1_x += move_speed
                elif event.key == pygame.K_w and player1_y > 0:
                    player1_y -= move_speed
                elif event.key == pygame.K_s and player1_y < GRID_HEIGHT - 1:
                    player1_y += move_speed
                # Player 2 movement with arrow keys
                elif event.key == pygame.K_LEFT and player2_x > 0:
                    player2_x -= move_speed
                elif event.key == pygame.K_RIGHT and player2_x < GRID_WIDTH - 1:
                    player2_x += move_speed
                elif event.key == pygame.K_UP and player2_y > 0:
                    player2_y -= move_speed
                elif event.key == pygame.K_DOWN and player2_y < GRID_HEIGHT - 1:
                    player2_y += move_speed

        # Draw grid
        WINDOW.fill(WHITE)
        for x in range(0, WIDTH, GRID_SIZE):
            pygame.draw.line(WINDOW, BLACK, (x, 0), (x, HEIGHT))
        for y in range(0, HEIGHT, GRID_SIZE):
            pygame.draw.line(WINDOW, BLACK, (0, y), (WIDTH, y))

        # Draw players
        pygame.draw.rect(WINDOW, RED, (player1_x * GRID_SIZE, player1_y * GRID_SIZE, GRID_SIZE, GRID_SIZE))
        pygame.draw.rect(WINDOW, BLUE, (player2_x * GRID_SIZE, player2_y * GRID_SIZE, GRID_SIZE, GRID_SIZE))

        pygame.display.update()

# Run the game
if __name__ == "__main__":
    main()
