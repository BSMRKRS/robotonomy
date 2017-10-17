from setup import RPL
import post_to_web as PTW # see post_to_web.py for instructions
import time as time
#sensors
back_sensor = 17
starboard_sensor = 18
port_sensor = 19

RPL.pinMode(17,RPL.INPUT)
RPL.pinMode(18,RPL.INPUT)
RPL.pinMode(19,RPL.INPUT)

def userInterface():
  rightSensor = RPL.digitalRead(starboard_sensor)
  leftSensor = RPL.digitalRead(port_sensor)
  backSensor = RPL. digitalRead(back_sensor)
  print "Right: %d" %rightSensor
  print "Left: %d"  %leftSensor
  print "Back: %d"  %backSensor

tState = time.time()

def post(interval = 0.5):
  global tState
  if time.time() - tState > interval:
    userInterface()
    tState = time.time()

def userInterface():
  print("\033c")
  rightSensor = RPL.readDistance(starboard_sensor)
  leftSensor = RPL.readDistance(port_sensor)
  backSensor = RPL. readDistance(back_sensor)
  print "Right: %d" %rightSensor
  print "Left: %d"  %leftSensor
  print "Back: %d"  %backSensor

while True:
    post()
