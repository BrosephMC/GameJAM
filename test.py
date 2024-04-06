import pygame

# Initialize Pygame
pygame.init()

# Screen dimensions
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

# Grid dimensions
GRID_WIDTH = 10
GRID_HEIGHT = 10

# Cell size
CELL_SIZE = 50

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GRAY = (200, 200, 200)
RED = (255, 0, 0)
BLUE = (0, 0, 255)

# Create the screen
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Two Player Game Grid")

# Player positions
player1_pos = [0, 0]  # Player 1 starting position (top left corner)
player2_pos = [GRID_WIDTH - 1, GRID_HEIGHT - 1]  # Player 2 starting position (bottom right corner)

# Player movements
player1_movement = [0, 0]
player2_movement = [0, 0]

# Main function
def main():
    # Main loop
    running = True
    while running:
        # Event handling
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_w:
                    player1_movement[1] = -1
                elif event.key == pygame.K_s:
                    player1_movement[1] = 1
                elif event.key == pygame.K_a:
                    player1_movement[0] = -1
                elif event.key == pygame.K_d:
                    player1_movement[0] = 1
                elif event.key == pygame.K_UP:
                    player2_movement[1] = -1
                elif event.key == pygame.K_DOWN:
                    player2_movement[1] = 1
                elif event.key == pygame.K_LEFT:
                    player2_movement[0] = -1
                elif event.key == pygame.K_RIGHT:
                    player2_movement[0] = 1
            elif event.type == pygame.KEYUP:
                if event.key == pygame.K_w or event.key == pygame.K_s:
                    player1_movement[1] = 0
                elif event.key == pygame.K_a or event.key == pygame.K_d:
                    player1_movement[0] = 0
                elif event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                    player2_movement[1] = 0
                elif event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                    player2_movement[0] = 0

        # Update player positions
        update_player_position(player1_pos, player1_movement)
        update_player_position(player2_pos, player2_movement)

        # Draw grid and players
        screen.fill(WHITE)
        draw_grid()
        draw_player(player1_pos, RED)
        draw_player(player2_pos, BLUE)

        pygame.display.flip()

    pygame.quit()

# Function to draw the grid
def draw_grid():
    for x in range(0, SCREEN_WIDTH, CELL_SIZE):
        pygame.draw.line(screen, GRAY, (x, 0), (x, SCREEN_HEIGHT))
    for y in range(0, SCREEN_HEIGHT, CELL_SIZE):
        pygame.draw.line(screen, GRAY, (0, y), (SCREEN_WIDTH, y))

# Function to draw a player
def draw_player(pos, color):
    x = pos[0] * CELL_SIZE
    y = pos[1] * CELL_SIZE
    pygame.draw.rect(screen, color, (x, y, CELL_SIZE, CELL_SIZE))

# Function to update player position
def update_player_position(pos, movement):
    pos[0] += movement[0]
    pos[1] += movement[1]
    # Ensure the player does not move beyond the grid boundaries
    pos[0] = max(0, min(pos[0], GRID_WIDTH - 1))
    pos[1] = max(0, min(pos[1], GRID_HEIGHT - 1))

# Run the main function
if __name__ == "__main__":
    main()
