# Importamos la paquteria necesaria
import RPi.GPIO as GPIO
import time
import os

TRIG = 23 #Variable que contiene el GPIO al cual conectamos la señal TRIG del sensor
ECHO = 24 #Variable que contiene el GPIO al cual conectamos la señal ECHO del sensor
LED = 17 #Variable que contiene el GPIO al cual conectamos la señal LED

GPIO.setmode(GPIO.BCM)     #Establecemos el modo según el cual nos refiriremos a los GPIO de nuestra RPi
GPIO.setup(TRIG, GPIO.OUT) #Configuramos el pin TRIG como una salida
GPIO.setup(ECHO, GPIO.IN)  #Configuramos el pin ECHO como una salida
GPIO.setup(LED, GPIO.OUT)  #Configuramos el pin LED como una salida

#Contenemos el código principal en un estructura try para limpiar los GPIO al terminar o presentarse un error
try:
    #Implementamos un loop infinito
    while True:

        # Ponemos en bajo el pin TRIG y después esperamos 0.5 seg para que el transductor se estabilice
        GPIO.output(TRIG, GPIO.LOW)
        time.sleep(0.5)

        #Ponemos en alto el pin TRIG esperamos 10 uS antes de ponerlo en bajo
        GPIO.output(TRIG, GPIO.HIGH)
        time.sleep(0.00001)
        GPIO.output(TRIG, GPIO.LOW)

        # En este momento el sensor envía 8 pulsos ultrasónicos de 40kHz y coloca su pin ECHO en alto
        # Debemos detectar dicho evento para iniciar la medición del tiempo

        while True:
            pulso_inicio = time.time()
            if GPIO.input(ECHO) == GPIO.HIGH:
                break

        # El pin ECHO se mantendrá en HIGH hasta recibir el eco rebotado por el obstáculo.
        # En ese momento el sensor pondrá el pin ECHO en bajo.
    # Prodedemos a detectar dicho evento para terminar la medición del tiempo

        while True:
            pulso_fin = time.time()
            if GPIO.input(ECHO) == GPIO.LOW:
                break

        # Tiempo medido en segundos
        duracion = pulso_fin - pulso_inicio

        #Obtenemos la distancia considerando que la señal recorre dos veces la distancia a medir y que la velocidad del sonido es 343m/s
        distancia = (34300 * duracion) / 2

        if distancia < 30.00:
            # Se enciende el LED como alarma
            GPIO.output(LED, GPIO.HIGH)
            # Imprimimos resultado
            print( "Distancia: %.2f cm" % distancia)
            #Se manda la alerta
            os.system('sudo sh /home/Gaboo/Proyecto/Scripts/Alerta.sh')
            time.sleep(15)
        else:
            # Se apaga el LED de la alarma
            GPIO.output(LED, GPIO.LOW)

finally:
    # Reiniciamos todos los canales de GPIO.
    GPIO.cleanup()
