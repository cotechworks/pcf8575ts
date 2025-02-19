from pcf8575ts import pcf8575ts
import time

gpio = pcf8575ts(0x20)
while 1:
    gpio.write(0x80)
    time.sleep(1)
    gpio.write(0x00)
    time.sleep(1)