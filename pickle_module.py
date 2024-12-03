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
import itertools
import logging
import pandas as pd
import dataframe_module
from config import csv_path
import os


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
        super().__init__(pickle_File=None)
        self.df = None
        self.output_folder = "OUTPUT"  
        os.makedirs(self.output_folder, exist_ok=True)  
        print("Math Wizard initialized.")
    #end

    def inputPickle(self, pickle):
        self.pickle_File = pickle
        self.df = self.load_Pickle()
        if self.df is not None:
            print("DataFrame loaded into Math Wizard.")
        else:
            print("Failed to load DataFrame.")
    #end
    
    #Getting Unique Values
    def get_unique_values(self, column_name):
        if self.df is None:
            print("No DataFrame loaded. Please load a pickle first.")
            return []
        
        if column_name not in self.df.columns:
            print(f"Column '{column_name}' not found in the DataFrame.")
            return []
        
        unique_values = self.df[column_name].dropna().unique().tolist()
        output_file = os.path.join(self.output_folder, f"unique_values_{column_name}.txt")
        
        with open(output_file, "w") as file:
            file.write(f"Unique values for '{column_name}':\n")
            for value in unique_values:
                file.write(f"{value}\n")
        
        print(f"Unique values saved to: {output_file}")
        return unique_values
    #end
    # Generating Permutations
    def generate_permutations(self, column_name):
        unique_values = self.get_unique_values(column_name)
        if not unique_values:
            return []
        
        permutations = list(itertools.permutations(unique_values))
        output_file = os.path.join(self.output_folder, f"permutations_{column_name}.txt")
        
        with open(output_file, "w") as file:
            file.write(f"Permutations for '{column_name}':\n")
            for perm in permutations:
                file.write(f"{perm}\n")
        
        print(f"Permutations saved to: {output_file}")
        return permutations
    #end

    # Generating Combinations
    def generate_combinations(self, column_name):
        unique_values = self.get_unique_values(column_name)
        if not unique_values:
            return []
        
        output_file = os.path.join(self.output_folder, f"combinations_{column_name}.txt")
        
        with open(output_file, "w") as file:
            file.write(f"Combinations for '{column_name}':\n")
            for r in range(1, len(unique_values) + 1):
                combinations = list(itertools.combinations(unique_values, r))
                file.write(f"Combinations of length {r}:\n")
                for comb in combinations:
                    file.write(f"{comb}\n")
        
        print(f"Combinations saved to: {output_file}")
        return combinations
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