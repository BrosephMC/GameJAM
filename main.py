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

#initialize background image
background_image = pygame.image.load("images/grass.jpg").convert()
background_image = pygame.transform.scale(background_image, (WIDTH, HEIGHT))

#Rendering settings
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
DARKRED = (144, 11, 10)
RED = (212, 14, 0)
ORANGE = (212, 106, 0)
YELLOW = (212, 187, 0)
FONT = pygame.font.SysFont(None, 30)

# Load player and opponent images
player_image = pygame.image.load('images/player.png').convert_alpha()
player_image = pygame.transform.scale(player_image, (GRID_SIZE, GRID_SIZE))
opponent_image = pygame.image.load('images/opponent.png').convert_alpha()
opponent_image = pygame.transform.scale(opponent_image, (GRID_SIZE, GRID_SIZE))
player_turn = 1

# Load player number images
one_image = pygame.image.load('images/1.png').convert_alpha()
one_image = pygame.transform.scale(one_image, (30, 40))
two_image = pygame.image.load('images/2.png').convert_alpha()
two_image = pygame.transform.scale(two_image, (30, 40))

# Rotate player images
player_images = [pygame.transform.rotate(player_image, angle) for angle in (0, 90, 180, 270)]
opponent_images = [pygame.transform.rotate(opponent_image, angle) for angle in (0, 90, 180, 270)]

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
                if player_turn == 1:
                    if event.key == pygame.K_a:
                        player1.move(-move_speed, 0, player2)
                    elif event.key == pygame.K_d:
                        player1.move(move_speed, 0, player2)
                    elif event.key == pygame.K_w:
                        player1.move(0, -move_speed, player2)
                    elif event.key == pygame.K_s:
                        player1.move(0, move_speed, player2)

                elif player_turn == 2:
                    # Player 2 movement with arrow keys
                    if event.key == pygame.K_LEFT:
                        player2.move(-move_speed, 0, player1)
                    elif event.key == pygame.K_RIGHT:
                        player2.move(move_speed, 0, player1)
                    elif event.key == pygame.K_UP:
                        player2.move(0, -move_speed, player1)
                    elif event.key == pygame.K_DOWN:
                        player2.move(0, move_speed, player1)

        # Draw background
        # WINDOW.fill(WHITE)
        WINDOW.blit(background_image, (0, 0))
        
        # Draw grid border
        #pygame.draw.rect(WINDOW, DARKRED, (0, 0, GRID_WIDTH * GRID_SIZE + 120, GRID_HEIGHT * GRID_SIZE + 100), 50)
        #pygame.draw.rect(WINDOW, RED, (20, 20, GRID_WIDTH * GRID_SIZE + 60, GRID_HEIGHT * GRID_SIZE + 60), 10)
        #pygame.draw.rect(WINDOW, DARKRED, (30, 30, GRID_WIDTH * GRID_SIZE + 40, GRID_HEIGHT * GRID_SIZE + 40), 10)
        #pygame.draw.rect(WINDOW, RED, (40, 40, GRID_WIDTH * GRID_SIZE + 20, GRID_HEIGHT * GRID_SIZE + 20), 10)
        pygame.draw.rect(WINDOW, BLACK, (50, 50, GRID_WIDTH * GRID_SIZE, GRID_HEIGHT * GRID_SIZE), BORDER_SIZE)
        
        

        # Draw grid
        for x in range(50 + GRID_SIZE, 50 + GRID_WIDTH * GRID_SIZE, GRID_SIZE):
            pygame.draw.line(WINDOW, BLACK, (x, 50), (x, 50 + GRID_HEIGHT * GRID_SIZE - 1), BORDER_SIZE)
        for y in range(50 + GRID_SIZE, 50 + GRID_HEIGHT * GRID_SIZE, GRID_SIZE):
            pygame.draw.line(WINDOW, BLACK, (50, y), (50 + GRID_WIDTH * GRID_SIZE - 1, y), BORDER_SIZE)

        # Draw players
        #WINDOW.blit(player_image, (player1.x * GRID_SIZE + 50, player1.y * GRID_SIZE + 50))
        #WINDOW.blit(opponent_image, (player2.x * GRID_SIZE + 50, player2.y * GRID_SIZE + 50))
        # Draw players with rotation
        WINDOW.blit(player_images[player1.direction], (player1.x * GRID_SIZE + 50, player1.y * GRID_SIZE + 50))
        WINDOW.blit(opponent_images[player2.direction], (player2.x * GRID_SIZE + 50, player2.y * GRID_SIZE + 50))

        #clock
        #####RESETS WHEN PLAYER ENDS TURN
        # Calculate elapsed time
        elapsed_time = (pygame.time.get_ticks() - start_time) // 1000  # Convert milliseconds to seconds
        # Draw timer overlay
        timer_surface = pygame.Surface((120, 30), pygame.SRCALPHA)
        timer_surface.fill((0, 0, 0, 128))  # Semi-transparent black background
        timer_text = FONT.render(f"Time: {elapsed_time}s", True, WHITE)
        timer_surface.blit(timer_text, (5, 5))
        WINDOW.blit(timer_surface, (5, 5))  # Position the timer overlay

        if player_turn == 1:
            WINDOW.blit(one_image, (450, 5))
        else:
            WINDOW.blit(two_image, (450, 5))
        
        #text_surface = FONT.render("Player Turn: " + str(player_turn), True, WHITE)  # Render the text with variable value
        #WINDOW.blit(text_surface, (300, 10))  # Blit the text surface onto the window

        pygame.display.update()

# Run the game
if __name__ == "__main__":
    main()