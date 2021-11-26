#Import Python modules
import RPi.GPIO as GPIO
import time
import os
from multiprocessing import Process

#def var
PIR_Sensor = 23
display_power_on= "vcgencmd display_power 1"
display_power_off= "vcgencmd display_power 0"

#set GPIOs to GPIO-Number
GPIO.setmode(GPIO.BCM)
#disable GPIO warnings
GPIO.setwarnings(False)
#def IN and OUT
GPIO.setup(PIR_Sensor, GPIO.IN)

#function to start MM
def start_MM ():
    print ">> START MAGIC MIRROR <<"
    start_mm = "cd MagicMirror; npm run start"
    os.system(start_mm)
    print ">> MAGIC MIRROR STARTED <<"
    
#MAIN until abort with Ctrl + C
p1 = Process(target=start_MM)
p1.start()

while True:
    input=GPIO.input(23)

#set time.sleep for how long display stays on/off at least
#no motion so display turns off
    if input==0:
        print ("Not Sensing Motion", input, time.strftime("%d.%m.%Y %H:%M:%S"))
        os.system(display_power_off)
        time.sleep(1.0)
#motion detected so display turns on

    elif input==1:              
        print ("Motion Detected", input, time.strftime("%d.%m.%Y %H:%M:%S"))
        os.system(display_power_on)
        time.sleep(30.0)
