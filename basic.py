from setup import RPL
import post_to_web as PTW # see post_to_web.py for instructions
import time as time
import control as con

#####################
######## PIN ########
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
#### CONTROL FUNCTIONS ###
##########################
def stopAll(): #Stops the vehicle
    RPL.servoWrite(left_servo_pin,1500)
    RPL.servoWrite(right_servo_pin,1500)

##########################
# GRAPHIC USER INTERFACE #
##########################
def gui(sensor): #Draws a visual representation of the cars surroundings
    print("\033c")
    print "Front: %d" %sensor[0]
    print "Right: %d" %sensor[1]
    print "Back: %d"  %sensor[2]
    print "Left: %d"  %sensor[3]
    if sensor[0] == 0:
        print """ ___"""
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
        print """ ---"""
    else:
        print """    """

#######################
######## LOGIC ########
#######################
def logic(history): #With four binary sensors, there are 16 possible scenarios.
    sensors = history
    if sensors == [0,0,0,0]: #Completely Surrounded
        print "Trapped!"
        stopAll()
    elif sensors == [0,0,0,1]: #Walls Front, Right, Behind
        print "Attempting to escape left"
        con.left()
    elif sensors == [0,0,1,0]: #Walls Front, Right, Left
        print "Dead End. Reversing."
        p = sensorRead() #sets temp variable p to current sensor readings
        while p[1] == 0 or p[3] == 0: #this while loop reverses, and then updates p with current data
            con.reverse()
            p = sensorRead() #This updates p. When p[1] or [3] (R/L) are no longer blocked, the loop stops.
        if p[1] == 1: #if the right sensor changes first, the vehicle turns right
            print "escape right"
            con.right()
            time.sleep(2)
            con.forward()
            time.sleep(0.5)
        else: #if the left changes, it turns left.
            print "escape left"
            con.left(2)
            time.sleep(2)
            con.forward()
            time.sleep(0.5)

    elif sensors == [0,0,1,1]: #Walls Front, Right. Front Right Corner
        print " Front Right Corner. Turning Left"
        con.left()
        time.sleep(0.5)
    elif sensors == [0,1,0,0]: #Walls Front, Behind, Left. Parral Parked Left
        print "Attempting to escape Right."
        con.right()
        time.sleep(0.25)
        con.reverse()
    elif sensors == [0,1,0,1]: #Walls Front, Behind.
        print "Blocked front and back. Escaping Right"
        con.right()
        time.sleep(0.25)
        con.reverse()
    elif sensors == [0,1,1,0]: #Walls Front, Left.
        print "Blocked Front and Left."
        con.right()
    elif sensors == [0,1,1,1]: #Wall Front.
        print "Wall ahead. Turning left."
        con.reverse()
        time.sleep(0.5)
        con.left()
        time.sleep(2)
        con.forward()
        time.sleep(0.5)
    elif sensors == [1,0,0,0]: #Walls Behind, Left, Right
        print "Backed in. Escaping forward"
        con.forward
    elif sensors == [1,0,0,1]: #Walls Right, Behind. Back Right Corner.
        print "Right Wall found. Proceeding Forward."
        con.forward
    elif sensors == [1,0,1,0]: #Walls Right, Left. Cooridor.
        print "In a cooridor. Proceeding Forward."
        con.forward()
    elif sensors == [1,0,1,1]: #Wall Right.
        print "Right Wall found. Proceeding Forward."
        con.forward()
    elif sensors == [1,1,0,0]: #Wall Behind, Left. Back Left Corner
        print "Wall Behind and Left. Turning Right."
        con.right()
    elif sensors == [1,1,0,1]: #Wall Behind.
        print "Wall Behind. Turning Right."
        con.forward()
        time.sleep(0.5)
        con.right()
    elif sensors == [1,1,1,0]: #Wall Left
        print "Wall Left. Turning around."
        con.right()
        time.sleep(3)
    elif sensors == [1,1,1,1]: #No walls/points of reference.
        print "No Wall Aquired. Finding Wall."
        con.forward()
        time.sleep(0.25)
        con.right()
        time.sleep(0.5)
    else:
        print "ERROR!"
    #stuck = 0
    #for i in history:
    #    if history[i] == history[0] and history[11,0] == 0:
    #        stuck +=1
    #    if stuck >= 11:
    #        print "Error: No Change in 3 seconds. Stopping"
    #        stopAll()
    #        startStop()


##########################
########## RUN ###########
##########################

history = []

def sensorRead(): #reads the digital sensor inputs and contains movement autonomy
    global history
    sensors = []
    sensors.append(RPL.digitalRead(front_sensor_pin))
    sensors.append(RPL.digitalRead(starboard_sensor_pin))
    sensors.append(RPL.digitalRead(back_sensor_pin))
    sensors.append(RPL.digitalRead(port_sensor_pin))
    history.append(sensors)
    if len(history) == 13:
        del history[0]
    return sensors

def run():
    gui(sensorRead())
    logic(sensorRead())

tState = time.time()
def timeInterval(interval = 0.25): #controls the time intervals that the sensors and ai refresh at
  global tState
  if time.time() - tState > interval:
    run()
    tState = time.time()
def pause():
    raw_input("Enter any key to continue")
pause()
while True: #run function
    timeInterval()
