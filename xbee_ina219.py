from ina219 import INA219
from machine import I2C

# pretty much all the breakout boards come with a 0.1 ohm shunt resistor
# giving a measurement range of +/- 3.2 amps.  If you know your device has
# a different resistor (or can infer it does based on a different measurement
# range) you'll need to change this
SHUNT_OHMS = 0.1

# use the hardware I2C device on the XBee - pins D1 (DIO1, scl) and P1 (DIO11, da)
i2c = I2C(1)

ina = INA219(SHUNT_OHMS, i2c)
ina.configure()

print("Bus Voltage: %.3f V" % ina.voltage())
print("Current: %.3f mA" % ina.current())
print("Power: %.3f mW" % ina.power())
