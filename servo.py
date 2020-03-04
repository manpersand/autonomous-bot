# Import libraries
import RPi.GPIO as GPIO
import time

# Set GPIO numbering mode
GPIO.setmode(GPIO.BCM)

GPIO.setwarnings(False)

# Set pin 7 as an output, and set servo1 as pin 7 as PWM
pin = 7
GPIO.setup(pin,GPIO.OUT)
servo1 = GPIO.PWM(pin,50) # Note 7 is pin, 50 = 50Hz pulse

#start PWM running, but with value of 0 (pulse off)
servo1.start(0)

#180 degrees
def left():
    servo1.ChangeDutyCycle(12)
    time.sleep(0.5)
    servo1.ChangeDutyCycle(0)

#90 degrees
def front():
    servo1.ChangeDutyCycle(7)
    time.sleep(0.5)
    servo1.ChangeDutyCycle(0)

#0 degrees
def right():
    servo1.ChangeDutyCycle(2)
    time.sleep(0.5)
    servo1.ChangeDutyCycle(0)

#Clean things up at the end
def cleanup():
    servo1.stop()
    GPIO.cleanup()

