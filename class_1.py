#%% MODULE BEGINS
module_name = "class_1"

'''
Version: .01

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
import config
import numpy  as np
import pandas as pd
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


#%% CONFIGURATION               ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~



#%% INITIALIZATIONS             ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~


#%% DECLARATIONS                ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

#Global declarations Start Here



#Class definitions Start Here
class parentCSV:
    def __init__(self):
        print("Parent 1 initialized.")
    #end

    def doSomething(self):
        print("parent1")
    #end
#end

class childCSV(parentCSV):
    filepathtest = ""
 
    def __init__(self, csv):
        self.filepath = csv
        self.df = pd.read_csv(csv)
        print("Child 1 initialized.")
    #end

    def csvToDataFrame(self, filepath):
        self.df = pd.read_csv(filepath)
    #end

    def generateDataFrame(self):
        self.df = pd.read_csv(self.filepath)
    #end

    def setFilepath(self, filepath):
        self.filepath = filepath
    #end

    def printDataFrame(self):
        print(self.df)
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
   