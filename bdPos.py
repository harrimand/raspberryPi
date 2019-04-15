from bluedot import BlueDot
from signal import pause

def dot_was_pressed(pos):
    print("The Blue Dot was pressed at pos x={} y={}".format(pos.x, pos.y))

bd = BlueDot()
bd.square = True
bd.when_pressed = dot_was_pressed
pause()

