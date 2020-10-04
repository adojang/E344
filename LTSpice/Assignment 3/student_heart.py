import numpy as np

def calibrate(time, amplitude):
        
    ######################################
    # Enter calibration code here:
    # AJ van Wijk 21786275
    ######################################

    samples = len(amplitude)
    newpulse =0
    oldstate = True
    newstate = False
    oldpulse =0
    counter =0
    totalperiod =0

    for x in range(samples):

       if amplitude[x] > 2.5:

          newstate = True
       else:
          newstate = False

       if oldstate == False and newstate == True: #Change from High to Low happens Here or Low to High

          newpulse = x
          period = newpulse - oldpulse
          if counter > 0: #This disregards the first value which is not a viable value.
             totalperiod += period
          
          counter += 1 #Counter keeps track of how many pulses there are
          
       #These allow us to calculate the difference
       oldstate = newstate
       oldpulse = newpulse

    avg = (totalperiod/(counter-1))/1000 #Gives us the average period in SECONDS
    bpm = 60/avg #Changes seconds to BPM

    ######################################
  
    return int(round(bpm))
        
