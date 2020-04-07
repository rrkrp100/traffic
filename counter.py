#!Python3

def counter():
    """The counter stub, using randint
     to simulate the actual vehicle counter function"""
    global ambulance
    #for i in vehicles:
     #    vehicles[i]= randint(1,50)
    #with open("../lane1.txt","r") as f:
    #        vehicles = int(f.read())
    vehicles=randint(0,53)
    for i in ambulance:
        ambulance[i]= randint(0,3)

    return (vehicles,ambulance)

def reset_counters(green_light_num):
    """Resets the count of vehicles to zero after every signal change"""
    ambulance[green_light_num]=0



def cams(green_light_num,signal_t):
    """Activates the motion detector cameras and resets the greened signal's counter"""
    from threading import Thread

    reset_counters(green_light_num)

    for m in motion_cams:
        if(m!=(green_light_num+1)%5):
            #Thread(target=start, args=(m,))
            print("Motion cam: ",str(m)," ON")
            motion.motion(sigt=signal_t,strt=time.time(),turn = green_light_num,flag=0)

#if __name__== "__main__":
from random import randint
import motion
#vehicles={1:0,2:0,3:0,4:0}
ambulance={1:0,2:0,3:0,4:0}
motion_cams = {0,1,2,3,4}
