# import csv tool

# import statements to pull from the command line
import sys
import csv
import pandas as pd

csv_file = pd.read_csv(sys.argv[1])
    
