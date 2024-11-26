#%% MODULE BEGINS
module_name = 'main'

'''
Version: 1.0

Description:
    Imports the classes from class_1, class_2, and
    config. Also runs the entire program, asking
    the user for commands and enacting them until
    the user types 'exit'.

Authors:
    Christian Bankovic
    Wren Caillouet
    Maxwell Benson
    Brian Britton

Date Created     :  11/20/2024
Date Last Updated:  11/25/2024

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
# TODO: Move custom modules heree
# from config import TEST # example import variable

#other imports
from   copy       import deepcopy as dpcpy
import pandas as pd
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
# TODO: Possibly place user input here

#%% CONSTANTS                   ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# TODO: use "nonlocal" and "private like" somewhere

#%% CONFIGURATION               ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
csv_path = "CSV_sterilizer/Student_performance_data.csv"
dataframe = pd.read_csv(csv_path)

#%% INITIALIZATIONS             ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
input = config.userInput()
parentCSV = class_1.parentCSV(dataframe)
classCSV = class_1.childCSV("CSV_sterilizer/Student_performance_data.csv")
classPickle = class_2.child()
commandDict = { # TODONE: Put this into a dictionary
    0: "help",
    1: "print",
    1.01: "[optional]:",
    1.02: "unshaped",
    1.03: "columns",
    1.04: "rows",
    1.05: "query",
    2: "filter",
    2.01: "columns",
    2.02: "rows",
    2.03: "query",
    2.04: "reset",
    3: "datatype",
    4: "switch",
    5: "csv",
    6: "pickle",
    7: "exit",
}


#%% DECLARATIONS                ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
handlingCSV = True

#Global declarations Start Here



#Class definitions Start Here


#Function definitions Start Here
def enactCommand(command): # TODO: Implement try catch statement, and if it catches an error, log it and continue on (not enacting a command shouldn't break ).
    global handlingCSV
    global commandList
    global commandDict
    commandArgs = command.split(" ")

    # TODONE: Implement "subcommands" of nested if statements. For instance, if (print), if (unshaped), elif (columns), etc
    # Might be able to do this by split()ing our command into arguments separated by spaces
    if (len(commandArgs) == 0 or command == ""):
        print("Please type a command.")
    elif (commandArgs[0] == "help" or commandArgs[0] == "commands"): # TODONE: Perhaps make help for subcommands?
        print("----------------------")
        if (len(commandArgs) > 1):
            if (commandArgs[1] == "help"):
                print("Available 'help' subcommands:")
                for key in commandDict:
                    if (key%1 == 0):
                        print("> "+commandDict[key])
                    #end
                #end
            else:
                commandKey = -1
                hasSubcommands = False
                for key in commandDict:
                    if (commandDict[key] == commandArgs[1] and key%1 == 0):
                        commandKey = key
                    elif ((key - commandKey) > 0 and (key - commandKey) < 1):
                        if (not hasSubcommands):
                            print("Available '"+commandArgs[1]+"' subcommands:")
                        #end
                        hasSubcommands = True
                        print("> "+commandDict[key])
                    #end
                #end
                if (not hasSubcommands):
                    print("No subcommands for '"+commandArgs[1]+"'.")
                #end
            #end
        else:
            print("Available commands:")
            for key in commandDict:
                if (key%1 != 0):
                    print("  > "+commandDict[key])
                else:
                    print("> "+commandDict[key])
                #end
            #end
        #end
        print("----------------------")
    # -------------- TEST FUNCTIONS --------------
    elif (command == "print histogram" or command == "plot histogram"):
        if handlingCSV:
            column_name = input.askForInput("Enter column name for histogram/bar chart: ")  
            parentCSV.plotAllColumnsHist(column_name, save=True)
        else:
            print("Unimplemented.")
        #end
    elif (command == "studyTime vs parentalSupport"):
        classCSV.Violin_StudyTimeWeekly_vs_ParentalSupport()
    elif (command == "GPA vs Gender"):
        classCSV.Violin_GPA_vs_Gender()
    elif (command == "Absences vs GradeClass"):
        classCSV.Box_Absences_vs_GradeClass()
    elif (command == "GPA vs ParentalEducation"):
        classCSV.Box_GPA_vs_ParentalEducation()
    elif (command == "StudyTimeWeekly vs GPA"):
        classCSV.scatter_StudyTimeWeekly_vs_GPA()
    elif (command == "Age vs Absences"):
        classCSV.scatter_Age_vs_Absences()
    # -------------- PRINTING --------------
    elif (commandArgs[0] == "print"):
        if (len(commandArgs) == 1): # default
            if (handlingCSV):   classCSV.printDataFrame()
            else:               classPickle.printPickle()
        elif (commandArgs[1] == "unshaped" or commandArgs[1] == "original"):
            if (handlingCSV):   classCSV.printDataFrameOriginal()
            else:               classPickle.printPickle()
        elif (commandArgs[1] == "columns" or commandArgs[1] == "column"):
            if (handlingCSV):
                answer = ""
                if (len(commandArgs) > 2):
                    answer = " ".join(commandArgs[2:])
                else:
                    answer = input.askForInput("Columns to print")
                #end
                if (answer == "exit"):  print("Skipping print.")
                else:                   classCSV.printColumns(answer)
            else:
                print("Unimplemented.")
            #end
        elif (commandArgs[1] == "rows" or commandArgs[1] == "row"):
            if (handlingCSV):
                answer = ""
                if (len(commandArgs) > 2):
                    answer = " ".join(commandArgs[2:])
                else:
                    answer = input.askForInput("Rows to print")
                #end
                if (answer == "exit"):  print("Skipping print.")
                else:                   classCSV.printRows(answer)
            else:
                print("Unimplemented.")
            #end
        elif (commandArgs[1] == "query"):
            if (handlingCSV):
                answer = ""
                if (len(commandArgs) > 2):
                    answer = " ".join(commandArgs[2:])
                else:
                    answer = input.askForInput("Query")
                #end
                if (answer == "exit"):  print("Skipping print.")
                else:                   classCSV.printQuery(answer)
            else:
                print("Unimplemented.")
            #end
        else:
            print("'"+command+"' is not a valid print command")
        #end
    # -------------- FILTERING --------------
    elif (commandArgs[0] == "filter"):
        if (len(commandArgs) == 1):
            print("'filter' must come with a subcommand. Valid subcommands include:")
            print("> 'columns'")
            print("> 'rows'")
            print("> 'query'")
            print("> 'reset'")
        elif (commandArgs[1] == "columns" or commandArgs[1] == "column"):
            if (handlingCSV):
                answer = ""
                if (len(commandArgs) > 2):
                    answer = " ".join(commandArgs[2:])
                else:
                    answer = input.askForInput("Columns to filter")
                #end
                if (answer == "exit"):
                    print("Skipping filter.")
                else:
                    classCSV.filterColumns(answer)
                    print("Filtered by '"+answer+"' columns.")
                #end
            else:
                print("Unimplemented.")
            #end
        elif (commandArgs[1] == "rows" or commandArgs[1] == "row"):
            if (handlingCSV):
                answer = ""
                if (len(commandArgs) > 2):
                    answer = " ".join(commandArgs[2:])
                else:
                    answer = input.askForInput("Rows to filter")
                #end
                if (answer == "exit"):
                    print("Skipping filter.")
                else:
                    classCSV.filterRows(answer)
                    print("Filtered by '"+answer+"' rows.")
                #end
            else:
                print("Unimplemented.")
            #end
        elif (commandArgs[1] == "query"):
            if (handlingCSV):
                answer = ""
                if (len(commandArgs) > 2):
                    answer = " ".join(commandArgs[2:])
                else:
                    answer = input.askForInput("Query")
                #end
                if (answer == "exit"):
                    print("Skipping filter.")
                else:
                    classCSV.filterQuery(answer)
                    print("Filtered by '"+answer+"'.")
                #end
            else:
                print("Unimplemented.")
            #end
        elif (commandArgs[1] == "reset"):
            if (handlingCSV):
                classCSV.resetShape()
                print("Dataframe filter reset.")
            else:
                print("Unimplemented.")
            #end
        else:
            print("'"+command+"' is not a valid filter command")
        #end
    # -------------- EXPORTING --------------
    elif (commandArgs[0] == "export"): # TODO: Allow for exporting the filtered table into a CSV/TXT file
        print("Unimplemented.")
    # -------------- CLASS SWAPPING --------------
    elif (commandArgs[0] == "datatype" or commandArgs[0] == "type"):
        if (handlingCSV):   print("Handling CSV's.")
        else:               print("Handling Pickles.")
    elif (commandArgs[0] == "switch"):
        handlingCSV = not handlingCSV
        if (handlingCSV):   print("Handling CSV's.")
        else:               print("Handling Pickles.")
    elif (commandArgs[0] == "csv"):
        handlingCSV = True
        print("Handling CSV's.")
    elif (commandArgs[0] == "pickle"):
        handlingCSV = False
        print("Handling Pickles.")
    # -------------- EXITING --------------
    elif (command[0] == "exit" or command[0] == "e"):
        print("Exiting program...")
        print("Thank you for using this program!")
        return True
    else:
        print("'"+command+"' is not a valid command.")
    #end
    return False
#end

def main():
    command = "initial"
    exiting = False
    while (not exiting):
        print()
        command = input.askForInput()
        exiting = enactCommand(command)
    #end
#end

#%% MAIN CODE                  ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#Main code start here



#%% SELF-RUN                   ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#Main Self-run block
if __name__ == "__main__":
    
    print(f"\"{module_name}\" module begins.")
    
    #TEST Code
    main()
  