
from bluedot import BlueDot
from signal import pause

count = 0

def rotated(rotation):
    global count
    count += rotation.value

    print("{} {} {}".format(count,
                            rotation.clockwise,
                            rotation.anti_clockwise))
    if(rotation.clockwise):
        bd.color="red"
    else:
        bd.color="blue"

bd = BlueDot()
bd.when_rotated = rotated

pause()

