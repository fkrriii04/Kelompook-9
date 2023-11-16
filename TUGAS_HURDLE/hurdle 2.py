#Program untuk membelokkan robot
def turn_right():
    turn_left()
    turn_left()
    turn_left()

#Program untuk menghadapi obstacle
def maju():
    turn_left()
    move()
    turn_right()
    move()
    turn_right()
    move()

#Program untuk eksekusi robot dengan if else untuk titik finish yang random
while not at_goal():
    if wall_in_front():
        maju()
        turn_left()
    elif front_is_clear():
        move()
