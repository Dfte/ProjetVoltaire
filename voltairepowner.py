#!/usr/bin/python3
#-.- coding: utf-8 -.-
#voltairepowner.py

#Librairies needed
import os
import pymouse
import pykeyboard
import time 
import argparse
import sys

# Colors code
white="\033[1;37m"
grey="\033[0;37m"
purple="\033[0;35m"
red="\033[1;31m"
green="\033[1;32m"
yellow="\033[1;33m"
purple="\033[0;35m"
blue="\033[1;34m"
end= "\033[m"


#This function will print you the coordinates of the point you're aiming at with your mouse.
#Once the correct place choosen you will have to Ctrl + c in order to exit the loop.
def getLocation():
	while 1 :
		try:
			point=mouse.position()
			print(point)
			time.sleep(1)
		except KeyboardInterrupt :
			return point


#This function is the scripting part that auto clicks wherever you specified.
#It will click every 'timing' secondes at the point located at (x, y).
#If you Ctrl + C, it will exit the infinite loop and called the leave() function.
def launchScripting(x,y,timing):
	#Let's get a quick idea of how many times you saved using my tool
	start=time.time()
	print('''%s\n[-] Auto Clicking launched on point (%s , %s)
[-] Will click every %s secondes.%s'''%(white,x,y,timing,end))
	while 1 :
		try :
			mouse.move(x,y)
			mouse.click(x,y)
			time.sleep(timing)
		except KeyboardInterrupt :
			leave(start)
	return 0

#This function prints the leaving banner and exits the programm.
def leave(start) :
	finish=time.time()
	print('''%s
        _          _     _       __                                           _ 
  /\/\ (_)___  ___| |__ (_) ___ / _|   /\/\   __ _ _ __   __ _  __ _  ___  __| |
 /    \| / __|/ __| '_ \| |/ _ \ |_   /    \ / _` | '_ \ / _` |/ _` |/ _ \/ _` |
/ /\/\ \ \__ \ (__| | | | |  __/  _| / /\/\ \ (_| | | | | (_| | (_| |  __/ (_| |
\/    \/_|___/\___|_| |_|_|\___|_|   \/    \/\__,_|_| |_|\__,_|\__, |\___|\__,_|
                                                               |___/            
\n[!] I'm glad to annonce you that you saved %s seconds of your time\n%s%s[-] If you enjoyed the tool, please go to https://whiteflagfr.wordpress.com.
[-] You can also follow me on : https://www.facebook.com/DefteWhiteFlag/\n%s''' % (red,str(finish-start),end,white,end))
	sys.exit()

#The argparse module allows us to interact with command lin easily.
#There is only one option (time) since the tool is fully automated.
#Note that you are not forced to use the -t since it has default value.
parser=argparse.ArgumentParser()
parser.add_argument('-t', help='Specify the time before each clicks.', dest='time', type=int)
args=parser.parse_args() 

#Let's clear the command line window.
os.system("clear")

#Printing our awesome welcome banner !! :D
print('''%s
                                                       (                                         
                (       )                              )\ )                                      
 (   (          )\   ( /(      )   (    (       (     (()/(         (  (               (    (    
 )\  )\    (   ((_)  )\())  ( /(   )\   )(     ))\     /(_))   (    )\))(     (       ))\   )(   
((_)((_)   )\   _   (_))/   )(_)) ((_) (()\   /((_)   (_))     )\  ((_)()\    )\ )   /((_) (()\  
\ \ / /   ((_) | |  | |_   ((_)_   (_)  ((_) (_))     | _ \   ((_) _(()((_)  _(_/(  (_))    ((_) 
 \ V /   / _ \ | |  |  _|  / _` |  | | | '_| / -_)    |  _/  / _ \ \ V  V / | ' \)) / -_)  | '_| 
  \_/    \___/ |_|   \__|  \__,_|  |_| |_|   \___|    |_|    \___/  \_/\_/  |_||_|  \___|  |_|   
                                                                                                                 
%s%s[>] Written by Defte%s''' % (white,end,yellow,end))
print('''%s[!] First of all point at the sentence using your cursor then press Ctrl + C.%s'''%(red,end))

#Initialise the mouse object that we will use in order to click and locate the mouse cursor.
mouse=pymouse.PyMouse()
#Initialize the defaulttime between two clicks.
defaulttime=25

#First of all we call the getlocation() function.
#We receive the cursor coordinates (x,y ) and send it to the launchScripting() function that will auto clicks.
#If you don't specify the -t option then it will use the defaulttime value.
point=getLocation()
if args.time == None :
	launchScripting(point[0], point[1], defaulttime)
else :
	launchScripting(point[0],point[1], args.time)

