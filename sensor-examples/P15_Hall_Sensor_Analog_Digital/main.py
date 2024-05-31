import time
from machine import ADC
from machine import Pin

# Pin setup
#change between digital or analog here
#analogPin = ADC(27)
digitalPin = Pin(27, Pin.IN)

while True:
    #analogValue = analogPin.read_u16()
    digitalValue = digitalPin.value()
    #print("The magnetic strength is {}".format(analogValue))  # The stronger the magnet the lower value it produce
    if digitalValue == False:
        print("Digital pin activated...")
    else:
        print("Digital pin inactive...")
    time.sleep(1)