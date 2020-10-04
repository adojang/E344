import numpy as np

def calibrate(time, amplitude):
        
    ######################################
    # Enter calibration code here:
    # AJ van Wijk 21786275
    ######################################
        
    x = (amplitude[0]-0.446)*2.131 + 34 # This line will is to be replaced with your calibration code.

    temperature = int(round(x))
 
    ######################################
        
    return temperature
        
