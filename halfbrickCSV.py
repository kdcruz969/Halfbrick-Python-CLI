import os 
import csv
import json
from collections import OrderedDict 
from CLIdatasummary import summarise

#Classes for coloured text
class txtcolour:
    GREEN = "\033[1;32;40m"
    RED = "\033[1;31;40m"
    DEFAULT = "\033[0m"

#Opening dialogue
print(txtcolour.GREEN + "This is a CLI program for CSV file conversion by Kyle Dela Cruz for Halfbrick studios.")
print("The three main functions available are:")
print("1. Convert CSV to JSON")
print("2. Present DATA SUMMARY from CSV")
print("3. Generate SQL insert statements from CSV\n" + txtcolour.DEFAULT)

#Select File
try:
    # request filename
    # load data
    print("Input file to begin")
    filename = input("CSV File: ")
    extension = filename.split(".")[-1].lower()
    data = {}
    
    #validate wether file is CSV
    if extension == "csv":
        # load csv file
        with open(filename, encoding='utf-8') as f:
            csvReader = csv.DictReader(f)
            
            for rows in csvReader:
                key = rows['user_pseudo_id']
                data[key] = rows
            
            print ("CSV file loaded")
    #throw unsupported filetype error
    else:
        print (txtcolour.RED + "unsupported file type - exiting" + txtcolour.DEFAULT)
        exit()
    #throw error
except Exception as e:
    # print error message, exit script
    print(txtcolour.RED + "Error opening file - exiting:", e, "" + txtcolour.DEFAULT)
    exit()
else:
    print(txtcolour.GREEN + "Please enter a number corresponding to one of the three program functions:")
    print("1. Convert CSV; 2. Present DATA SUMMARY; 3. SQL INSERT" + txtcolour.DEFAULT)
    
    #Input function
    while True:
        try:
            option = int(input("Please enter option:"))
            if option <1 or option >3:
                raise ValueError
            break
        except ValueError:
            print (txtcolour.RED + "Please enter a number from 1 to 3!" + txtcolour.DEFAULT)
    
    if option == 1:
        #Output file
        converted_file_basename = os.path.basename(filename).split(".")[0]
        converted_file_extension = ".json"
        
        if(os.path.isfile(converted_file_basename + converted_file_extension)):
            counter = 1
            while os.path.isfile(converted_file_basename + " (" + str(counter) + ")" + converted_file_extension):
                counter += 1
            converted_file_basename = converted_file_basename + " (" + str(counter) + ")"
        try:
            if converted_file_extension == ".json":
                with open(converted_file_basename + converted_file_extension, 'w', encoding='utf-8') as outfile:
                    outfile.write(json.dumps(data, indent=4))
        #throw error
        except Exception as e: 
            print(txtcolour.RED + "Error creating file - exiting:", e, "" + txtcolour.DEFAULT)
        #confirm JSON file creation
        else:
            print(txtcolour.GREEN + "File Created: " + converted_file_basename + converted_file_extension + txtcolour.DEFAULT)
            
    elif option == 2:
        print("option 2")
        summarise(filename)
    elif option == 3:
        print("option 3")
    else:
        print (txtcolour.RED + "ERROR - exiting" + txtcolour.DEFAULT)
        exit()
