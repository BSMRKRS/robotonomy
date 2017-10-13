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

tState = time.time()

while True:
  PTW.state['d1'] = RPL.digitalRead(starboard_sensor)
  PTW.state['d2'] = RPL.digitalRead(port_sensor)
  PTW.state['d3'] = RPL. digitalRead(back_sensor)
  PTW.post()
