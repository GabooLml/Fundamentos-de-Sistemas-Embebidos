from pygame import mixer
import time

def init():
    mixer.init(buffer=4096)

def Gatita():
    mixer.music.load('/home/Gaboo/Music/Gatita.mp3')
    mixer.music.play()
    
def Cochinae():
    mixer.music.load('/home/Gaboo/Music/Cochinae.mp3')
    mixer.music.play()
    
def Titi():
    mixer.music.load('/home/Gaboo/Music/Tití.mp3')
    mixer.music.play()

def stop():
    mixer.music.stop()
