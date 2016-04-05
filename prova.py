__author__ = 'sc04'

import datetime
import time
buf = bytearray(100)                # create a buffer of 100 bytes
f = open("sadata.dat", "a")    # open the file for writing
k=0
lines=[]
while (k<10):
    k=k+1
    [x, y, z] = [0,0,0]
    #buf=[k,k,k,k,k,k,k,k,k,]
    t = datetime.datetime.now().time()    # get time in ms
    #f.write("{} {} {} {}\n".format(t, buf, x, y, z)) # write muscl_input and x,y,z
        #f.write("{} {} {} {}\n".format(time, val, x, y, z)) # write muscl_input and x,y,z
    lines.append('{} {} {} {}\n'.format(t,buf, x, y, z))# FASTER, BUT then lines gets quite big...
    time.sleep(0.001)                    # apparently, for stability
    #for val in buf:                # REPL: loop and print values
    #    print(val)
f.writelines(lines)
f.close()                           # close the file


