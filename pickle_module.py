#%% MODULE BEGINS
module_name = "pickle_module"

'''
Version: 1.0

Description:
    Class meant to handle Pickle files and
    vector math.

Authors:
    Christian Bankovic
    Wren Caillouet
    Maxwell Benson
    Brian Britton

Date Created     :  11/20/2024
Date Last Updated:  12/08/2024

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
from config import csv_path
from config import dataframe

#other imports
from   copy       import deepcopy as dpcpy
import itertools
import logging
import pandas as pd
import numpy as np
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






#%% DECLARATIONS                ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

#Global declarations Start Here



#Class definitions Start Here
class pickle_manager:
    def __init__(self, pickle_File):
        self.pickle_File = pickle_File
        self.create_Pickle(dataframe)

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
    def __init__(self, pickle_File):
        super().__init__(pickle_File)
        self.df = self.load_Pickle()
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

#-----------------Vector Operations--------------
   
   # Display the vector on the console.
    def display_vector(self, vector_name):
        if vector_name not in self.df.columns:
            print(f"Vector '{vector_name}' not found in the DataFrame.")
            return

        vector = self.df[vector_name].dropna().tolist()
        print(f"Vector '{vector_name}': {vector}")
        return vector
    #end

    # Export the vector to a file in the OUTPUT folder.
    def export_vector(self, vector_name, file_name=None):
        if vector_name not in self.df.columns:
            print(f"Vector '{vector_name}' not found in the DataFrame.")
            return

        vector = self.df[vector_name].dropna().tolist()

        # Define the output file name, defaulting to vector_name_vector.txt
        if file_name is None:
            file_name = f"{vector_name}_vector.txt"
        
        output_file = os.path.join(self.output_folder, file_name)
        
        with open(output_file, "w") as file:
            file.write(f"Vector '{vector_name}':\n")
            for value in vector:
                file.write(f"{value}\n")

        print(f"Vector '{vector_name}' exported to: {output_file}")
        return output_file
    #end

    # Obtain the position vector (for example, 3D vector with x, y, z).
    def obtain_position_vector(self, *columns):
        if len(columns) != 3:
            print("Position vector requires exactly 3 columns")
            return

        for col in columns:
            if col not in self.df.columns:
                print(f"Column '{col}' not found in the DataFrame.")
                return

        # Extract the position vector
        position_vector = self.df[list(columns)].dropna().values.tolist()
        
        # Output file for the position vector
        position_vector_file = os.path.join(self.output_folder, f"position_vector_{'_'.join(columns)}.txt")
        
        with open(position_vector_file, "w") as file:
            file.write(f"Position vector ({columns}):\n")
            for value in position_vector:
                file.write(f"{value}\n")
        
        print(f"Position vector saved to: {position_vector_file}")
        return position_vector
    #end

    # Obtain the unit vector for a given vector.
    def obtain_unit_vector(self, vector_name):
        if vector_name not in self.df.columns:
            print(f"Vector '{vector_name}' not found in the DataFrame.")
            return

        vector = self.df[vector_name].dropna().tolist()

        # Calculate the magnitude (length) of the vector
        magnitude = np.linalg.norm(vector)

        if magnitude == 0:
            print(f"Cannot calculate unit vector for a zero vector.")
            return

        # Calculate unit vector
        unit_vector = [x / magnitude for x in vector]

        # Output file for the unit vector
        unit_vector_file = os.path.join(self.output_folder, f"unit_vector_{vector_name}.txt")

        with open(unit_vector_file, "w") as file:
            file.write(f"Unit vector for '{vector_name}':\n")
            for value in unit_vector:
                file.write(f"{value}\n")

        print(f"Unit vector saved to: {unit_vector_file}")
        return unit_vector
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
    