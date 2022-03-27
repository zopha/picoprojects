from machine import Pin, PWM
from time import sleep

pwm = PWM(Pin(15))

pwm.freq(1000)

while True:
    for duty in range(32512):
        pwm.duty_u16(duty)
        sleep(0.000001)
    for duty in range(32512, 0, -1):
        pwm.duty_u16(duty)
        sleep(0.000001)