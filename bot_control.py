import gpiozero as gpio
import math
import time
import board
import busio
from adafruit_lsm6ds import LSM6DSOX


#setup the gyroscope sensor using i2c
i2c = busio.I2C(board.SCL, board.SDA)
gyro_sensor = LSM6DSOX(i2c)


#ultra sonic distance sensor setup
dist_sensor = gpio.DistanceSensor(trigger=5, echo=6, max_distance=3)


#function to return the current distance of object in the proximity
# of the sensor, in centimeters
def distance():
    global dist_sensor
    return dist_sensor.distance * 100


# motor wheel constants
WHEEL_DIAMETER = 67.9  # diameter of the wheel in millimeters
STEP_COUNT = 20.0  # number of slots in the wheel speed encoder ring


# pulse counters for speed sensors
counter_right = 0
counter_left = 0


# right speed pulse counter event
def ev_right_count():
    global counter_right
    counter_right += 1


# left speed pulse counter event
def ev_left_count():
    global counter_left
    counter_left += 1


# Motor gpio setup (forward pin, backward pin)
right_motors = gpio.Motor(17, 27)
left_motors = gpio.Motor(24, 23)

# speed encoder sensor setup
right_speed = gpio.DigitalInputDevice(25)
left_speed = gpio.DigitalInputDevice(22)
right_speed.when_activated = ev_right_count  # event
left_speed.when_activated = ev_left_count  # event


def counter_reset():
    global counter_right, counter_left
    counter_right = 0
    counter_left = 0


# converts centimeters to the number of steps required by
# the wheel to cover the distance provided in centimeters
# 1 step = 1 slot on the encoder wheel
def cm_to_steps(cm):
    circumference = (WHEEL_DIAMETER * math.pi) / 10  # divide by 10 to go from mm to cm
    steps = cm / (circumference / STEP_COUNT)  # steps required to travel the given cm distance
    return int(steps)  # return the number of steps as integer


# stop all motors
def stop():
    left_motors.stop()
    right_motors.stop()


# skid steer LEFT with a speed between 0-1 (default = 1)
def left(speed=1):
    currentRotation = gyro_sensor.gyro[2]  # DID NOT TEST THIS YET!
    left_motors.backward(speed)
    right_motors.forward(speed)
    while currentRotation 





# skid steer RIGHT with a speed between 0-1 (default = 1)
def right(speed=1):
    left_motors.forward(speed)
    right_motors.backward(speed)


# move forward by centimeters given at a given speed between 0-1
def forward(cm, speed=1):
    steps = cm_to_steps(cm)  # get the number of steps required for the given cm
    counter_reset()
    left_motors.forward(speed)
    right_motors.forward(speed)
    while counter_left < steps or counter_right < steps:
        print("left counter:" + str(counter_left) + "\r\n"),
        print("right counter:" + str(counter_right) + "\r\n"),
    stop()
    # reset counters
    counter_reset()


# move forward by centimeters given at a given speed between 0-1
def backward(cm, speed=1):
    steps = cm_to_steps(cm)  # get the number of steps required for the given cm
    counter_reset()
    left_motors.backward(speed)
    right_motors.backward(speed)
    while counter_left < steps or counter_right < steps:
        print("left counter:" + str(counter_left) + "\r\n"),
        print("right counter:" + str(counter_right) + "\r\n"),
    stop()
    # reset counters
    counter_reset()

