import bot_control as bot
import time


distance = bot.distance()

while True:
    while distance > 20:
        print("Distance : " + str(distance)),
        #time.sleep(0.250)
        bot.forward(0.7)
        distance = bot.distance()

    while distance <= 20:
        print("Distance : " + str(distance) + "Too close!")
        bot.stop()
        distance = bot.distance()
