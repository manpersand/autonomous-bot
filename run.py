from time import sleep
import bot_control
import curses



# Get the curses window, turn off echoing of keyboard to screen, turn on
# instant (no waiting) key response, and use special values for cursor keys
screen = curses.initscr()
curses.noecho() 
curses.cbreak()
screen.keypad(True)

try:
        while True:
            Stop()
            char = screen.getch()
            if char == ord('q'):
                break
            elif char == curses.KEY_UP:
                Forward(0.7)
                print
            elif char == curses.KEY_DOWN:
                Backward(0.7)
            elif char == curses.KEY_RIGHT:
                TurnRight(0.7)
            elif char == curses.KEY_LEFT:
                TurnLeft(0.7)
            elif char == ord('d'):
                Forward(0.7)
                sleep(0.5)
                Backward(0.7)
                sleep(0.5)
                TurnLeft(0.7)
                sleep(0.5)
                TurnRight(0.70)
                sleep(0.5)
                Stop()

##            if speedSensRight.value == True:
##                print("ON"),
##            else:
##                print("OFF"),
             
finally:
    #Close down curses properly, inc turn echo back on!
    curses.nocbreak(); screen.keypad(0); curses.echo()
    curses.endwin()
