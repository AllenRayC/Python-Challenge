# Modules
import os
import csv

# Set path for file
csvpath = os.path.join("..", "Resources", "budget_data.csv")

# set variables
months = 0

# Open and read csv
with open(csvpath, newline="") as csvfile:
    csvreader = csv.reader(csvfile)

    # Read the header row first
    csv_header = next(csvfile)
    print(f"Header: {csv_header}")

    # Read through each row of data after the header
    #for row in csvreader:
    #    months += 1
    #    print(months)