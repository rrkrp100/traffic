#!Python3

def turn_red(light_num):
    """Turns the specific Light Red"""
    print("RED: %s"%(light_num))



def turn_green(light_num,sig_t):
    """Turns the light Green, rest are turned Red;
     Also calls the camera activatio functions """

    print("Green = Signal %s\n"%(light_num))

    for i in range(1,5):
        if(i!=light_num):
            turn_red(i)

    motion.motion(sig_t,time.time())        #Run for "Sig_t" secs, starting now.

def signal(turn):
    """The signal algorithm that starts the
    cameras as well as regulates the lights"""
    veh,amb = counter()                              # Returns a tuple of dictionaries for the number of vehicles and ambulances on all the roads

    try:
        while(1):
            print("****************************** Signal Change **************************************")
            print(" \n\n Vehicles:%s\nAmbulances: %s\n"%(veh,amb))
            turn= (turn)%4 +1

            sig_time = max(15,min(45,(veh[turn]*3)))        # Alloting time acording to the vehicles standing at this Signal
            for i in range(1,5):
                if(amb[i]!=0 and turn!= i):
                    sig_time = max(15,(sig_time-5))         #deducting 5 seconds of time for every ambulance waiting on another signal
            print("Signal will change in %s secs"%(sig_time))

            turn_green(turn,sig_time-2)                                # Turn the selected light green

            #for i in range(1,sig_time-2):
            #    print("Sec:",str(i),end="\r")
            #    time.sleep(1)

            #time.sleep(sig_time-2)
            veh,amb = counter()                              # Returns a tuple of dictionaries for the number of vehicles and ambulances on all the roads

    except(KeyboardInterrupt):
        print("\nSystem will exit user on demand...\n")


turn = 1
import time, motion
from random import *
from counter import *
signal(turn)
