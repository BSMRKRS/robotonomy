from setup import RPL
import post_to_web as PTW # see post_to_web.py for instructions
import time as time
#sensors
analogue_pin = 16
back_sensor = 17
starboard_sensor = 18
port_sensor = 19

RPL.pinMode(16,RPL.INPUT)
RPL.pinMode(17,RPL.INPUT)
RPL.pinMode(18,RPL.INPUT)
RPL.pinMode(19,RPL.INPUT)

def userInterface():
  print("\033c")
  analogue = RPL.readDistance(analogue_pin)
  rightSensor = RPL.digitalRead(starboard_sensor)
  leftSensor = RPL.digitalRead(port_sensor)
  backSensor = RPL.digitalRead(back_sensor)
  print "LeftAn: %d" %analogue
  print "Right: %d" %rightSensor
  print "Left: %d"  %leftSensor
  print "Back: %d"  %backSensor

tState = time.time()

def post(interval = 0.5):
  global tState
  if time.time() - tState > interval:
    userInterface()
    tState = time.time()

while True:
    post()
