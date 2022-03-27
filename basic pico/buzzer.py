from machine import Pin
import time
 
button = Pin(3, Pin.IN, Pin.PULL_UP)
buzzer = Pin(11, Pin.OUT)
 
while True:
    if button.value() == 0:
        print("button pressed")
        buzzer.value(0.0001)
        time.sleep(0.1)
    else:
        buzzer.value(0)