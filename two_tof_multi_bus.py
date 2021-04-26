from machine import Pin, I2C
from vl53l0x import setup_tofl_device

i2c_0 = I2C(id=0, sda=Pin(16), scl=Pin(17))
i2c_1 = I2C(id=1, sda=Pin(14), scl=Pin(15))

tofl0 = setup_tofl_device(i2c_0, 40000, 12, 8)
tofl1 = setup_tofl_device(i2c_1, 40000, 12, 8)

while True:
    left, right = tofl0.ping() - 50, tofl1.ping() - 50
    print(left, 'mm, ', right, 'mm')
