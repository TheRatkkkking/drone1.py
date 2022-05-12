from djitellopy import tello
from time import sleep

me = tello.Tello()
me.connect()
print(me.get_battery())

# The drone will reach just above 160cm, around 200cm after take off
me.takeoff()
me.move_up(120)
sleep(.5)

# reach just over the halfway point of the classroom
me.move_forward(500)
sleep(.5)

me.rotate_counter_clockwise(90)
sleep(.5)

# cool trick to prove that drones are cool
me.flip_forward()
me.move_forward(350)
sleep(.5)

me.rotate_counter_clockwise(90)
sleep(.5)

# start to head back
me.move_forward(500)
sleep(.5)

me.rotate_counter_clockwise(90)
sleep(.5)

# we are almost home!! Return to original spot
me.move_forward(350)
sleep(.5)

# spin twice, then land
me.rotate_clockwise(810)
sleep(.5)

me.land()
