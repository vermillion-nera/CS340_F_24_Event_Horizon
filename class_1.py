#%% MODULE BEGINS
module_name = "class_1"

'''
Version: 1.0

Description:
    Holds two classes designed for handling Pandas
    DataFrames, and converting CSV's to DataFrames.

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
import config
import numpy  as np
import pandas as pd
import logging
import sys
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
logger = logging.getLogger(__name__)



#%% INITIALIZATIONS             ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~


#%% DECLARATIONS                ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

#Global declarations Start Here



#Class definitions Start Here
class parentCSV:
    def __init__(self, dataframe):
        self.df = dataframe
        self.shaped = dataframe
        print("CSV parent initialized.")
    #end

    def getDataFrame(self):
        return self.df
    #end

    def printColumns(self, colNames): # Inputs a string (i.e. "Age GPA")
        print(self.df[colNames.split(" ")])
    #end

    def printRows(self, rowIndices): # Inputs a string (i.e. "4:9")
        mask = 0 < self.shaped.index
        num1 = num2 = ""
        isOperator = False
        for char in rowIndices:
            if (char == " "): break
            elif (char.isnumeric()): 
                if (not isOperator): num1 += char
                else: num2 += char
            elif (char == ":"):
                isOperator = True
            #end
        #end
        if (num1 != ""): num1 = int(num1)
        if (num2 != ""): num2 = int(num2)
        if (isOperator):
            if (num1 != "" and num2 == ""): # "4:"
                mask = num1 <= self.shaped.index
            elif (num1 == "" and num2 != ""): # ":6"
                mask = self.shaped.index < num2
            elif (num1 != "" and num2 != ""): # "4:6"
                mask = ((num1 <= self.shaped.index) & (self.shaped.index < num2))
            else: # ":"
                mask = 0 < self.shaped.index
            #end
            print(self.shaped[mask])
        else:
            print(self.shaped.iloc[[num1]])
        #end
    #end

    def printQuery(self, myQuery): # Inputs a query. Not for the faint of heart.
        print(self.shaped.query(myQuery))
    #end

    def filterColumns(self, colNames): # Inputs a string (i.e. "Age GPA")
        self.shaped = self.shaped[colNames.split(" ")]
    #end

    def filterRows(self, rowIndices): # Inputs a string (i.e. "4:9")
        mask = 0 < self.shaped.index
        num1 = num2 = ""
        isOperator = False
        for char in rowIndices:
            if (char == " "): break
            elif (char.isnumeric()): 
                if (not isOperator): num1 += char
                else: num2 += char
            elif (char == ":"):
                isOperator = True
            #end
        #end
        if (num1 != ""): num1 = int(num1)
        if (num2 != ""): num2 = int(num2)
        if (isOperator):
            if (num1 != "" and num2 == ""): # "4:"
                mask = num1 <= self.shaped.index
            elif (num1 == "" and num2 != ""): # ":6"
                mask = self.shaped.index < num2
            elif (num1 != "" and num2 != ""): # "4:6"
                mask = ((num1 <= self.shaped.index) & (self.shaped.index < num2))
            else: # ":"
                mask = 0 < self.shaped.index
            #end
            self.shaped = self.shaped[mask]
        else:
            self.shaped = self.shaped.iloc[[num1]]
        #end
    #end

    def filterQuery(self, myQuery): # Inputs a query. Not for the faint of heart.
        self.shaped = self.shaped.query(myQuery)
    #end

    def resetShape(self):
        self.shaped = self.df
    #end

    def printDataFrame(self):
        print(self.shaped)
    #end

    def printDataFrameOriginal(self):
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
    
    logging.warning("hello")