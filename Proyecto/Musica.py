#Módulo que permite la reproducción de audio
from pygame import mixer
import time

#Función que inicializa la reproducción de música
def init():
    mixer.init(buffer=4096)

#Reproductor de canciones
def Gatita():
    mixer.music.load('/home/Gaboo/Music/Gatita.mp3')
    mixer.music.play()

#Reproductor de canciones
def Cochinae():
    mixer.music.load('/home/Gaboo/Music/Cochinae.mp3')
    mixer.music.play()

#Reproductor de canciones
def Titi():
    mixer.music.load('/home/Gaboo/Music/Tití.mp3')
    mixer.music.play()

#Función que permite la detención de la música
def stop():
    mixer.music.stop()
