import pyb
import math
led3 = pyb.LED(3)
led3.on()

lcd = pyb.LCD('X')      # if pyskin is in the X position
lcd.light(True)
lcd.write('MyoGen 1.0 beta\n\nPress USR buttonto begin workout\n')

i2c = pyb.I2C(1, pyb.I2C.MASTER)
i2c.mem_write(4, 90, 0x5e)
touch = i2c.mem_read(1, 90, 0)[0]

sw  = pyb.Switch()   # USR button
while True:          # wait for user to press button
    pyb.delay(100)
    led3.toggle()
    if sw():
        break
led3.on()
pyb.delay(2000)

adc = pyb.ADC(pyb.Pin.board.Y12)    # create an ADC on pin X19
buf = bytearray(100)                # create a buffer of 100 bytes

led2 = pyb.LED(2) #green
led2.on()

accel = pyb.Accel()                 # accellerometer

f = open('log/data'+str(pyb.millis())+'.dat', 'a')  # generate & open file with new timestamp
maxStrength=0 # initialize max Strength
while True:
    adc.read_timed(buf, 100)        # read analog values into buf at 100Hz (will take 10 s)
    x, y, z = accel.filtered_xyz()  # get the accelerometer data
    tm = pyb.millis()             # get time in ms
    f.write("{} {} {} {} {}\n".format(tm, x, y, z," ".join(str(e) for e in buf))) # write muscl_input and x,y,z
    # count=0
    # for val in buf:
    #     count=count+val
        # f.write("{} {} {} {} {}\n".format(tm, x, y, z, val[0])) # write muscl_input and x,y,z
        # lines.append('{} {} {} {} {}\n'.format(tm, x, y, z, val[0]))# FASTER, BUT then lines gets quite big...
    Mean=sum(buf)/len(buf)
    maxStrength=max([Mean, maxStrength])

    prog_bar=''
    for k in range(1,math.trunc(10*Mean/254)): # this will produce 10 bars if the average (count/100) is max (=>254)
        prog_bar=prog_bar+'|'
    lcd.write('\nstrength:'+str(math.trunc(Mean))+'\n'+prog_bar+'\nhighest:'+str(maxStrength)+'\nx,y,z='+str(x)+','+str(y)+','+str(z))
    #lcd.write('\nstrength:'+str(count/100)+'\nstamina:'+str(100-val)+'\ntime:'+str(time)+'\nx,y,z = '+str(x)+','+str(y)+','+str(z))

    pyb.delay(1)                    # apparently, for stability
    led2.toggle()
    if sw():                        # if USR button is pressed, exit loop
        break

lcd.write('\n\nEnd recording\n\n')
f.close()                           # close the file
led2.off()                          # turn led off
led3.off()                          # turn led off
