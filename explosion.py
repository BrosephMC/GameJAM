import pygame
import sys

# Initialize Pygame
pygame.init()

# Set up the window
WIDTH, HEIGHT = 800, 600
WINDOW = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Explosion Animation")

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
YELLOW = (255, 255, 0)
ORANGE = (255, 165, 0)
RED = (255, 0, 0)

# Explosion animation parameters
explosion_radius = 20
explosion_duration = 20
explosion_speed = 1

# Main game loop
def main():
    explosion_center = (WIDTH // 2, HEIGHT // 2)
    explosion_frame = 0

    running = True
    clock = pygame.time.Clock()

    while running:
        # Handle events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        # Draw explosion frame
        WINDOW.fill(BLACK)  # Clear the window

        if explosion_frame < explosion_duration:
            pygame.draw.circle(WINDOW, YELLOW, explosion_center, explosion_frame * explosion_speed)
            pygame.draw.circle(WINDOW, ORANGE, explosion_center, explosion_frame * explosion_speed - 10)
            pygame.draw.circle(WINDOW, RED, explosion_center, explosion_frame * explosion_speed - 20)
            explosion_frame += 1
        else:
            # Reset explosion animation
            explosion_frame = 0

        pygame.display.update()
        clock.tick(30)  # Cap the frame rate at 30 FPS

# Run the game
if __name__ == "__main__":
    main()
