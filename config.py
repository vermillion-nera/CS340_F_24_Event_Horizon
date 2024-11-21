#%% MODULE BEGINS
module_name = 'config'

'''
Version: <***>

Description:
    <***>

Authors:
    <***>

Date Created     :  <***>
Date Last Updated:  <***>

Doc:
    <***>

Notes:
    <***>
'''

#%% IMPORTS                    ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
if __name__ == "__main__":
   import os
   #os.chdir("./../..")
#

#custom imports


#other imports
from   copy       import deepcopy as dpcpy
import numpy as np
import pandas as pd
import os
import logging

'''
from   matplotlib import pyplot as plt
import mne
import numpy  as np 
import os
import pandas as pd
import seaborn as sns
import logging
'''
#%% USER INTERFACE              ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~


#%% CONSTANTS                   ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
TEST = True


#%% CONFIGURATION               ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
logging.basicConfig(          #sets up root logger
    filename = "log_1.log",
    encoding = "utf-8",
    filemode = "a",
    format = "{asctime} - {levelname} - {message}",
    style = "{",
    datefmt = "%Y-%m-%d %H:%M",

)

#%% INITIALIZATIONS             ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~


#%% DECLARATIONS                ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

#Global declarations Start Here



#Class definitions Start Here
class userInput:
    def __init__(self):
        print("User Input initialized.")
    #end

    def askForInput(self, message="Give input"):
        return input(message+":\t")
    #end
#end


#Function definitions Start Here
def main():
    pass
#

#%% MAIN CODE                  ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#Main code start here



#%% SELF-RUN                   ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#Main Self-run block
if __name__ == "__main__":
    
    print(f"\"{module_name}\" module begins.")
    
    #TEST Code
    main()
    