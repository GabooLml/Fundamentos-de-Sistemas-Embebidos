import time
import Adafruit_DHT
import I2C_LCD_driver
import Motor
import os

pin = 4
sensor = Adafruit_DHT.DHT11
LCD = I2C_LCD_driver.lcd()
motor = Motor
state = False

while True:
    humedad, temperatura = Adafruit_DHT.read(sensor, pin)
    if humedad is not None and temperatura is not None:
        print("Temp={0:0.1f} C Humedad={1:0.1f}%".format(temperatura, humedad))
        LCD.lcd_display_string("Temp:{0:0.0f}Casagr".format(temperatura))
        LCD.lcd_display_string("Hume:{0:0.0f}%".format(humedad),2)
        if temperatura >= 25:
            if state == False:
                motor.encender()
                os.system('sudo sh /home/Gaboo/Proyecto/Scripts/Ventilador.sh')
                state = True
        else:
            motor.apagar()
            state = False
    else:
        print("Falla");
    time.sleep(3); 
