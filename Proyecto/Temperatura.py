"""Librerías que permiten el uso de los módulos del sensor DHT11 (Temperatura),
el módulo del LCD y el motor (ventilador).
"""
import time
import Adafruit_DHT
import I2C_LCD_driver
import Motor
import os

#GPIO que permite el funcionamiento del sensor DHT11
pin = 4

#Instancia para el sensor de temperatura
sensor = Adafruit_DHT.DHT11

#Instancia para el LCD
LCD = I2C_LCD_driver.lcd()

#Instancia para el ventilador
motor = Motor

#Variable para validar el funcionamiento del ventilador
state = False

while True:
    #Variables que capturan la información de la lectura del sensor
    humedad, temperatura = Adafruit_DHT.read(sensor, pin)
    
    #Validación de que los valores no sean nulos
    if humedad is not None and temperatura is not None:
        
        #Impresión de los valores retornados
        print("Temp={0:0.1f} C Humedad={1:0.1f}%".format(temperatura, humedad))
        LCD.lcd_display_string("Temp:{0:0.0f}Casagr".format(temperatura))
        LCD.lcd_display_string("Hume:{0:0.0f}%".format(humedad),2)
        
        #Validación de que la temperatura no rebase los 25°
        if temperatura >= 25:
            
            #Validación que la alerta ya fue emitida una vez y el ventilador ya fue encendido
            if state == False:
                
                #Encendido del ventilador
                motor.encender()
                os.system('sudo sh /home/Gaboo/Proyecto/Scripts/Ventilador.sh')
                state = True
        else:
            
            #Apagado del ventilador
            motor.apagar()
            state = False
    else:
        print("Falla");
    time.sleep(3); 
