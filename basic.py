from setup import RPL
import post_to_web as PTW # see post_to_web.py for instructions
import time as time
import control as con
#####################
#########PINS########
#####################

#sensor pins
back_sensor_pin = 16
starboard_sensor_pin = 17
port_sensor_pin = 18
front_sensor_pin = 23

#servo pins
left_servo_pin = 0
right_servo_pin = 1

#pin setup
RPL.pinMode(left_servo_pin,RPL.OUTPUT)
RPL.pinMode(right_servo_pin,RPL.OUTPUT)
RPL.pinMode(16,RPL.INPUT)
RPL.pinMode(17,RPL.INPUT)
RPL.pinMode(18,RPL.INPUT)
RPL.pinMode(19,RPL.INPUT)


##########################
#####control functions####
##########################
def stopAll():
    RPL.servoWrite(left_servo_pin,1500)
    RPL.servoWrite(right_servo_pin,1500)

def userInterface(): #reads the digital sensor inputs and contains movement autonomy
    print("\033c")
    sensors = []
    sensors.append(RPL.digitalRead(front_sensor_pin))
    sensors.append(RPL.digitalRead(starboard_sensor_pin))
    sensors.append(RPL.digitalRead(back_sensor_pin))
    sensors.append(RPL.digitalRead(port_sensor_pin))

    print "Front: %d" %frontSensorRead
    print "Right: %d" %starboardSensorRead
    print "Back: %d"  %backSensorRead
    print "Left: %d"  %portSensorRead

#######################
######## Logic ########
#######################
    if sensors = [0,0,0,0]: #Completely Surrounded
        print "Trapped!"
    elif sensors = [0,0,0,1]: #Walls Front, Right, Behind
        print "Attempting to escape left"
        con.left()
    elif sensors = [0,0,1,0]: #Walls Front, Right, Left
        print "Dead End. Reversing."
        con.reverse()
        time.sleep(3)
    elif sensors = [0,0,1,1]: #Walls Front, Right. Front Right Corner
        print " Front Right Corner. Turning Left"
        con.left()
    elif sensors = [0,1,0,0]: #Walls Front, Behind, Left. Parral Parked Left
        print "Attempting to escape Right."
        con.right()
        time.sleep(0.25)
        con.reverse()
    elif sensors = [0,1,0,1]: #Walls Front, Behind.
        print "Blocked front and back. Escaping Right"
        con.right()
        time.sleep(0.25)
        con.reverse()
    elif sensors = [0,1,1,0]: #Walls Front, Left.
        print "Blocked Front and Left."
        con.right()
    elif sensors = [0,1,1,1]: #Wall Front.
        print "Wall ahead. Turning left."
        con.reverse()
        time.sleep(0.25)
        con.left()
    elif sensors = [1,0,0,0]: #Walls Behind, Left, Right
        print "Backed in. Escaping forward"
        con.forward
    elif sensors = [1,0,0,1]: #Walls Right, Behind. Back Right Corner.
        print "Right Wall found. Proceeding Forward."
        con.forward
    elif sensors = [1,0,1,0]: #Walls Right, Left. Cooridor.
        print "In a cooridor. Proceeding Forward."
        con.forward()
    elif sensors = [1,0,1,1]: #Wall Right.
        print "Right Wall found. Proceeding Forward."
        con.forward()
    elif sensors = [1,1,0,0]: #Wall Behind, Left. Back Left Corner
        print "Wall Behind and Left. Turning Right."
        con.right()
    elif sensors = [1,1,0,1]: #Wall Behind.
        print "Wall Behind. Turning Right."
        con.right()
    elif sensors = [1,1,1,0]: #Wall Left
        print "Wall Left. Turning around."
        con.right()
        time.sleep(2)
    elif sensors = [1,1,1,1]: #No walls/points of reference.
        print "No Wall Aquired. Finding Wall."
        con.forward()


tState = time.time()

def post(interval = 0.25): #controls the time intervals that the sensors and ai refresh at
  global tState
  if time.time() - tState > interval:
    userInterface()
    tState = time.time()

while True: #run function
    post()
