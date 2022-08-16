from os.path import isfile, join
from decimal import Decimal
from os import listdir
import csv


sum = 0
path = 'files'
greatest_values = []

# Gets all files and directories from a diretory and writes all file-entries in array
onlyfiles = [f for f in listdir(path) if isfile(join(path, f))]

# For every file in the array
for file in onlyfiles:
    greatest_value = 0
    # Open File (path + filename)
    with open(join(path, file), newline='') as csvfile:
        reader = csv.DictReader(csvfile)
        # Iterate through every line of file
        for row in reader:
            # Row-name is the 'Date: ' + file name - 'classic_/meraki_' - '.csv' ending
            # Split file into array with '_' as separator
            # Take the second element of the array -> filename - classic/meraki
            # Remove last four characters from file -> - '.csv'
            row_name = 'Date: ' + file.split('_')[1][:-4]
            if 'time' in row[row_name]:
                # Same Process as above
                value = Decimal(row[row_name].split('time=')[1][:-3])
                # If value is greater than any before, save it
                if value > greatest_value:
                    greatest_value = value

    # Print filename + greatest value
    greatest_values.append(greatest_value)
    print(file + ': ' + str(greatest_value))

for value in greatest_values:
    sum += value
schnitt = sum / len(greatest_values)
print('Schnitt: ' + str(schnitt))
