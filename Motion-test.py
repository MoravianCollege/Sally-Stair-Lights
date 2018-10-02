import time
import RPi.GPIO as GPIO

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)
GPIO.setup(7, GPIO.IN)
GPIO.setup(3, GPIO.OUT)

while True:
        i=GPIO.input(7)
        if i==0:
                print ("No Movement", i)
                GPIO.output(3,0)
                time.sleep(1)
        elif i==1:
                print ("Movement Detected ,i)
                GPIO.output(3,1)
                time.sleep(1)
