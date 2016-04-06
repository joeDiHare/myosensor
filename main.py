import pyb
led3 = pyb.LED(3)
led3.on()

lcd = pyb.LCD('X')      # if pyskin is in the Y position
lcd.light(True)

i2c = pyb.I2C(1, pyb.I2C.MASTER)
i2c.mem_write(4, 90, 0x5e)
touch = i2c.mem_read(1, 90, 0)[0]

sw  = pyb.Switch()                  # USR button
#if sw():
adc = pyb.ADC(pyb.Pin.board.Y12)    # create an ADC on pin X19
buf = bytearray(100)                # create a buffer of 100 bytes
#buf2 = bytearray(100)               # create a buffer of 100 bytes

accel = pyb.Accel()                 # accellerometer
f = open('log/data.dat', 'a')     # open the file for writing
val=0;
while True:
    adc.read_timed(buf, 100)        # read analog values into buf at 100Hz (will take 10 s)
    x, y, z = accel.filtered_xyz()  # get the accelerometer data
    time = pyb.millis()             # get time in ms
    #f.write("{} {} {} {}".format(time, x, y, z)) # write muscl_input and x,y,z
    for val in buf:
        f.write("{} {} {} {} {}\n".format(time, x, y, z, val)) # write muscl_input and x,y,z
    #lines.append('{} {} {} {}\n'.format(a, x, y, z))# FASTER, BUT then lines gets quite big...
    #for val in buf:                # REPL: loop and print values
    #    print(val)
    lcd.write('\nstrength:'+str(val)+'\nstamina:'+str(100-val)+'\ntime:'+str(time)+'\nx,y,z = '+str(x)+','+str(y)+','+str(z))

    pyb.delay(1)                    # apparently, for stability

    if sw():                        # if USR button is pressed, exit loop
        break
#f.close()                           # close the file
led3.off()                          # turn led off
