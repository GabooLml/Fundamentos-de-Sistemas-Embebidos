#Módulo que permite el funcionamiento de un motor DC
from gpiozero import Motor
from time import  sleep

#Instancia para el control del motor
motor = Motor(forward=14, backward=15)

#Función que hace andar el ventilador
def encender():
    motor.forward()

#Función que detiene el ventilador
def apagar():
    motor.stop()
    