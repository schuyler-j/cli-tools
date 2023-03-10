import os
import time
import glob
import math
from math import pi
import re
import random
from PIL import Image
import sys

class image():
    pntr = 0
    def main(self):

        #term colours
        OKBLUE = '\033[94m'
        OKRED = '\033[93m'
        OKGREEN = '\033[92m'
        OKBLACK = '\033[1m'

        COLOR_ONE = ''
        COLOR_TWO = ''

        size = (120, 120)

        fileImg = 'img.png'
        image1 = Image.open(fileImg)

        f1 = image1.resize(size)
        f1.save("img.png")
        f1.close()

        imgROT = 'imgROT.png'

        #open rotated image
        image1 = Image.open(imgROT)
        pix_access = image1.load()

        if self.pntr == 0:
            print("Rotating Image...")
        else:
            print("Printing...")
        time.sleep(1)

        #chars for drawing
        low  = "@"
        med  = ","
        high = "-"
        low_med = "o"
        high_med = "*"
        high_high = "."
        low_low = "&"
        payload = ""

        if self.pntr == 0:
            width, height = 1, 1
        else:
            width, height = f1.size

        mul = 1
        for x in range(width):
            for y in range(height):

                # list for rgb
                a = pix_access[x, y][0]
                b = pix_access[x, y][1]
                c = pix_access[x, y][2]

                a = a *mul 
                b = b *mul 
                c = c *mul 

                total = 765*mul

                #(80, 35, 65, 50)
                #(85, 65, 55, 45
                #(85, 70, 35, 20)
                #(80, 65, 45, 25)

                # contrast levels 
                # alter these values for different contrasts
                hh =(total*0.90)
                t = (total*0.75)
                hm =(total*0.65)
                m = (total*0.45)
                l = (total*0.25)
                ll =(total*0.15)

                chk = total-(a+b+c)

                # calculate brightness to see where to place char
                if chk >= t:
                    payload = high
                elif chk < hm and chk > m:
                    payload = med
                elif chk < l:
                    payload = low
                elif chk < t and chk > hm:
                    payload = high_med
                elif chk < m and chk > l:
                    payload = low_med
                elif chk > hh:
                    payload = high_high
                elif chk < ll:
                    payload = low_low
                with open("picture.txt", "a") as fileHop:
                    fileHop.writelines(payload) 

                    #DEFAULT COLORS
                sys.stdout.write(payload)
                sys.stdout.flush()

            with open("picture.txt", "a") as fileHop:
                fileHop.writelines("\n")

        self.pntr = 1
        self.rotate()

    def rotate(self):
        fImg = 'img.png'
        image = Image.open(fImg)
        
            #ROTATE
        angle = 90
        f0 = image.rotate(angle)
        f0.save("imgROT.png")

        self.main() # begin loop     
    
    def rename(self):
        fileList = glob.glob("./*")
        latestFile = max(fileList, key=os.path.getctime)
        latestFile = latestFile.split('\\')
        rFile = latestFile[1]

        command = ("rename " + "\"" + "./" + rFile + "\"" + " img.png")
        os.system(command)
        print("finished.")
        self.rotate()

if __name__ == "__main__":

    a = image()
    a.rotate()





