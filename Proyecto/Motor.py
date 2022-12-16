from gpiozero import Motor
from time import  sleep

motor = Motor(forward=14, backward=15)

def encender():
    motor.forward()
    
def apagar():
    motor.stop()
    