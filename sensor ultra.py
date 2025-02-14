from gpiozero import DistanceSensor
from time import sleep

sensor = DistanceSensor(23, 24)

while True:
	print( sensor.distance)
	sleep(1)

import RPi.GPIO as GPIO
import time
TRIG = 23
ECHO = 24
GPIO.setmode(GPIO.BCM)
GPIO.setup(TRIG, GPIO.OUT)
GPIO.setup(ECHO, GPIO.IN)

try:
    while True:
        GPIO.output(TRIG, GPIO.LOW)
        time.sleep(0.5)
        GPIO.output(TRIG, GPIO.HIGH)
        time.sleep(0.00001)
        GPIO.output(TRIG, GPIO.LOW)

    while True:
        pulso_inicio = time.time()
        if GPIO.input(ECHO) == GPIO.HIGH:
            break
    while True:
        pulso_fin = time.time()
        if GPIO.input(ECHO) == GPIO.LOW:
            break
    duracion = pulso_fin - pulso_inicio
    distancia = (34300 * duracion) / 2
    print( "Distancia: %.2f cm" % distancia)
finally:
GPIO.cleanup()
