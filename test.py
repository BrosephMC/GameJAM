import pygame
import sys

# Initialize Pygame
pygame.init()

# Set up the window
WIDTH, HEIGHT = 500, 700
GRID_WIDTH, GRID_HEIGHT = 6, 7
GRID_SIZE = min((WIDTH - 100) // GRID_WIDTH, (HEIGHT - 100) // GRID_HEIGHT)
BORDER_SIZE = 4
WINDOW = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Grid Movement Game")

# Load player and opponent images
player_image = pygame.image.load('images/player.png').convert_alpha()
player_image = pygame.transform.scale(player_image, (GRID_SIZE, GRID_SIZE))
opponent_image = pygame.image.load('images/opponent.png').convert_alpha()
opponent_image = pygame.transform.scale(opponent_image, (GRID_SIZE, GRID_SIZE))

# Main game loop
def main():
    player1_x, player1_y = 0, 0
    player2_x, player2_y = GRID_WIDTH - 1, GRID_HEIGHT - 1
    move_speed = 1  # Number of squares the player moves at a time

    running = True

    while running:
        # Handle events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                # Player 1 movement with WASD
                if event.key == pygame.K_a and player1_x > 0 and (player1_x - move_speed, player1_y) != (player2_x, player2_y):
                    player1_x -= move_speed
                elif event.key == pygame.K_d and player1_x < GRID_WIDTH - 1 and (player1_x + move_speed, player1_y) != (player2_x, player2_y):
                    player1_x += move_speed
                elif event.key == pygame.K_w and player1_y > 0 and (player1_x, player1_y - move_speed) != (player2_x, player2_y):
                    player1_y -= move_speed
                elif event.key == pygame.K_s and player1_y < GRID_HEIGHT - 1 and (player1_x, player1_y + move_speed) != (player2_x, player2_y):
                    player1_y += move_speed
                # Player 2 movement with arrow keys
                elif event.key == pygame.K_LEFT and player2_x > 0 and (player2_x - move_speed, player2_y) != (player1_x, player1_y):
                    player2_x -= move_speed
                elif event.key == pygame.K_RIGHT and player2_x < GRID_WIDTH - 1 and (player2_x + move_speed, player2_y) != (player1_x, player1_y):
                    player2_x += move_speed
                elif event.key == pygame.K_UP and player2_y > 0 and (player2_x, player2_y - move_speed) != (player1_x, player1_y):
                    player2_y -= move_speed
                elif event.key == pygame.K_DOWN and player2_y < GRID_HEIGHT - 1 and (player2_x, player2_y + move_speed) != (player1_x, player1_y):
                    player2_y += move_speed

        # Draw background
        WINDOW.fill((255, 255, 255))

        # Draw grid border
        pygame.draw.rect(WINDOW, (0, 0, 0), (50, 50, GRID_WIDTH * GRID_SIZE, GRID_HEIGHT * GRID_SIZE), BORDER_SIZE)

        # Draw grid
        for x in range(50 + GRID_SIZE, 50 + GRID_WIDTH * GRID_SIZE, GRID_SIZE):
            pygame.draw.line(WINDOW, (0, 0, 0), (x, 50), (x, 50 + GRID_HEIGHT * GRID_SIZE - 1), BORDER_SIZE)
        for y in range(50 + GRID_SIZE, 50 + GRID_HEIGHT * GRID_SIZE, GRID_SIZE):
            pygame.draw.line(WINDOW, (0, 0, 0), (50, y), (50 + GRID_WIDTH * GRID_SIZE - 1, y), BORDER_SIZE)

        # Draw players
        WINDOW.blit(player_image, (player1_x * GRID_SIZE + 50, player1_y * GRID_SIZE + 50))
        WINDOW.blit(opponent_image, (player2_x * GRID_SIZE + 50, player2_y * GRID_SIZE + 50))

        pygame.display.update()

# Run the game
if __name__ == "__main__":
    main()
