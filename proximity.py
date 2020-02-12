import time
from gpiozero import DistanceSensor

sensor = DistanceSensor(trigger=5, echo=6)

while True:
    print(f'Distance : {sensor.distance * 100} cm', end='\n')
    time.sleep(1)


