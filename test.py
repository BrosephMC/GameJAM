import pygame
import sys

# Initialize Pygame
pygame.init()

# Set up the window
WIDTH, HEIGHT = 800, 600
WINDOW = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Text Bubbles")

# Colors
WHITE = (255, 255, 255)
GRAY = (200, 200, 200)
RED = (255, 0, 0)

# Font
font = pygame.font.Font(None, 20)  # Adjusted font size

# Bubble properties
bubble_width = int(200 * 0.9)  # Decreased width by 10%
bubble_height = int(100 * 0.9)  # Decreased height by 10%
bubble_offset = 8  # Reduced offset

# Main game loop
def main():
    running = True
    highlighted_bubble = None

    while running:
        # Handle events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_w:
                    highlighted_bubble = 1
                elif event.key == pygame.K_a:
                    highlighted_bubble = 2
                elif event.key == pygame.K_s:
                    highlighted_bubble = 3
                elif event.key == pygame.K_d:
                    highlighted_bubble = 4

        # Draw background
        WINDOW.fill(WHITE)

        # Draw text bubbles
        x_center = WIDTH // 2
        y_center = HEIGHT // 2

        bubble_positions = [
            (x_center, y_center - (bubble_height + bubble_offset)),    # Top bubble
            (x_center - (bubble_width + bubble_offset), y_center),     # Left bubble
            (x_center, y_center),                                      # Center bubble
            (x_center + (bubble_width + bubble_offset), y_center)      # Right bubble
        ]

        # Draw text bubbles
        for i, (x, y) in enumerate(bubble_positions):
            # Check if bubble should be highlighted
            if i + 1 == highlighted_bubble:
                pygame.draw.rect(WINDOW, RED, (x, y, bubble_width, bubble_height), border_radius=20)  # Adjusted border radius
            else:
                pygame.draw.rect(WINDOW, GRAY, (x, y, bubble_width, bubble_height), border_radius=20)  # Adjusted border radius

            # Draw text
            text_surface = font.render("Bubble {}".format(i+1), True, (0, 0, 0))
            text_rect = text_surface.get_rect(center=(x + bubble_width // 2, y + bubble_height // 2))
            WINDOW.blit(text_surface, text_rect)

        pygame.display.update()

# Run the game
if __name__ == "__main__":
    main()
