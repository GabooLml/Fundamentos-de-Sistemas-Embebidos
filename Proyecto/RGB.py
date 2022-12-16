from bluedot import BlueDot
from gpiozero import LED
from signal import pause

bd = BlueDot(cols = 2, rows = 4)
bd.border = True
bd[0,0].color = "gray"
bd[0,1].color = "green"
bd[0,2].color = "purple"
bd[0,3].color = "yellow"
bd[1,0].color = "red"
bd[1,1].color = "blue"
bd[1,2].color = "cyan"
bd[1,3].color = "white"


def off_rgb():
    red.value = 0
    green.value = 0
    blue.value = 0
    red1.value = 0
    green1.value = 0
    blue1.value = 0

def set_red():
    red.value = 1
    green.value = 0
    blue.value = 0
    red1.value = 1
    green1.value = 0
    blue1.value = 0

def set_green():
    red.value = 0
    green.value = 1
    blue.value = 0
    red1.value = 0
    green1.value = 1
    blue1.value = 0

def set_blue():
    red.value = 0
    green.value = 0
    blue.value = 1
    red1.value = 0
    green1.value = 0
    blue1.value = 1

def set_magenta():
    red.value = 1
    green.value = 0
    blue.value = 1
    red1.value = 1
    green1.value = 0
    blue1.value = 1

def set_cyan():
    red.value = 0
    green.value = 1
    blue.value = 1
    red1.value = 0
    green1.value = 1
    blue1.value = 1

def set_yellow():
    red.value = 1
    green.value = 1
    blue.value = 0
    red1.value = 1
    green1.value = 1
    blue1.value = 0

def set_white():
    red.value = 1
    green.value = 1
    blue.value = 1
    red1.value = 1
    green1.value = 1
    blue1.value = 1

red = LED(27)
green = LED(22)
blue = LED(10)
red1 = LED(11)
green1 = LED(25)
blue1 = LED(9)

#bd[0,0].when_pressed = set_red
#bd[0,2].when_moved = set_green
#bd[0,4].when_moved = set_blue
bd.border = True
bd[0,0].when_pressed = off_rgb
bd[0,1].when_pressed = set_green
bd[0,2].when_pressed = set_magenta
bd[0,3].when_pressed = set_yellow
bd[1,0].when_pressed = set_red
bd[1,1].when_pressed = set_blue
bd[1,2].when_pressed = set_cyan
bd[1,3].when_pressed = set_white

pause()