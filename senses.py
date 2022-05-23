
from sense_hat import SenseHat
from time import sleep

sense = SenseHat()

#declare a temperature variable and assign it the value of sense.get_temperature()
temp = sense.get_temperature()
pressure = sense.get_pressure()

#print out type statements:

print("The temperature is", temp)
print("The pressure is", pressure)



# show values on Sense HAT / one-time

sense.show_message(temp)


#make a while True loop



    #add conditional statements to test
