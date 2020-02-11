import gpiozero as gpio
import proximity
import gyro

# Motor gpio setup (forward pin, backward pin)
right_motors = gpio.Motor(17, 27)
left_motors = gpio.Motor(24, 23)

# speed encoder sensor setup
right_speed = gpio.DigitalInputDevice(25)
left_speed = gpio.DigitalInputDevice(22)


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
