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
logger = logging.getLogger(__name__)


#%% INITIALIZATIONS             ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~


#%% DECLARATIONS                ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

#Global declarations Start Here



#Class definitions Start Here
class parentCSV:
    def __init__(self, dataframe):
        self.df = dataframe
        print("CSV parent initialized.")
    #end

    def requestColumn(self, colName):
        print(self.df[[colName]])
    #end

    def printDataFrame(self):
        print(self.df)
    #end
#end

class childCSV(parentCSV):
    def __init__(self, csv):
        self.filepath = csv
        super().__init__(pd.read_csv(csv))
        print("CSV child initialized.")
    #end

    def setFilepath(self, filepath):
        self.filepath = filepath
    #end

    def csvToDataFrame(self, filepath):
        self.filepath = filepath
        self.df = pd.read_csv(filepath)
    #end

    def generateDataFrame(self):
        self.df = pd.read_csv(self.filepath)
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
    logger.error("test")
   