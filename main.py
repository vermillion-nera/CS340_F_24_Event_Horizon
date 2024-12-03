#%% MODULE BEGINS
module_name = 'main'

'''
Version: 1.0

Description:
    Imports the classes from dataframe_module, pickle_module, and
    config. Also runs the entire program, asking
    the user for commands and enacting them until
    the user types 'exit'.

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
import dataframe_module
import pickle_module
import logging
import config

#other imports
from   copy       import deepcopy as dpcpy
import pandas as pd
import logger
import os


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


#%% INITIALIZATIONS             ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
input = config.userInput()
logger = logging.getLogger(__name__)

csv_manager = dataframe_module.csv_manager(config.csv_path)

dataframe = pd.read_csv(config.csv_path)
dataframe_manager = dataframe_module.dataframe_manager(dataframe)
wizard = pickle_module.math_wizard()


classPickle = pickle_module.math_wizard()
commandDictCSV = { # TODONE: Put this into a dictionary
    0: "help",
    1: "print",
    1.01: "[optional]:",
    1.02: "unshaped",
    1.03: "columns",
    1.04: "rows",
    1.05: "query",
    1.06: "boolquery",
    2: "filter",
    2.01: "columns",
    2.02: "rows",
    2.03: "query",
    2.04: "boolquery",
    2.05: "reset",
    3: "export",
    4: "datatype",
    5: "switch",
    6: "csv",
    7: "pickle",
    8: "exit",
}
commandDictPickle = { # TODOING: Update this as needed
    0: "help",
    # pickle commands go here
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

def enactCommand(command): # TODONE: Implement try catch statement, and if it catches an error, log it and continue on (not enacting a command shouldn't break ).
    logging.info(command)
    global handlingCSV
    global commandDictCSV
    global commandDictPickle

    currentHelpDict = commandDictCSV
    if (not handlingCSV):
        currentHelpDict = commandDictPickle
    #end

    commandArgs = command.split(" ")
    try:
        # TODONE: Implement "subcommands" of nested if statements. For instance, if (print), if (unshaped), elif (columns), etc
        # Might be able to do this by split()ing our command into arguments separated by spaces
        answer = ""
        if (len(commandArgs) == 0 or command == ""):
            print("Please type a command.")
        elif (commandArgs[0] == "help" or commandArgs[0] == "commands"): # TODONE: Perhaps make help for subcommands?
            print("----------------------")
            if (len(commandArgs) > 1):
                if (commandArgs[1] == "help"):
                    print("Available 'help' subcommands:")
                    for key, comm in currentHelpDict.items():
                        if (key%1 == 0):
                            print("> "+comm)
                        #end
                    #end
                else:
                    commandKey = -1
                    hasSubcommands = False
                    for key, comm in currentHelpDict.items():
                        if (comm == commandArgs[1] and key%1 == 0):
                            commandKey = key
                        elif ((key - commandKey) > 0 and (key - commandKey) < 1):
                            if (not hasSubcommands):
                                print("Available '"+commandArgs[1]+"' subcommands:")
                            #end
                            hasSubcommands = True
                            print("> "+comm)
                        #end
                    #end
                    if (not hasSubcommands):
                        print("No subcommands for '"+commandArgs[1]+"'.")
                    #end
                #end
            else:
                print("Available commands:")
                for key, comm in currentHelpDict.items():
                    if (key%1 != 0):
                        print("  > "+comm)
                    else:
                        print("> "+comm)
                    #end
                #end
            #end
            print("----------------------")
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
        elif (commandArgs[0] == "exit" or commandArgs[0] == "e"):
            print("Exiting program...")
            print("Thank you for using this program!")
            return True # This is to indicate we ARE exiting.
        # -------------- CSV HANDLING --------------
        elif (handlingCSV):
            # -------------- TEST FUNCTIONS --------------
            if (command == "print histogram" or command == "plot histogram" or command == "print line plot" or command == "plot line plot"):
                column_name = input.askForInput("Enter column name for histogram or line chart: ")  
                dataframe_manager.plotAllColumnsHist(column_name, save=True)
            elif (command == "studyTime vs parentalSupport"):
                csv_manager.Violin_StudyTimeWeekly_vs_ParentalSupport()
            elif (command == "GPA vs Gender"):
                csv_manager.Violin_GPA_vs_Gender()
            elif (command == "Absences vs GradeClass"):
                csv_manager.Box_Absences_vs_GradeClass()
            elif (command == "GPA vs ParentalEducation"):
                csv_manager.Box_GPA_vs_ParentalEducation()
            elif (command == "StudyTimeWeekly vs GPA"):
                csv_manager.scatter_StudyTimeWeekly_vs_GPA()
            elif (command == "Age vs Absences"):
                csv_manager.scatter_Age_vs_Absences()
            elif command == "get unique values":
                 column_name = input.askForInput("Enter column name: ")
                 wizard.inputPickle("pickle_dataframe.pkl") 
                 wizard.get_unique_values(column_name)
            elif command == "generate permutations":
                 column_name = input.askForInput("Enter column name: ")
                 wizard.inputPickle("pickle_dataframe.pkl")
                 wizard.generate_permutations(column_name)
            elif command == "generate combinations":
                 column_name = input.askForInput("Enter column name: ")
                 wizard.inputPickle("pickle_dataframe.pkl")
                 wizard.generate_combinations(column_name)
            # -------------- PRINTING --------------
            elif (commandArgs[0] == "print"):
                if (len(commandArgs) == 1): # default
                    csv_manager.printDataFrame()
                elif (commandArgs[1] == "unshaped" or commandArgs[1] == "original"):
                    csv_manager.printDataFrameOriginal()
                elif (commandArgs[1] == "columns" or commandArgs[1] == "column"):
                    if (len(commandArgs) > 2):
                        answer = " ".join(commandArgs[2:])
                    else:
                        answer = input.askForInput("Columns to print")
                    #end
                    if (answer == "exit"):  print("Skipping print.")
                    else:                   csv_manager.printColumns(answer)
                elif (commandArgs[1] == "rows" or commandArgs[1] == "row"):
                    if (len(commandArgs) > 2):
                        answer = " ".join(commandArgs[2:])
                    else:
                        answer = input.askForInput("Rows to print")
                    #end
                    if (answer == "exit"):  print("Skipping print.")
                    else:                   csv_manager.printRows(answer)
                elif (commandArgs[1] == "query"):
                    if (len(commandArgs) > 2):
                        answer = " ".join(commandArgs[2:])
                    else:
                        answer = input.askForInput("Query")
                    #end
                    if (answer == "exit"):  print("Skipping print.")
                    else:                   csv_manager.printQuery(answer)
                elif (commandArgs[1] == "boolquery" or commandArgs[1] == "booleanquery"):
                    if (len(commandArgs) > 2):
                        answer = " ".join(commandArgs[2:])
                    else:
                        answer = input.askForInput("Boolean index query")
                    #end
                    if (answer == "exit"):  print("Skipping print.")
                    else:                   csv_manager.printBooleanQuery(answer)
                else:
                    raise ValueError("'"+commandArgs[1]+"' is not a valid print subcommand.")
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
                    if (len(commandArgs) > 2):
                        answer = " ".join(commandArgs[2:])
                    else:
                        answer = input.askForInput("Columns to filter")
                    #end
                    if (answer == "exit"):
                        print("Skipping filter.")
                    else:
                        csv_manager.filterColumns(answer)
                        print("Filtered by '"+answer+"' columns.")
                    #end
                elif (commandArgs[1] == "rows" or commandArgs[1] == "row"):
                    if (len(commandArgs) > 2):
                        answer = " ".join(commandArgs[2:])
                    else:
                        answer = input.askForInput("Rows to filter")
                    #end
                    if (answer == "exit"):
                        print("Skipping filter.")
                    else:
                        csv_manager.filterRows(answer)
                        print("Filtered by '"+answer+"' rows.")
                    #end
                elif (commandArgs[1] == "query"):
                    if (len(commandArgs) > 2):
                        answer = " ".join(commandArgs[2:])
                    else:
                        answer = input.askForInput("Query")
                    #end
                    if (answer == "exit"):
                        print("Skipping filter.")
                    else:
                        csv_manager.filterQuery(answer)
                        print("Filtered by '"+answer+"'.")
                    #end
                elif (commandArgs[1] == "boolquery" or commandArgs[1] == "booleanquery"):
                    if (len(commandArgs) > 2):
                        answer = " ".join(commandArgs[2:])
                    else:
                        answer = input.askForInput("Boolean index query")
                    #end
                    if (answer == "exit"):
                        print("Skipping filter.")
                    else:
                        csv_manager.filterBooleanQuery(answer)
                        print("Filtered by '"+answer+"'.")
                elif (commandArgs[1] == "reset"):
                    csv_manager.resetShape()
                    print("Dataframe filter reset.")
                else:
                    raise ValueError("'"+commandArgs[1]+"' is not a valid filter subcommand")
            # -------------- EXPORTING --------------
            elif (commandArgs[0] == "export"): # TODONE: Allow for exporting the filtered table into a CSV/TXT file
                if (len(commandArgs) > 1):
                    answer = " ".join(commandArgs[1:])
                else:
                    answer = input.askForInput("Filename")
                #end
                if (answer == "exit"):
                    print("Skipping export.")
                else:
                    csv_manager.export(answer)
                    print("Exported dataframe to 'OUTPUT/"+answer+"'.")
                #end
            else:
                raise ValueError("'"+command+"' is not a valid command.")
        # -------------- PICKLE HANDLING --------------
        else: #TODO: Fill this out with methods for handling pickle files
            if (commandArgs[0] == "first"):
                if (len(commandArgs) == 1):
                    print("first default pickle")
                elif (commandArgs[1] == "first"):
                    print("first first pickle")
                elif (commandArgs[1] == "second"):
                    print("first second pickle")
                else:
                    raise ValueError("'"+commandArgs[1]+"' is not a valid first pickle subcommand.")
            elif (commandArgs[0] == "second"):
                print("second pickle")
            else:
                raise ValueError("'"+command+"' is not a valid command.")
            #end
        #end
    except ValueError as e:
        logging.error(e)
        print(e)
    except pd.errors.UndefinedVariableError as e:
        logging.error(e)
        print(e)
    except KeyError as e:
        logging.error("Invalid key:\t"+str(e))
        print("Invalid key:\t"+str(e))
    except TypeError as e:
        logging.error(e)
        print(e)
    except SyntaxError as e:
        logging.error("Syntax error. What in the world happened??")
        logging.error(e)
        print("Syntax error. What in the world happened??")
        print(e)
    #end
    return False # This is to indicate we are not exiting yet.
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
  