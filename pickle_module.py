#%% MODULE BEGINS
module_name = "pickle_module"

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
Date Last Updated:  11/20/2024

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
import logging
import pandas as pd
import dataframe_module
from config import csv_path


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



#%% INITIALIZATIONS             ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
logger = logging.getLogger(__name__)

dataframe = pd.read_csv(csv_path)




#%% DECLARATIONS                ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

#Global declarations Start Here



#Class definitions Start Here
class pickle_manager:
    def __init__(self, pickle_File):
        self.pickle_File = pickle_File
       

        print("Pickle parent initialized.")
    #end
    def create_Pickle(self, df):

        try:
            df.to_pickle(self.pickle_File)
            logging.info("Successfully created pickle file")

        except Exception as e:
            print(f"Error pickling data: {e}")
            logging.error("Error pickling data.")
            
    def load_Pickle(self):
        try:
            df = pd.read_pickle(self.pickle_File)
            print(f"Loaded dataframe from {self.pickle_File}")
            return df
        except Exception as e:
            print("Error loading pickle as a dataframe from {self.pickle_File}: {e}")
            logging.error("Error loading pickle as a dataframe from {self.pickle_File}: {e}")
            
        
    def print_Pickle(self):
        df = self.load_Pickle()
        if df is not None:
            print(df)
            logging.info("Printed pickle.")
        else:
            print("No data to display from pickle")
            logging.info("No data to display from pickle")
        
    #end
#end

class math_wizard(pickle_manager):
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
    manager = pickle_manager("pickle_dataframe.pkl")
    manager.create_Pickle(dataframe)
    manager.print_Pickle()