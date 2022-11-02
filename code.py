import neopixel
import board
import time
import random
import digitalio as dio
import touchio

BRIGHTNESS = 0.25
np = neopixel.NeoPixel(board.NEOPIXEL, 10, brightness=BRIGHTNESS, auto_write=False)

button_a = dio.DigitalInOut(board.BUTTON_A)
button_a.direction = dio.Direction.INPUT
button_a.pull = dio.Pull.DOWN
touch1 = touchio.TouchIn(board.A1)
touch2 = touchio.TouchIn(board.A2)
touch3 = touchio.TouchIn(board.A5)
touch4 = touchio.TouchIn(board.A6)

game_list = []
green = [0, 255, 0]
blue = [0, 0, 255]
red = [255, 0, 0]
yellow = [236, 236, 0]
black = [0, 0, 0]

comparitive = 0
game_status = False
buttons = False

def reset():
    global game_list, game_status
    game_list = []
    game_status = False

def make_seq(glist):
    global beginning
    beginning = 1
    number = random.randint(1, 4)
    glist.append(number)

def flash(color, delay):
    for i in range(2):
        np.fill(color)
        np.show()
        time.sleep(delay)
        np.fill(black)
        np.show()
        time.sleep(delay)

def show_seq(num, delay):
        if num == 1:
            np[5] = green
            np[6] = green
            np.show()
            time.sleep(delay)
            np[5] = black
            np[6] = black
            np.show()
            time.sleep(delay)
        if num == 2:
            np[8] = blue
            np[9] = blue
            np.show()
            time.sleep(delay)
            np[8] = black
            np[9] = black
            np.show()
            time.sleep(delay)
        if num == 3:
            np[0] = red
            np[1] = red
            np.show()
            time.sleep(delay)
            np[0] = black
            np[1] = black
            np.show()
            time.sleep(delay)
        if num == 4:
            np[3] = yellow
            np[4] = yellow
            np.show()
            time.sleep(delay)
            np[3] = black
            np[4] = black
            np.show()
            time.sleep(delay)
        time.sleep(delay * 2)

def check_seq(comp_val, index):
        if comp_val == index:
            return True
        else:
            return False
        time.sleep(0.25)

def input_of_user(delay):
    global comparitive
    global value_sent
    for i in range(len(game_list)):
        while (touch1.value or touch2.value or touch3.value or touch4.value) == False:
            pass
        if touch1.value == True:
            np[5] = green
            np[6] = green
            np.show()
            time.sleep(delay)
            np[5] = black
            np[6] = black
            np.show()
            time.sleep(delay)
            comparitive = 1

        if touch2.value == True:
            np[8] = blue
            np[9] = blue
            np.show()
            time.sleep(delay)
            np[8] = black
            np[9] = black
            np.show()
            time.sleep(delay)
            comparitive = 2

        if touch3.value == True:
            np[0] = red
            np[1] = red
            np.show()
            time.sleep(delay)
            np[0] = black
            np[1] = black
            np.show()
            time.sleep(delay)
            comparitive = 3

        if touch4.value == True:
            np[3] = yellow
            np[4] = yellow
            np.show()
            time.sleep(delay)
            np[3] = black
            np[4] = black
            np.show()
            time.sleep(delay)
            comparitive = 4

        value_sent = check_seq(comparitive, game_list[i])
        if not value_sent == True:
            flash(red, 0.1)
            reset()
            return


def game():
    global game_list
    make_seq(game_list)
    flash(green, 0.1)
    time.sleep(1)
    for i in range(len(game_list)):
        show_seq(game_list[i], 0.25)
    input_of_user(0.32)


while True:
    time.sleep(0.01)
    if not game_status:
        if button_a.value:
            buttons = not buttons
            time.sleep(0.05)
            game_status = True
    else:
        game()
