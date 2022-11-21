from gpiozero import LightSensor, LED
from signal import pause

sensor = LightSensor(18)
led = LED(17)

sensor.when_dark = led.on
sensor.when_light = led.off

pause()