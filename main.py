import pygame
import sys

# Initialize Pygame
pygame.init()

# Set up the window
WIDTH, HEIGHT = 700, 500
GRID_SIZE = 100
GRID_WIDTH, GRID_HEIGHT = WIDTH // GRID_SIZE, HEIGHT // GRID_SIZE
WINDOW = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Grid Movement Game")

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

# Font
FONT = pygame.font.SysFont(None, 30)

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

    #clock variable
    start_time = pygame.time.get_ticks()  # Get the time when the program starts
    
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

        # Draw grid
        WINDOW.fill((255, 255, 255))
        for x in range(0, WIDTH, GRID_SIZE):
            pygame.draw.line(WINDOW, (0, 0, 0), (x, 0), (x, HEIGHT))
        for y in range(0, HEIGHT, GRID_SIZE):
            pygame.draw.line(WINDOW, (0, 0, 0), (0, y), (WIDTH, y))

        # Draw players
        WINDOW.blit(player_image, (player1_x * GRID_SIZE, player1_y * GRID_SIZE))
        WINDOW.blit(opponent_image, (player2_x * GRID_SIZE, player2_y * GRID_SIZE))

        #clock
        # Calculate elapsed time
        elapsed_time = (pygame.time.get_ticks() - start_time) // 1000  # Convert milliseconds to seconds
        # Draw timer overlay
        timer_surface = pygame.Surface((200, 50), pygame.SRCALPHA)
        #timer_surface.fill((0, 0, 0, 128))  # Semi-transparent black background
        timer_text = FONT.render(f"Time: {elapsed_time}s", True, BLACK)
        timer_surface.blit(timer_text, (5, 5))
        WINDOW.blit(timer_surface, (5, 5))  # Position the timer overlay
        
        pygame.display.update()

# Run the game
if __name__ == "__main__":
    main()
