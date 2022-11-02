# all imports from library
import neopixel
import board
import time
import random
import digitalio as dio
import touchio

# defining neopixel
BRIGHTNESS = 0.25
np = neopixel.NeoPixel(board.NEOPIXEL, 10, brightness=BRIGHTNESS, auto_write=False)

#defining button and touch pads
button_a = dio.DigitalInOut(board.BUTTON_A)
button_a.direction = dio.Direction.INPUT
button_a.pull = dio.Pull.DOWN
touch1 = touchio.TouchIn(board.A1)
touch2 = touchio.TouchIn(board.A2)
touch3 = touchio.TouchIn(board.A5)
touch4 = touchio.TouchIn(board.A6)

#rgb values defined, game_list defined, and boolean values defined
green = [0, 255, 0]
blue = [0, 0, 255]
red = [255, 0, 0]
yellow = [236, 236, 0]
black = [0, 0, 0]
game_list = []
comparitive = 0
game_status = False
buttons = False


"""
Function name: reset
Description: This resets the game mode to have an empty list and set the 
status to false
Parameters: none
Return value: none
"""
def reset():
    global game_list, game_status
    game_list = []
    game_status = False

"""
Function name: make_seq
Description: Makes a random sequence of game numbers
Parameters: glist (list) - the inputted list that will hold the values
Return value: none
"""
def make_seq(glist):
    global beginning
    beginning = 1
    number = random.randint(1, 4)
    glist.append(number)

"""
Function name: flash
Description: Flashes the inputted color twice
Parameters: color (tuple) - rgb that will flash;
delay (floating point) - the time that is delayed
Return value: none
"""
def flash(color, delay):
    for i in range(2):
        np.fill(color)
        np.show()
        time.sleep(delay)
        np.fill(black)
        np.show()
        time.sleep(delay)

"""
Function name: show_seq
Description: Converts the numbers into rgb colors and flashes the sequence in order
of the list
Parameters: num (int) - the value from the list; 
delay (floating point) - the time that is delayed
Return value: none
"""
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

"""
Function name: check_seq
Description: It will check the comparitive value to the index in the list
Parameters: comp_val (int) - the comparitive value set in 
another function; index (int) - the index set in the game list
Return value: True or Flase depending on the if statements
"""
def check_seq(comp_val, index):
        if comp_val == index:
            return True
        else:
            return False
        time.sleep(0.25)

"""
Function name: input_of_user
Description: Takes in the input of user and flashes the rgb value associated 
with the touch pad and while setting a comparitive value; also has the check_seq function
inside this function
Parameters: delay - the time that is delayed (floating point)
Return value: none
"""
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

"""
Function name: game
Description: Takes all the functions together and turns it into 
the game with the for loops and correct order
Parameters: none
Return value: none
"""
def game():
    global game_list
    make_seq(game_list)
    flash(green, 0.1)
    time.sleep(1)
    for i in range(len(game_list)):
        show_seq(game_list[i], 0.25)
    input_of_user(0.32)


# displays the infinite loop of the game
while True:
    time.sleep(0.01)
    if not game_status:
        if button_a.value:
            buttons = not buttons
            time.sleep(0.05)
            game_status = True
    else:
        game()
