from setup import RPL
import post_to_web as PTW # see post_to_web.py for instructions
#sensors
import time as time
back_sensor = 17
starboard_sensor = 18
port_sensor = 19

RPL.pinMode(17,RPL.INPUT)
RPL.pinMode(18,RPL.INPUT)
RPL.pinMode(19,RPL.INPUT)

tState = time.time()
while True:
    global tState
    if time.time() - tState > 0.5:
<<<<<<< HEAD
        print RPL.digitalRead(back_sensor)
        print RPL.digitalRead(starboard_sensor)
        print RPL.digitalRead(port_sensor)
        tState = time.time()
=======
        print RPL.readDistance(back_sensor)
        print RPL.readDistance(starboard_sensor)
        print RPL.readDistance(port_sensor)
            tState = time.time()
>>>>>>> 0a55936c447eb1eb0508a4dbb9eb7ae038beb99b
