#%% MODULE BEGINS
module_name = 'main'

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
import config
import class_1
import class_2
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


#%% CONFIGURATION               ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~


#%% INITIALIZATIONS             ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
input = config.userInput()
classCSV = class_1.childCSV("CSV_sterilizer/Student_performance_data.csv")
classPickle = class_2.child()


#%% DECLARATIONS                ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
handlingCSV = True

#Global declarations Start Here



#Class definitions Start Here


#Function definitions Start Here
def enactCommand(command):
    global handlingCSV
    if (command == "print"):
        if (handlingCSV):   classCSV.printDataFrame()
        else:               classPickle.printPickle()
    elif (command == "print columns"):
        if (handlingCSV):   print(classCSV.requestColumn(input.askForInput("Column to print")))
        else:               print("Unimplemented.")
    elif (command == "datatype" or command == "data type"):
        if (handlingCSV):   print("Handling CSV's.")
        else:               print("Handling Pickles.")
    elif (command == "switch"):
        handlingCSV = not handlingCSV
        if (handlingCSV):   print("Handling CSV's.")
        else:               print("Handling Pickles.")
    elif (command == "csv"):
        handlingCSV = True
        print("Handling CSV's.")
    elif (command == "pickle"):
        handlingCSV = False
        print("Handling Pickles.")
    elif (command == "exit"):
        print("Exiting program...")
        print("Thank you for using this program!")
    else:
        print("'"+command+"' is not a valid command.")
    #end
#end

def main():
    command = "initial"
    while (command != "exit"):
        command = input.askForInput()
        enactCommand(command)
    #end
    
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
    