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
csv_path = "CSV_sterilizer/Student_performance_data.csv"
dataframe = pd.read_csv(csv_path)
logger = logging.getLogger(__name__)


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

def enactCommand(command): # TODO: Implement try catch statement, and if it catches an error, log it and continue on (not enacting a command shouldn't break ).
    logging.info(command)
    global handlingCSV
    global commandList
    try:
        
       
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
            if (handlingCSV):   classCSV.printColumns(input.askForInput("Columns to print"))
            else:               print("Unimplemented.")
        elif (command == "print rows" or command == "print row"):
            if (handlingCSV):   classCSV.printRows(input.askForInput("Rows to print"))
            else:               print("Unimplemented.")
        elif (command == "print query"):
            if (handlingCSV):   classCSV.printQuery(input.askForInput("Query"))
            else:               print("Unimplemented.")
        elif (command == "filter columns" or command == "filter column"):
            if (handlingCSV):
                answer = input.askForInput("Columns to filter")
                classCSV.filterColumns(answer)
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
        elif (command == "filter query"):
            if (handlingCSV):
                answer = input.askForInput("Query")
                classCSV.filterQuery(answer)
                print("Filtered by '"+answer+"'.")
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
            # TODO: Allow for exporting the filtered table into a CSV/TXT file
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
        elif (command == "print histogram" or command == "plot histogram"):
            if handlingCSV:   #indentation?
                column_name = input.askForInput("Enter column name for histogram/bar chart: ")  
                parentCSV.plotAllColumnsHist(column_name, save=True) 
        elif (command == "studyTime vs parentalSupport"):
            classCSV.Violin_StudyTimeWeekly_vs_ParentalSupport() #indentation?
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
        elif (command == "exit" or command == "e"):
            print("Exiting program...")
            print("Thank you for using this program!")
        else:
            raise ValueError("Invalid command entered.")
        #else:
            #print("'"+command+"' is not a valid command.")
        #end
    #end
    except ValueError as e:
        logging.error("Invalid command entered")
        print(e)


        #end
    #end
    except pd.errors.UndefinedVariableError as e:
        logging.error("Invalid query input")
        print("Invalid query input")

    
def main():
    command = "initial"
    while (command != "exit" and command != "e"):
        command = input.askForInput()
        enactCommand(command)
    #end
    
    pass
#
    
    #

#%% MAIN CODE                  ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#Main code start here



#%% SELF-RUN                   ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#Main Self-run block
if __name__ == "__main__":
    
    print(f"\"{module_name}\" module begins.")
    
    #TEST Code
    main()
  