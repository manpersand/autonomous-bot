import bot_control as bot
from time import sleep

distance = bot.distance()

while True:
    while distance > 30:
        print("Distance : " + str(distance)),
        bot.left_motors.forward(0.7)
        bot.right_motors.forward(0.7)
        distance = bot.distance()

    while distance <= 30:
        print("Distance : " + str(distance) + "Too close!")
        bot.stop()
        bot.servo.left()
        sleep(0.2)
        left_distance = bot.distance()
        bot.servo.right()
        sleep(0.4)
        right_distance = bot.distance()
        if left_distance > right_distance:
            bot.left()
        elif right_distance > left_distance:
            bot.right()
        distance = bot.distance()

