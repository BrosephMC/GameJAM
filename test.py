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

# Rendering settings
WHITE = (255, 255, 255)
GRAY = (200, 200, 200)
RED = (255, 0, 0)
BLACK = (0, 0, 0)  # Define BLACK color

FONT = pygame.font.SysFont(None, 30)

# Load player and opponent images
player_image = pygame.image.load('images/player.png').convert_alpha()
player_image = pygame.transform.scale(player_image, (GRID_SIZE, GRID_SIZE))
opponent_image = pygame.image.load('images/opponent.png').convert_alpha()
opponent_image = pygame.transform.scale(opponent_image, (GRID_SIZE, GRID_SIZE))
player_turn = 1

# Rotate player images
player_images = [pygame.transform.rotate(player_image, angle) for angle in (0, 90, 180, 270)]
opponent_images = [pygame.transform.rotate(opponent_image, angle) for angle in (0, 90, 180, 270)]

# Colors
WHITE = (255, 255, 255)
GRAY = (200, 200, 200)
RED = (255, 0, 0)
BLACK = (0, 0, 0)  # Define BLACK color

# Font
font = pygame.font.Font(None, 20)  # Adjusted font size

# Bubble properties
bubble_width = int(100 * 0.9)  # Decreased width by 10%
bubble_height = int(50 * 0.9)  # Decreased height by 10%
bubble_offset = 8  # Reduced offset

# Player class
class Player:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.direction = 0

    def set_rotation(self, dx, dy):
        if dx > 0:
            self.direction = 1
        elif dx < 0:
            self.direction = 3
        elif dy > 0:
            self.direction = 0
        elif dy < 0:
            self.direction = 2

    def move(self, dx, dy, other_player):
        self.set_rotation(dx, dy)

        if 0 <= self.x + dx < GRID_WIDTH and 0 <= self.y + dy < GRID_HEIGHT and not (self.x + dx == other_player.x and self.y + dy == other_player.y):
            self.x += dx
            self.y += dy
            self.finish_turn()

    def finish_turn(self):
        global player_turn
        if player_turn == 1:
            player_turn = 2
        elif player_turn == 2:
            player_turn = 1

# Main game loop
def main():
    player1 = Player(0, 0)
    player2 = Player(GRID_WIDTH - 1, GRID_HEIGHT - 1)
    move_speed = 1  # Number of squares the player moves at a time

    # Clock variable
    start_time = pygame.time.get_ticks()  # Get the time when the program starts
    running = True
    highlighted_bubble = None
    
    while running:

        # Handle events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                
                # Player 1 movement with WASD
                if player_turn == 1:
                    if event.key == pygame.K_a:
                        player1.move(-move_speed, 0, player2)
                        highlighted_bubble = 1
                    elif event.key == pygame.K_d:
                        player1.move(move_speed, 0, player2)
                        highlighted_bubble = 3
                    elif event.key == pygame.K_w:
                        player1.move(0, -move_speed, player2)
                        highlighted_bubble = 4
                    elif event.key == pygame.K_s:
                        player1.move(0, move_speed, player2)
                        highlighted_bubble = 2

                elif player_turn == 2:
                    # Player 2 movement with arrow keys
                    if event.key == pygame.K_LEFT:
                        player2.move(-move_speed, 0, player1)
                        highlighted_bubble = 1
                    elif event.key == pygame.K_RIGHT:
                        player2.move(move_speed, 0, player1)
                        highlighted_bubble = 3
                    elif event.key == pygame.K_UP:
                        player2.move(0, -move_speed, player1)
                        highlighted_bubble = 4
                    elif event.key == pygame.K_DOWN:
                        player2.move(0, move_speed, player1)
                        highlighted_bubble = 2

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
        WINDOW.blit(player_images[player1.direction], (player1.x * GRID_SIZE + 50, player1.y * GRID_SIZE + 50))
        WINDOW.blit(opponent_images[player2.direction], (player2.x * GRID_SIZE + 50, player2.y * GRID_SIZE + 50))

        # Draw text bubbles
        bubble_positions = [
            (50 + GRID_WIDTH * GRID_SIZE // 4 - bubble_width // 2, HEIGHT - 50 - bubble_height - 20), # A bubble
            (50 + 2 * GRID_WIDTH * GRID_SIZE // 4 - bubble_width // 2, HEIGHT - 50 - bubble_height - 20), # W bubble
            (50 + 3 * GRID_WIDTH * GRID_SIZE // 4 - bubble_width // 2, HEIGHT - 50 - bubble_height - 20), # S bubble
            (50 + GRID_WIDTH * GRID_SIZE // 2 - bubble_width // 2, HEIGHT - 50 - 2 * bubble_height - 40), # D bubble
        ]

        for i, (x, y) in enumerate(bubble_positions):
            # Check if bubble should be highlighted
            if i + 1 == highlighted_bubble:
                pygame.draw.rect(WINDOW, RED, (x, y, bubble_width, bubble_height), border_radius=20)
            else:
                pygame.draw.rect(WINDOW, GRAY, (x, y, bubble_width, bubble_height), border_radius=20)

            # Draw text
            text_surface = font.render("ASDW"[i], True, BLACK)  # Render the text with variable value
            text_rect = text_surface.get_rect(center=(x + bubble_width // 2, y + bubble_height // 2))
            WINDOW.blit(text_surface, text_rect)

        # Clock
        # Calculate elapsed time
        elapsed_time = (pygame.time.get_ticks() - start_time) // 1000  # Convert milliseconds to seconds
        # Draw timer overlay
        timer_surface = pygame.Surface((200, 50), pygame.SRCALPHA)
        timer_text = FONT.render(f"Time: {elapsed_time}s", True, BLACK)
        timer_surface.blit(timer_text, (5, 5))
        WINDOW.blit(timer_surface, (5, 5))  # Position the timer overlay

        text_surface = FONT.render("Player Turn: " + str(player_turn), True, BLACK)  # Render the text with variable value
        WINDOW.blit(text_surface, (300, 5))  # Blit the text surface onto the window

        pygame.display.update()

# Run the game
if __name__ == "__main__":
    main()
