from machine import Pin, I2C
from vl53l0x import setup_tofl_device, TBOOT
import utime

device_1_xshut = Pin(16, Pin.OUT)
i2c_1 = I2C(id=1, sda=Pin(14), scl=Pin(15))

# Set this low to disable device 1
print("Setting up device 0")
device_1_xshut.value(0)
tofl0 = setup_tofl_device(i2c_1, 40000, 12, 8)
tofl0.set_address(0x31)

try:
    print("Now setting up device 1")
    # Re-enable device 1 - on the same bus
    device_1_xshut.value(1)
    utime.sleep_us(TBOOT)

    tofl1 = setup_tofl_device(i2c_1, 40000, 12, 8)


    while True:
        left, right = tofl0.ping(), tofl1.ping()
        print(left, 'mm, ', right, 'mm')
        # left = tofl0.ping()
        # print(left, 'mm')
finally:
    # Restore default address
    print("Restoring")
    tofl0.set_address(0x29)
