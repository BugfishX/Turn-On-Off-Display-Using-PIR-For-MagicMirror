# Turn On/Off Display Using PIR For MagicMirror
## Description

Hi everyone,
I created a python script to turn on or off the display using PIR to avoid BurnIn for example.

The script is checking the PIRs output all time.  
If no motion is detected the display turns off/ stays off.  
If motion is detected the display will turn on and stays on for entered time.  

The script will start Magic Mirror and is checking the PIR then all time until quit with Ctrl + C

## How To Install

Just create a new file (I called it pir.py) in your /home/pi and paste the script into it as listed.  
Check which GPIO you will use at set it to yours.  
Set time.sleep () as you like.  
With python pir.py you can run the script then.

## The Script

```Python
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
    input=GPIO.input(PIR_Sensor)

#set time.sleep for how long display stays on/off at least
#no motion so display turns off
    if input==0:
        print ("Not Sensing Motion", time.strftime("%d.%m.%Y %H:%M:%S"))
        os.system(display_power_off)
        time.sleep(1.0)
#motion detected so display turns on

    elif input==1:              
        print ("Motion Detected", time.strftime("%d.%m.%Y %H:%M:%S"))
        os.system(display_power_on)
        time.sleep(30.0)
  ```
     
 ## Configuration
 | Option  | Description |
|----------|----------|
| PIR_Sensor  | The GPIO you will use (example: GPIO 23 is Pin 16 on RPi 3)  |
| time.sleep()  | Works as a timer. There are two "time.sleep()"s. One is for time waiting until display turns on  and the other until display turns off   |
   
<br><br><br>
This is my first repository here so please show mercy :smile: 
If you have any suggestions or tips > tell me!
