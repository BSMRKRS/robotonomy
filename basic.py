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
RPL.pinMode(back_sensor_pin,RPL.INPUT)
RPL.pinMode(starboard_sensor_pin,RPL.INPUT)
RPL.pinMode(port_sensor_pin,RPL.INPUT)
RPL.pinMode(front_sensor_pin,RPL.INPUT)


##########################
#####control functions####
##########################
def stopAll(): #Stops the vehicle
    RPL.servoWrite(left_servo_pin,1500)
    RPL.servoWrite(right_servo_pin,1500)

##########################
##Graphic User Interface##
##########################
def gui(sensor): #Draws a visual representation of the cars surroundings
    print("\033c")
    print "Front: %d" %frontSensorRead
    print "Right: %d" %starboardSensorRead
    print "Back: %d"  %backSensorRead
    print "Left: %d"  %portSensorRead
    if sensor[0] == 0:
        print """____"""
    else:
        print"""    """
    if sensor[1] == 0 and sensor[3] == 0:
        print"""|   |"""
        print"""|   |"""
    elif sensor[1] == 1 and sensor[3] == 0:
        print"""    |"""
        print"""    |"""
    elif sensor[1] == 0 and sensor[3] == 1:
        print"""|    """
        print"""|    """
    else:
        print
        print
    if sensor[2] == 0:
        print """----"""
    else:
        print """    """

#######################
######## Logic ########
#######################
def logic(history): #With four binary sensors, there are 16 possible scenarios.
    sensors = history[-1]
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
    else: #No walls/points of reference.
        print "No Wall Aquired. Finding Wall."
        con.forward()
    if for i in history i == history[0] and history[11,0] == 0:
        print "Error: No Change in 3 seconds. Stopping"
        stopAll()
        startStop()


##########################
########## Run ###########
##########################


def sensorRead(): #reads the digital sensor inputs and contains movement autonomy
    sensors = []
    sensors.append(RPL.digitalRead(front_sensor_pin))
    sensors.append(RPL.digitalRead(starboard_sensor_pin))
    sensors.append(RPL.digitalRead(back_sensor_pin))
    sensors.append(RPL.digitalRead(port_sensor_pin))
    history.append(sensors)
    if len(history) == 13:
        del history[0]
    gui(sensors)
    logic(history)

tState = time.time()
def timeInterval(interval = 0.25): #controls the time intervals that the sensors and ai refresh at
  global tState
  if time.time() - tState > interval:
    sensorRead()
    tState = time.time()
def pause():
    raw_input("Enter any key to continue")
while True: #run function
    timeInterval()
