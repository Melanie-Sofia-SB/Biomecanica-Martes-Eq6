from machine import Pin, PWM, ADC
import utime

pot1 = ADC(Pin(28))
pot2 = ADC(Pin(27))

servo1 = PWM(Pin(0))
servo2 = PWM(Pin(1))

servo1.freq(50)
servo2.freq(50)

while True:
    value1 = int(1350 + (pot1.read_u16()/9.57))
    servo1.duty_u16(value1)
    utime.sleep(0.02)
    
    value2 = int(1350 + (pot2.read_u16()/9.57))
    servo2.duty_u16(value2)
    utime.sleep(0.02)