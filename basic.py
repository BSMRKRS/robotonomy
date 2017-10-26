from setup import RPL
import post_to_web as PTW # see post_to_web.py for instructions
import time as time
import control as con
#####################
#########PINS########
#####################

#sensor pins
analogue_pin = 16
back_sensor_pin = 17
starboard_sensor_pin = 18
port_sensor_pin = 19
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
  #rightSensor = RPL.digitalRead(starboard_sensor)
  #leftSensor = RPL.digitalRead(port_sensor)
  backSensorRead = RPL.digitalRead(back_sensor_pin)
  frontSensorRead = RPL.digitalRead(front_sensor_pin)
  print "Front: %d"  %frontSensorRead
  print "Back: %d"  %backSensorRead
  if frontSensorRead == 0:
      con.forward()
      print "forward"
  elif frontSensorRead == 1 and backSensorRead == 0:
      con.reverse()
      print "reverse"
  else:
      stopAll()
      print "stop"

tState = time.time()

def post(interval = 0.25): #controls the time intervals that the sensors and ai refresh at
  global tState
  if time.time() - tState > interval:
    userInterface()
    tState = time.time()

while True: #run function
    post()
