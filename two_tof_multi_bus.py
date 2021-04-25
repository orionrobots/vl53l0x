from machine import Pin, I2C
from vl53l0x import VL53L0X

def setup_tofl_device(i2c, timing_budget, pre_range, final_range):
    tofl = VL53L0X(i2c)
    # initialise timing budget
    # the measuring_timing_budget is a value in ms, the longer the budget, the more accurate the reading.
    #budget_0 = tof.measurement_timing_budget_us
    tofl.set_measurement_timing_budget(timing_budget)
    # Set VCSel
    # Sets the VCSEL (vertical cavity surface emitting laser) pulse period for the
    # given period type (VL53L0X::VcselPeriodPreRange or VL53L0X::VcselPeriodFinalRange)
    # to the given value (in PCLKs). Longer periods increase the potential range of the sensor.
    # Valid values are even numbers only pre = 18,12 and final 14, 8:
    # tof.set_Vcsel_pulse_period(tof.vcsel_period_type[0], 18)
    tofl.set_Vcsel_pulse_period(VL53L0X.vcsel_period_type[0], pre_range)

    # tof.set_Vcsel_pulse_period(tof.vcsel_period_type[1], 14)
    tofl.set_Vcsel_pulse_period(VL53L0X.vcsel_period_type[1], final_range)
    return tofl


i2c_0 = I2C(id=0, sda=Pin(16), scl=Pin(17))
i2c_1 = I2C(id=1, sda=Pin(14), scl=Pin(15))

tofl0 = setup_tofl_device(i2c_0, 40000, 12, 8)
tofl1 = setup_tofl_device(i2c_1, 40000, 12, 8)
tofl1.set_address(0x31)

while True:
    left, right = tofl0.ping() - 50, tofl1.ping() - 50
    print(left, 'mm, ', right, 'mm')
