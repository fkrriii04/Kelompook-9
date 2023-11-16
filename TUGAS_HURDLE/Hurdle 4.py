def turn_right():
    turn_left()
    turn_left()
    turn_left()

def pucuk():
    turn_right()
    move()
    turn_right()

def gerak():
    turn_left()
    while wall_on_right():
        move()
    pucuk()
    while front_is_clear():
        move()
    turn_left()

while not at_goal():
    if wall_in_front():
        gerak()
    else:
        move()
