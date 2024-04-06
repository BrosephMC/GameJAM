import pygame

# Initialize Pygame
pygame.init()

# Set the screen dimensions (not necessary for audio)
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Audio Playback Example")

# Load the audio file
pygame.mixer.music.load("audio/punch.mp3")

# Play the audio
pygame.mixer.music.play()

# Main loop to keep the program running
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

# Quit Pygame
pygame.quit()
