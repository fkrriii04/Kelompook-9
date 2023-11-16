# Program untuk belok ke kanan
def turn_right():
    turn_left()
    turn_left()
    turn_left()
    
# Program Untuk melewati Rintangan
def maju():
    turn_left()
    move()
    turn_right()
    move()
    turn_right()
    move()
    
# Program untuk maju ke depan 
while not at_goal():
    if wall_in_front():
        maju()
        turn_left()
    elif front_is_clear():
        move()
