import gpiozero as gpio
import math
import proximity
import gyro

# motor wheel constants
WHEEL_DIAMETER = 63.9  # diameter of the wheel in millimeters
STEP_COUNT = 20.0  # number of slots in the wheel speed encoder ring

# Motor gpio setup (forward pin, backward pin)
right_motors = gpio.Motor(17, 27)
left_motors = gpio.Motor(24, 23)

# speed encoder sensor setup
right_speed = gpio.DigitalInputDevice(25)
left_speed = gpio.DigitalInputDevice(22)
right_speed.when_activated = ev_right_count  # event
left_speed.when_activated = ev_left_count  # event

# pulse counters for speed sensors
counter_right = 0
counter_left = 0


# right speed pulse counter event
def ev_right_count():
    counter_right += 1


# left speed pulse counter event
def ev_left_count():
    counter_left += 1


def counter_reset():
    counter_right = 0
    counter_left = 0


# converts centimeters to the number of steps required by
# the wheel to cover the distance provided in centimeters
# 1 step = 1 slot on the encoder wheel
def cm_to_steps(cm):
    circumference = (WHEEL_DIAMETER * math.pi) / 10  # divide by 10 to go from mm to cm
    steps = (circumference / STEP_COUNT) * cm  # steps required to travel the given cm distance
    return int(steps)  # return the number of steps as integer


# move forward by centimeters given at a given speed between 0-1
def forward(cm, speed=1):
    steps = cm_to_steps(cm)  # get the number of steps required for the given cm
    while counter_left < steps and counter_right < steps:
        forward(speed)
    stop()
    # reset counters
    counter_reset()


# move forward by centimeters given at a given speed between 0-1
def backward(cm, speed=1):
    steps = cm_to_steps(cm)  # get the number of steps required for the given cm
    while counter_left < steps and counter_right < steps:
        backward(speed)
    stop()
    # reset counters
    counter_reset()


# move forward with a speed between 0-1 (default = 1)
def forward(speed=1):
    left_motors.forward(speed)
    right_motors.forward(speed)


# move backward with a speed between 0-1 (default = 1)
def backward(speed=1):
    left_motors.backward(speed)
    right_motors.backward(speed)


# stop all motors
def stop():
    left_motors.stop()
    right_motors.stop()


# skid steer LEFT with a speed between 0-1 (default = 1)
def left(speed=1):
    left_motors.backward(speed)
    right_motors.forward(speed)


# skid steer RIGHT with a speed between 0-1 (default = 1)
def right(speed=1):
    left_motors.forward(speed)
    right_motors.backward(speed)
