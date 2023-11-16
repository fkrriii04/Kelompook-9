#Program untuk membelokan robot
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

#Program robot berjalan dan menghadapi obstacle
def jalan():
    move()
    maju()
    turn_left()

#Program eksekusi jalannya robot
def jalan_seterusnya():
    jalan()
    jalan()
    jalan()
    jalan()
    jalan()
    jalan()

#Eksekusi
jalan_seterusnya()