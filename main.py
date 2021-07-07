import time
import board
import adafruit_bh1750
import subprocess
from Brightness import BrightnessTable
import wifi

i2c = board.I2C()
sensor = adafruit_bh1750.BH1750(i2c)

bt = BrightnessTable()


if __name__ == "__main__":
    while True:

        #Readfile -> check if there is manual setting
        lux = sensor.lux
        #print("%.2f Lux" % sensor.lux)
        brightness = min(100,int(lux/3))  #conversion lux -> brightness
        with open("./brightness.txt","r") as file:
            data = file.read().replace('\n','').split(',')
            #print(data)
        if (data[0]=="manual"):
            
            bt.update(brightness,int(data[1]))
            bt.get_brightness(brightness)
            process = subprocess.run(["ddcutil", "setvcp", "10", str(data[1])])
            with open("./brightness.txt","w") as file:
                file.write("auto, " + str(data[1]))
        else:
            realbrightness = int(bt.get_brightness(brightness))
            bt.plot()
            process = subprocess.run(["ddcutil", "setvcp", "10", str(realbrightness)])


        #pass brightness to monitor
        print(process)
        time.sleep(2)    





