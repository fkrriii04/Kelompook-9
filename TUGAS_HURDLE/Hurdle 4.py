#Program Untuk Bergerak ke Kanan
def turn_right():
    turn_left()
    turn_left()
    turn_left()
    
#Program Ketika Objek mencapai pucuk
def pucuk():
    turn_right()
    move()
    turn_right()

#program agar objek bergerak mengikuti pattern
def gerak():
    turn_left()
    while wall_on_right():
        move()
    pucuk()
    while front_is_clear():
        move()
    turn_left()

#Program agar objek tetap bergerak dan berhenti di goal
while not at_goal():
    if wall_in_front():
        gerak()
    else:
        move()
