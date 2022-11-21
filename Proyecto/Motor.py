from gpiozero import Motor
from time import sleep

motor = Motor(forward = 14, backward = 4)

while True:
    motor.forward()
    sleep(5)
    motor.backward()
    sleep(5)
    motor.stop()
    sleep(5)
