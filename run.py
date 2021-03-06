from time import sleep
import bot_control as bot
import curses

# Get the curses window, turn off echoing of keyboard to screen, turn on
# instant (no waiting) key response, and use special values for cursor keys
screen = curses.initscr()
curses.noecho()
curses.cbreak()
screen.keypad(True)

try:
    while True:
        # bot.stop()
        char = screen.getch()
        if char == ord('q'):
            break
        elif char == curses.KEY_UP:
            bot.forward(100, 0.7)
        elif char == curses.KEY_DOWN:
            bot.backward(100, 0.7)
        elif char == curses.KEY_RIGHT:
            bot.right(0.7)
        elif char == curses.KEY_LEFT:
            bot.left(0.7)
        elif char == ord('d'):
            bot.forward(cm=2)
            bot.backward(cm=2)
            bot.left(angle=45)
            bot.right(angle=90)
            bot.left(angle=45)
            bot.Stop()
        else:
            bot.stop()


finally:
    # Close down curses properly, inc turn echo back on!
    curses.nocbreak()
    screen.keypad(0)
    curses.echo()
    curses.endwin()
