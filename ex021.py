import pygame

pygame.init()   

pygame.mixer.music.load('teste.mp3')
pygame.mixer.music.play()
pygame.event.wait()  # Wait for the music to finish playing




