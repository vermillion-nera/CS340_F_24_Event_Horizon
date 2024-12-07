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
Date Last Updated:  12/06/2024

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
import config
from   config import dataframe
import user_input

#other imports
from   copy       import deepcopy as dpcpy
import pandas as pd
import logging
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

#%% CONSTANTS                   ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

#%% CONFIGURATION               ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~


#%% INITIALIZATIONS             ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
input = user_input.userInput()
logger = logging.getLogger(__name__)

csv_manager = dataframe_module.csv_manager(config.csv_path)

dataframe_manager = dataframe_module.dataframe_manager(dataframe)
wizard = pickle_module.math_wizard("pickle_dataframe.pkl")

commandDictCSV = {
    000: "help",
    100: "print",
    110: "[optional]:",
    120: "unshaped",
    130: "columns",
    140: "rows",
    150: "query",
    160: "boolquery",
    200: "filter",
    210: "columns",
    220: "rows",
    230: "query",
    240: "boolquery",
    250: "reset",
    300: "export",
    400: "datatype",
    500: "switch",
    600: "csv",
    700: "pickle",
    800: "exit",
}
commandDictPickle = {
    000: "help",
    100: "generate",
    110: "permutations",
    120: "combinations",
    200: "vector",
    210: "display",
    220: "export",
    230: "obtain",
    231: "positon",
    232: "unit",
    300: "datatype",
    400: "switch",
    500: "csv",
    600: "pickle",
    700: "exit",
}


#%% DECLARATIONS                ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
handlingCSV = True

#Global declarations Start Here



#Class definitions Start Here

#Function definitions Start Here

def enactCommand(command):
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
        answer = ""
        if (len(commandArgs) == 0 or command == ""):
            print("Please type a command.")
        elif (commandArgs[0] == "help" or commandArgs[0] == "commands"):
            print("----------------------")
            if (len(commandArgs) > 1):
                if (commandArgs[1] == "help"):
                    print("Available 'help' subcommands:")
                    for key, comm in currentHelpDict.items():
                        if (key%100 == 0):
                            print("> "+comm)
                        elif (key%10 == 0):
                            print("  > "+comm)
                        #end
                    #end
                else:
                    commandKey = -1
                    hasSubcommands = False
                    for key, comm in currentHelpDict.items():
                        if (comm == commandArgs[1] and key%100 == 0):
                            commandKey = key
                        elif ((key - commandKey) > 0 and (key - commandKey) < 100):
                            if (not hasSubcommands):
                                print("Available '"+commandArgs[1]+"' subcommands:")
                            #end
                            hasSubcommands = True
                            if (comm != "help"):
                                if    (key%10 == 0):    print("> "+comm)
                                else:                   print("  > "+comm)
                            #end
                        elif ((key - commandKey) > 0 and (key - commandKey) < 10):
                            if (not hasSubcommands):
                                print("Available '"+commandArgs[1]+"' subcommands:")
                            #end
                            hasSubcommands = True
                            if (comm != "help"):
                                print("> "+comm)
                            #end
                        #end
                    #end
                    if (not hasSubcommands):
                        print("No subcommands for '"+commandArgs[1]+"'.")
                    #end
                #end
            else:
                print("Available commands:")
                for key, comm in currentHelpDict.items():
                    if      (key%100 == 0): print("> "+comm)
                    elif    (key%10 == 0):  print("  > "+comm)
                    else:                   print("    > "+comm)
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
            elif (commandArgs[0] == "export"):
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
        else:
            # -------------- TEST FUNCTIONS --------------
            if command == "get unique values":
                 column_name = input.askForInput("Enter column name")
                 wizard.get_unique_values(column_name)
            elif (commandArgs[0] == "generate"):
                if (len(commandArgs) == 1):
                    print("'generate' must come with a subcommand. Valid subcommands include:")
                    print("> 'permutations'")
                    print("> 'combinations'")
                elif (commandArgs[1] == "permutations"):
                    if (len(commandArgs) > 2):
                        answer = " ".join(commandArgs[2:])
                    else:
                        answer = input.askForInput("Enter column name")
                    #end
                    if (answer == "exit"):  print("Skipping generating permutations.")
                    else:                   wizard.generate_permutations(answer)
                elif (commandArgs[1] == "combinations"):
                    if (len(commandArgs) > 2):
                        answer = " ".join(commandArgs[2:])
                    else:
                        answer = input.askForInput("Enter column name")
                    #end
                    if (answer == "exit"):  print("Skipping generating combinations.")
                    else:                   wizard.generate_combinations(answer)  
                else:
                    raise ValueError("'"+commandArgs[1]+"' is not a valid generate subcommand")
                #end
            # -------------- VECTOR FUNCTIONS --------------
            elif (commandArgs[0] == "vector"):
                if (len(commandArgs) == 1):
                    print("'vector' must come with a subcommand. Valid subcommands include:")
                    print("> 'display'")
                    print("> 'export'")
                    print("> 'obtain'")
                    print("  > 'position'")
                    print("  > 'unit'")
                elif (commandArgs[1] == "display"):
                    if (len(commandArgs) > 2):
                        answer = " ".join(commandArgs[2:])
                    else:
                        answer = input.askForInput("Enter vector column name")
                    #end
                    if (answer == "exit"):  print("Skipping displaying vector.")
                    else:                   wizard.display_vector(answer)
                elif (commandArgs[1] == "export"):
                    if (len(commandArgs) > 2):
                        answer = " ".join(commandArgs[2:])
                    else:
                        answer = input.askForInput("Enter vector column name")
                    #end
                    if (answer == "exit"):  print("Skipping exporting vector.")
                    else:                   wizard.export_vector(answer)
                elif (commandArgs[1] == "obtain"):
                    if (len(commandArgs) == 2):
                        print("'vector obtain' must come with a subcommand. Valid subcommands include:")
                        print("> 'position'")
                        print("> 'unit'")
                    elif (commandArgs[2] == "position"):
                        if (len(commandArgs) > 3):
                            answer = " ".join(commandArgs[3:])
                        else:
                            answer = input.askForInput("Enter three column names seperated by a ',' (e.g., x, y, z)")
                        #end
                        if (answer == "exit"):  print("Skipping obtaining position vector.")
                        else:                   wizard.obtain_position_vector(*answer)
                    elif (commandArgs[2] == "unit"):
                        if (len(commandArgs) > 3):
                            answer = " ".join(commandArgs[3:])
                        else:
                            answer = input.askForInput("Enter vector column name")
                        #end
                        if (answer == "exit"):  print("Skipping obtaining unit vector.")
                        else:                   wizard.obtain_unit_vector(answer)
                    else:
                        raise ValueError("'"+commandArgs[2]+"' is not a valid vector obtain subcommand")
                    #end
                else:
                    raise ValueError("'"+commandArgs[1]+"' is not a valid vector subcommand")
                #end
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
  