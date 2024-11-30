#%% MODULE BEGINS
module_name = "pickleModule"

'''
Version: 0.1

Description:
    WIP class meant to handle Pickle files.

Authors:
    Christian Bankovic
    Wren Caillouet
    Maxwell Benson
    Brian Britton

Date Created     :  11/20/2024
Date Last Updated:  11/30/2024

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
import dataFrameModule

#other imports
from   copy       import deepcopy as dpcpy
import logging
import pickle
import pandas as pd


'''
from   matplotlib import pyplot as plt
import mne
import numpy  as np 
import os
import pandas as pd
import seaborn as sns
import logging
import sys
'''
#%% USER INTERFACE              ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~


#%% CONSTANTS                   ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~


#%% CONFIGURATION               ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
csv_path = "INPUT/Student_performance_data.csv"
dataframe = pd.read_csv(csv_path)


#%% INITIALIZATIONS             ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
dataFrameHandler = dataFrameModule.dataFrameHandler(dataframe)
csvHandler = dataFrameModule.csvHandler(csv_path)

#%% DECLARATIONS                ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

#Global declarations Start Here



#Class definitions Start Here
class pickleHandler:
    def __init__(self, pickle):
        self.pk = pickle
        test = True

        print("Pickle parent initialized.")
    #end

    def create_Pickle_File(self):
        print("DO SOMETHING")

    def printPickle(self):
        print("printingPickle")
    #end
#end

class mathWizard(pickleHandler):
    def __init__(self):
        test = True
        print("Pickle child initialized.")
    #end

    def inputPickle(self, pickle):
        print("this is supposed to input a pickle")
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
   