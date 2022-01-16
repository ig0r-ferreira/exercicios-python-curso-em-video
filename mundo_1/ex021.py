# Algoritmo que abre e reproduz o áudio de um arquivo MP3.

import pygame

pygame.mixer.init()
pygame.mixer.music.load('musica.mp3')
pygame.mixer.music.play()

pygame.init()
pygame.event.wait()
