import pygame
import sys

# Initialize Pygame
pygame.init()

# Set up the window
WIDTH, HEIGHT = 640, 480
WINDOW = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Timer Overlay Example")

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

# Font
FONT = pygame.font.SysFont(None, 30)

# Main game loop
def main():
    running = True
    start_time = pygame.time.get_ticks()  # Get the time when the program starts

    while running:
        # Handle events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        #########################
        # Calculate elapsed time
        elapsed_time = (pygame.time.get_ticks() - start_time) // 1000  # Convert milliseconds to seconds
        #########################
        
        # Draw main content
        WINDOW.fill(WHITE)
        pygame.draw.circle(WINDOW, BLACK, (WIDTH // 2, HEIGHT // 2), 200)

        #########################
        # Draw timer overlay
        timer_surface = pygame.Surface((200, 50), pygame.SRCALPHA)
        timer_surface.fill((0, 0, 0, 128))  # Semi-transparent black background
        timer_text = FONT.render(f"Time: {elapsed_time}s", True, WHITE)
        timer_surface.blit(timer_text, (10, 10))
        WINDOW.blit(timer_surface, (10, 10))  # Position the timer overlay
        #########################
        
        pygame.display.update()

# Run the game
if __name__ == "__main__":
    main()
