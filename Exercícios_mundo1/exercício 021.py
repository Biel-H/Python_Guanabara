#faça um programa em python que abra e reproduza o áudio de um arquivo MP3.
from platform import python_branch
import winsound
winsound.PlaySound('SystemExit', winsound.SND_ALIAS)

#Ou usando o pygame

import pygame
pygame.init()
pygame.mixer.music.load('Exemplo.mp3')
pygame.mixer.play()
pygame.event.wait()

