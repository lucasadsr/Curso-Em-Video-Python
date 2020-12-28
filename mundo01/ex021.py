# Faça um programa que abra e reproduza o áudio de um arquivo MP3.

from pygame import mixer
mixer.init()
mixer.music.load('musica.mp3')
mixer.music.play()
import time
time.sleep(360)
