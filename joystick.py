from sense_hat import SenseHat
sense = SenseHat()
sense.clear()

while True:
  for event in sense.stick.get_events():
    print(event.direction, event.action)
    
def red():
  sense.clear(255, 0, 0)
  
def blue():
  sense.clear(0, 0, 255)
  
def green():
  sense.clear(0, 255, 0)
  
def yellow():
  sense.clear(255, 255, 0)
  
sense.stick.direction_up = red
sense.stick.direction_down = blue
#sense.stick.direction_left = green
#sense.stick.direction_right = yellow
sense.stick.direction_middle = sense.clear

# need to create a repeat forever

while True:
  pass
