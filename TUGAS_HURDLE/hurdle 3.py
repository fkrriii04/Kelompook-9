def turn_right():
    turn_left()
    turn_left()
    turn_left()
def maju():
    turn_left()
    move()
    turn_right()
    move()
    turn_right()
    move()
while not at_goal():
    if wall_in_front():
        maju()
        turn_left()
    elif front_is_clear():
        move()
