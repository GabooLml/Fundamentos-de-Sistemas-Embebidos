from gpiozero import DistanceSensor, LED
from signal import pause

sensor = DistanceSensor(23, 24, max_distance = 10, threshold_distance = 0.2)
led = LED(16)

sensor.when_in_range = led.on
sensor.when_out_of_range = led.off
print('Distancia: ', sensor.distance * 100)

pause()
