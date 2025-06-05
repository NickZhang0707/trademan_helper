

import pygame

# Initialize pygame mixer
pygame.mixer.init()

# Load music file (better for long audio)
pygame.mixer.music.load('./train-horn-337875.mp3')  # Replace with your file

# Play music in a loop (-1 means infinite loop)
pygame.mixer.music.play(-1)

# Keep the program running (press Ctrl+C to stop)
try:
    while True:
        pygame.time.wait(1000)
except KeyboardInterrupt:
    pygame.mixer.music.stop()