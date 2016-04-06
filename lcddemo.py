"""
Demo for the LCD and touch sensor.

Plug the LCD skin in the X-position, have the mpr121.py script and
this script on the board, and then type:

>>> import lcddemo
>>> lcddemo.run(1000)

"""

import pyb
import mpr121

def run(n):
    lcd = pyb.LCD('X')
    lcd.light(1)
    m = mpr121.MPR121(pyb.I2C(1, pyb.I2C.MASTER))

    def blob(x, y, w, h, fill):
        for i in range(w):
            for j in range(h):
                if pyb.rng() & 0xff < fill:
                    lcd.pixel(x + i, y + j, 1)

    for i in range(n):
        t = m.touch_status()
        lcd.fill(0)
        for y in range(32):
            lcd.pixel(64, y, 1)
        for x in range(128):
            lcd.pixel(x, 16, 1)
        if t & 1:
            blob(90, 20, 10, 10, 316 - m.elec_voltage(0))
        if t & 2:
            blob(30, 20, 10, 10, 316 - m.elec_voltage(1))
        if t & 4:
            blob(90, 5, 10, 10, 316 - m.elec_voltage(2))
        if t & 8:
            blob(30, 5, 10, 10, 316 - m.elec_voltage(3))
        lcd.show()
        pyb.delay(50)
