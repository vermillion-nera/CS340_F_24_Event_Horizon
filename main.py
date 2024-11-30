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
import config
import dataFrameModule
import pickleModule

#other imports
from   copy       import deepcopy as dpcpy
import os
import logging
import sys

#%% USER INTERFACE              ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~


#%% CONSTANTS                   ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~


#%% CONFIGURATION               ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~





#%% INITIALIZATIONS             ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
input = config.userInput()
classCSV = dataFrameModule.csvHandler("INPUT/Student_performance_data.csv")
classPickle = pickleModule.child()
commandList = (
    "help",
    "print",
    "print unshaped",
    "print columns",
    "print rows",
    "filter columns",
    "filter rows",
    "filter reset",
    "datatype",
    "switch",
    "csv",
    "pickle",
    "exit",
)


#%% DECLARATIONS                ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
handlingCSV = True

#Global declarations Start Here



#Class definitions Start Here


#Function definitions Start Here
def enactCommand(command):
    global handlingCSV
    global commandList
    # TODO: Implement "subcommands" of nested if statements. For instance, if (print), if (unshaped), elif (columns), etc
    # Might be able to do this by split()ing our command into arguments separated by spaces
    if (command == "help" or command == "commands"):
        print("----------------------")
        print("Available commands:")
        for item in commandList:
            print("> "+item)
        print("----------------------")
    elif (command == "print"):
        if (handlingCSV):   classCSV.printDataFrame()
        else:               classPickle.printPickle()
    elif (command == "print unshaped" or command == "print original"):
        if (handlingCSV):   classCSV.printDataFrameOriginal()
        else:               classPickle.printPickle()
    elif (command == "print columns" or command == "print column"):
        if (handlingCSV): classCSV.printColumns(input.askForInput("Columns to print"))
        else: print("Unimplemented.")
    elif (command == "print rows" or command == "print row"):
        if (handlingCSV): classCSV.printRows(input.askForInput("Rows to print"))
        else: print("Unimplemented.")
    elif (command == "filter columns" or command == "filter column"):
        if (handlingCSV):
            answer = input.askForInput("Columns to filter")
            filter = answer.split(" ")
            classCSV.filterColumns(filter)
            print("Filtered by '"+answer+"' columns.")
        else:
            print("Unimplemented.")
        #end
    elif (command == "filter rows" or command == "filter row."):
        if (handlingCSV):
            answer = input.askForInput("Rows to filter")
            classCSV.filterRows(answer)
            print("Filtered by '"+answer+"' rows.")
        else:
            print("Unimplemented.")
        #end
    elif (command == "filter reset"):
        if (handlingCSV):
            classCSV.resetShape()
            print("Dataframe filter reset.")
        else:
            print("Unimplemented.")
        #end
    elif (command == "query"):
        if (handlingCSV):
            answer = input.askForInput("Query")
            classCSV.filterQuery(answer)
            print("Filtered by '"+answer+"'.")
        else:
            print("Unimplemented.")
        #end
    elif (command == "datatype" or command == "data type" or command == "type"):
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
    elif (command == "exit" or command == "e"):
        print("Exiting program...")
        print("Thank you for using this program!")
    else:
        print("'"+command+"' is not a valid command.")
    #end
#end

def main():
    command = "initial"
    while (command != "exit" and command != "e"):
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
  