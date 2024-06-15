from machine import Pin, ADC
import time
import sys

VRX = ADC(27)
VRY = ADC(28)
SW = Pin(26, Pin.IN, Pin.PULL_UP)
led = Pin(25, Pin.OUT)

while True:
    led.value(1)
    x = int(VRX.read_u16() / 300)
    y = int(VRY.read_u16() / 300)
    btn = int(not SW.value())
    
    mensaje = f"x{x},y{y},b{btn}\n"
    sys.stdout.write(mensaje)
    led.value(0)
    time.sleep(0.2)